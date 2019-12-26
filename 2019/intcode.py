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
OP_REL = 9
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
        print(self.inputStreams)

    def hasNext(self,name):
        return len(self.inputStreams[name]) > 0

    def add(self, name, val):
        self.inputStreams[name].append(val)

class Stack:
    def __init__(self, intcode):
        assert isinstance(intcode, IntCode)
        self.stack = intcode.get_code()
        self.index = 0
        self.relative = 0
        #self.manual_update = True
        self.waiting = False
        self.memory = {}

    def execute(self):
        while self.index < len(self.stack): 
            if self.waiting:
                self.waiting = False
                break
            # if not self.manual_update:
            #     self.index += 1
            # self.manual_update = False
            inst= self._get(self.index)
            yield inst
            
    def wait(self):
        self.waiting = True

    def update_relative(self, r):
        self.relative += r

    def update_index(self, new_index):
        self.index = new_index
        # self.manual_update = True

    def save_immediately(self, address, value):
        if address >= len(self.stack) or address < 0:
            self.memory[address] = value
        else:
            self.stack[address] = value

    def save_value(self, address, value):
        a = self._get(address)
        if a >= len(self.stack) or a < 0:
            self.memory[a] = value
        else:
            self.stack[a] = value

    def get_immediate(self,address):
        return self._get(address) 

    def get_value(self,address):
        return self._get(self._get(address))

    def get_relative(self,address):
        return self._get(self._get(address) + self.relative)

    def _get(self, address):
        if address >= len(self.stack) or address < 0:
            if address not in self.memory:
                self.memory[address] = 0
            return self.memory[address]
        else:
            return self.stack[address]

class OpCode:
    def __init__(self, code):
        self.code = code % 100
        self.mode_a = (code % 1000) / 100
        self.mode_b = (code % 10000) / 1000
        self.mode_c = (code % 100000) / 10000

    def __str__(self):
        return "Opcode(%d %d %d %d)" % (self.code, self.mode_a, self.mode_b, self.mode_c)


def get_param(self, mode, idx_diff):
    idx = self.stack.index + idx_diff
    if mode == 0:
        return self.stack.get_value(idx)
    elif mode == 1:
        return self.stack.get_immediate(idx)
    elif mode == 2:
        return self.stack.get_relative(idx)

def one_input(func):
    def f(self, opcode):
        A = get_param(self, opcode.mode_a,  1)
        func(self,A, opcode.mode_a)
        self.stack.update_index(self.stack.index + 2)
    return f

def two_input(func):
    def f(self, opcode):
        A = get_param(self, opcode.mode_a,  1)
        B = get_param(self, opcode.mode_b,  2)
        func(self,A, B)
        self.stack.update_index(self.stack.index + 3)
    return f

def three_input(func):
    def f(self, opcode):
        A = get_param(self, opcode.mode_a,  1)
        B = get_param(self, opcode.mode_b,  2)
        if opcode.mode_c == 2:
            C = self.stack.relative + get_param(self, 1, 3)  
        else: 
            C = self.stack.index + 3 
        func(self,A,B,C, opcode.mode_c)
        self.stack.update_index(self.stack.index + 4)
    return f

class Program:
    def __init__(self, intcode, stream=None, name="", verbose=True):
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
            OP_REL: self.relative,
        }
        self.verbose = verbose

    def log(self, *args):
        if self.verbose:
            print(args)

    @three_input
    def add(self, A, B, C, mode_c):
        if mode_c == 2:
            self.stack.save_immediately(C, A + B)
            return
        self.stack.save_value(C, A + B)

    @three_input
    def multiply(self, A, B, C, mode_c):
        if mode_c == 2:
            self.stack.save_immediately(C, A * B)
            return
        self.stack.save_value(C, A * B)
        
    @one_input
    def stdin(self, A, mode):
        #self.log("Input", self.name, self.args)
        if self.stream.hasNext(self.name):
            val = self.stream.popleft(self.name)

            if mode == 2:
                v = self.stack.get_immediate(self.stack.index + 1)
                self.stack.save_immediately(self.stack.relative + v, val)
            else:
                self.stack.save_value(self.stack.index+1, val)
        else:
            self.stack.update_index(self.stack.index - 2)
            self.wait = True
            self.stack.wait()

    @one_input
    def stdout(self, A, mode):
        #self.log("Output", self.name, A)
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
    def less(self, A, B, C, mode_c):

        if mode_c == 2:
            if A < B:
                self.stack.save_immediately(C, 1)
            else:
                self.stack.save_immediately(C, 0)
            return
            
        if A < B:
            self.stack.save_value(C, 1)
        else:
            self.stack.save_value(C, 0)

    @three_input
    def equals(self, A, B, C, mode_c):
        if mode_c == 2:
            if A == B:
                self.stack.save_immediately(C, 1)
            else:
                self.stack.save_immediately(C, 0)
            return
        if A == B:
            self.stack.save_value(C, 1)
        else:
            self.stack.save_value(C, 0)

    @one_input
    def relative(self, A, mode):
        self.stack.update_relative(A)
        
    def run(self, *argv, **kwargs):
        get_stack = False
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                if key == 'get_stack':
                    get_stack = True
        
        for instruction in self.stack.execute():
            #print "INSTRUCTION", instruction
            op = OpCode(instruction)
            #self.log(self.name, self.stack.index, self.stack.stack[self.stack.index:self.stack.index+4])
            

            if op.code == OP_END:
                break
            elif op.code in self.operations:
                self.operations[op.code](op)
            else:
                print("Err opcode", op.code)
                exit()

            if len(self.output) > 0:
                yield self.output.pop(0) 

        if self.wait:
            #yield "INPUT" 
            self.wait = False
            return
        if get_stack:
            yield self.stack
