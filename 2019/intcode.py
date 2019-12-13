from itertools import permutations
from collections import deque 

# Operation codes
OP_ADD = 1
OP_MUL = 2
OP_INP = 3
OP_OUT = 4
OP_JIT = 5
OP_JIF = 6
OP_LES = 7
OP_EQL = 8
OP_END = 99
        
class IntCode:
    def __init__(self, intcode):
        self.instructions = map(int, intcode.split(','))
    def get_code(self):
        return self.instructions

class Streams:
    def __init__(self, names):
        self.inputStreams = {}
        for name in names:
            self.inputStreams[name] = deque()

    def get(self, name):
        return self.inputStreams[name]

    def popleft(self, name):
        val = self.inputStreams[name].popleft() 
        return val

    def log(self):
        return self.inputStreams

    def hasNext(self,name):
        return len(self.inputStreams[name]) > 0

    def add(self, name, val):
        self.inputStreams[name].append(val)

class Stack:
    def __init__(self, intcode):
        assert isinstance(intcode, IntCode)
        self.stack = intcode.get_code()
        self.index = 0
        #self.manual_update = True
        self.waiting = False

    def execute(self):
        while self.index < len(self.stack): 
            if self.waiting:
                self.waiting = False
                break
            # if not self.manual_update:
            #     self.index += 1
            # self.manual_update = False
            yield self.stack[self.index]
            
    def wait(self):
        self.waiting = True

    def update_index(self, new_index):
        self.index = new_index
        # self.manual_update = True

    def save_value(self, address, value):
        self.stack[self.stack[address]] = value

    def get_immediate(self,address):
        return self.stack[address]

    def get_value(self,address):
        return self.stack[self.stack[address]]

class OpCode:
    def __init__(self, code):
        self.code = code % 100
        self.mode_a = code % 1000
        self.mode_a = self.mode_a > 99
        self.mode_b = code % 10000
        self.mode_b = self.mode_b > 999
        self.mode_c = code % 100000
        self.mode_c = self.mode_c > 9999

    def __str__(self):
        return "%d %s %s %s " % (self.code, str(self.mode_a),str(self.mode_b),  str(self.mode_b))

def one_input(func):
    def f(self, opcode):
        if opcode.mode_a:
            A = self.stack.get_immediate(self.stack.index + 1)
        else:
            A = self.stack.get_value(self.stack.index + 1)
        func(self,A)
        self.stack.update_index(self.stack.index + 2)
    return f

def two_input(func):
    def f(self, opcode):
        if opcode.mode_a:
            A = self.stack.get_immediate(self.stack.index + 1)
        else:
            A = self.stack.get_value(self.stack.index + 1)
        if opcode.mode_b:
            B = self.stack.get_immediate(self.stack.index + 2)
        else:
            B = self.stack.get_value(self.stack.index + 2)
        func(self,A, B)
        self.stack.update_index(self.stack.index + 3)
    return f

def three_input(func):
    def f(self, opcode):
        if opcode.mode_a:
            A = self.stack.get_immediate(self.stack.index + 1)
        else:
            A = self.stack.get_value(self.stack.index + 1)
        if opcode.mode_b:
            B = self.stack.get_immediate(self.stack.index + 2)
        else:
            B = self.stack.get_value(self.stack.index + 2)
        if opcode.mode_c:
            C = self.stack.get_immediate(self.stack.index + 3)
        else:
            C = self.stack.get_value(self.stack.index + 3)

        func(self,A,B,C)
        self.stack.update_index(self.stack.index + 4)
    return f

class Program:
    def __init__(self, intcode, stream=None, name="", verbose=False):
        assert stream != None
        assert len(name) > 0
        self.intcode = intcode
        self.name = name
        self.args = []
        self.stream = stream
        self.stack = None
        self.output = []
        self.wait = False
        self.stack = Stack(self.intcode)
        self.operations = { 
            OP_ADD: self.add,
            OP_MUL: self.multiply,
            OP_INP: self.stdin,
            OP_OUT: self.stdout,
            OP_JIT: self.jumptrue,
            OP_JIF: self.jumpfalse,
            OP_LES: self.less,
            OP_EQL: self.equals,
        }
        self.verbose = verbose

    def log(self, *args):
        if self.verbose:
            print(args)

    @three_input
    def add(self, A, B, C):
        self.stack.save_value(self.stack.index+3, A + B)

    @three_input
    def multiply(self, A, B, C):
        self.stack.save_value(self.stack.index+3, A * B)
        
    @one_input
    def stdin(self, inp):
        self.log("Input", self.name, self.args)
        if self.stream.hasNext(self.name):
            val = self.stream.popleft(self.name)
            A = self.stack.get_immediate(self.stack.index + 1)
            self.stack.save_value(self.stack.index+1, val)
        else:
            self.stack.wait()

    @one_input
    def stdout(self, A):
        self.log("Output", self.name, A)
        self.output.append(A)

    @two_input
    def jumptrue(self, A, B):
        if A != 0:
            self.stack.update_index(B-3)

    @two_input
    def jumpfalse(self, A, B):
        if A == 0:
            self.stack.update_index(B-3)

    @three_input
    def less(self, A, B, C):
        if A < B:
            self.stack.save_value(self.stack.index+3, 1)
        else:
            self.stack.save_value(self.stack.index+3, 0)

    @three_input
    def equals(self, A, B, C):
        if A == B:
            self.stack.save_value(self.stack.index+3, 1)
        else:
            self.stack.save_value(self.stack.index+3, 0)
        
    def run(self, *argv, **kwargs):
        get_stack = False
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                if key == 'get_stack':
                    get_stack = True
        
        count = 0 
        for instruction in self.stack.execute():
            count += 1
            op = OpCode(instruction)
            self.log(self.name, self.stack.index, self.stack.stack[self.stack.index:self.stack.index+4])

            if op.code == OP_END:
                break
            elif op.code in self.operations:
                self.operations[op.code](op)
            else:
                print("Err opcode", op.code)
                exit()

            if len(self.output) > 0:
                yield self.output.pop(0) 

        self.wait = False
        if get_stack:
            yield self.stack
