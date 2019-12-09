from itertools import permutations

f = open('09.input', 'r')
content = ["1102,34915192,34915192,7,4,7,99,0"]
content = ["104,1125899906842624,99"]
content = ["109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"]
content = [x.strip() for x in f.readlines()]

def val(data, mode, idx, relative):
    if mode == 0:
        return position(data, idx)
    elif mode == 1:
        return immediate(data, idx)
    elif mode == 2:
        return immediate(data, relative + immediate(data, idx))
    else:
        exit('NOOOOOO')
    
def immediate(data,idx):
    return get(data, idx)

def rel_pos(data,idx):
    return get(data, idx)
     
def position(data,idx):
    return get(data, get(data, idx))

def get_modes(opcode):
    mode_a = (opcode % 1000) / 100
    mode_b = (opcode % 10000) / 1000
    mode_c = (opcode % 100000) / 10000
    return mode_a, mode_b, mode_c

mem = {}
def save(data, pos, val):
    if pos > len(data):
        mem[pos] = val
    else:
        data[pos] = val
    return data

def get(data, pos, mode_c=0, relative=0):
    if mode_c == 2:
        return _get(data,pos) + relative
    else:
        return _get(data,pos)

def _get(data, pos):
    if pos > len(data):
        if pos not in mem:
            mem[pos] = 0
        return mem[pos] 
    else:
        return data[pos] 
    

def add(data,A,B,curr, mode_c,relative):
    return save(data, get(data, curr+3, mode_c,relative), A+B), curr + 4

def multiply(data,A,B,curr, mode_c,relative):
    return save(data, get(data, curr+3, mode_c, relative), A * B), curr + 4

def inputs(data,inputInt,curr,mode_c,relative):
    return save(data, get(data, curr+1, mode_c,relative), inputInt), curr + 2

def outputs(data,A,curr):
    #print("OUTPUT %d" % A)
    return data, curr + 2, A

def goto_true(A,B,curr):
    return B if A != 0 else curr+3

def goto_false(A,B,curr):
    return B if A == 0 else curr+3

def less(data, A, B, curr, mode_c,relative):
    save(data, get(data, curr+3, mode_c,relative), 1 if A < B else 0)
    curr += 4
    return data, curr

def equals(data, A, B, curr, mode_c,relative):
    save(data, get(data, curr+3, mode_c,relative), 1 if A == B else 0)
    curr += 4
    return data, curr

def update_relative(relative, A, curr):
    return relative + A, curr+2

def program(inputInt):
    data = [int(x) for x in content[0].split(',')]
    curr = 0
    output = ""
    relative = 0
    while data[curr] != 99:
        #print("OPERATION %d: %d %d %d %d" % (curr, data[curr], data[curr+1], data[curr+2], data[curr+3]))
        opcode = data[curr] % 100
        mode_a, mode_b, mode_c = get_modes(data[curr])

        A = val(data, mode_a, curr+1, relative)
        if opcode in [1,2,5,6,7,8]:
            B = val(data, mode_b, curr+2, relative)
        
        if opcode == 1:
            data, curr = add(data,A,B,curr, mode_c,relative)
        elif opcode == 2:
            data, curr = multiply(data,A,B,curr, mode_c,relative)
        elif opcode == 3:
            data, curr = inputs(data, inputInt, curr, mode_a, relative)
        elif opcode == 4:
            data, curr, output = outputs(data,A,curr)
        elif opcode == 5:
            curr = goto_true(A,B,curr) 
        elif opcode == 6:
            curr = goto_false(A,B,curr)
        elif opcode == 7:
            data, curr = less(data,A,B,curr, mode_c,relative)
        elif opcode == 8:
            data, curr = equals(data,A,B,curr, mode_c,relative)
        elif opcode == 9:
            relative, curr = update_relative(relative, A, curr)
        else: 
            exit('fatal error, opcode received: %d' % opcode)
    return output

print('Part 1 result: %d ' % program(1))
print('Part 2 result: %d ' % program(2))
