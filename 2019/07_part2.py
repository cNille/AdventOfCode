from intcode import *
input_code = open('07.input', 'r').readline().strip()
input_code = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'

phaseSettings = permutations([5,6,7,8,9])
res = 0
p = []
values = {}

for phase in phaseSettings:
    phase = [9,8,7,6,5]
    names = ["A", "B", "C","D","E"]
    stream = Streams(names)
    programs = [
        Program(IntCode(input_code), name="A", stream=stream),
        Program(IntCode(input_code), name="B", stream=stream),
        Program(IntCode(input_code), name="C", stream=stream),
        Program(IntCode(input_code), name="D", stream=stream),
        Program(IntCode(input_code), name="E", stream=stream),
    ]
    stream.add("A", phase[0])
    stream.add("A", 0)
    stream.add("B", phase[1])
    stream.add("C", phase[2])
    stream.add("D", phase[3])
    stream.add("E", phase[4])
    
    count = 0
    while count < 100:   
        count += 1
        for out in programs[0].run():
            stream.add(names[1], out)
            break
        for out in programs[1].run():
            stream.add(names[2], out)
            break
        for out in programs[2].run():
            stream.add(names[3], out)
            break
        for out in programs[3].run():
            stream.add(names[4], out)
            break
        for out in programs[4].run():
            stream.add(names[0], out)
            E = out 
            if E > res:
                res = E
                p = phase
            break


    exit()

print('Part 2 result: %d ' % res)
exit()

from itertools import permutations
from collections import deque 

f = open('07.input', 'r')
content = [x.strip() for x in f.readlines()]

def program(programCode):
    state = datas[programCode]
    data, curr = state
    while data[curr] != 99:
        opcode = data[curr] % 100
        mode_a = data[curr] % 1000
        mode_a = mode_a > 99
        mode_b = data[curr] % 10000
        mode_b = mode_b > 999
        mode_c = data[curr] % 100000
        mode_c = mode_c > 9999

        A = data[curr+1] if mode_a else data[data[curr+1]]
        if opcode in [1,2,5,6,7,8]:
            B = data[curr+2] if mode_b else data[data[curr+2]]
        
        if opcode == 1:
            data[data[curr+3]] = A + B
            curr += 4
        elif opcode == 2:
            data[data[curr+3]] = A * B
            curr += 4
        elif opcode == 3:
            if len(outputs[programCode]) > 0:
                val = outputs[programCode].popleft()
                data[data[curr+1]] = val 
                curr += 2
            else:
                return
        elif opcode == 4:
            outputs[nextP[programCode]].append(A)
            datas[programCode] = (data, curr)
            q.append(nextP[programCode])
            curr += 2
        elif opcode == 5:
            if A != 0:
                curr = B
            else:
                curr += 3
        elif opcode == 6:
            if A == 0:
                curr = B
            else: 
                curr += 3
        elif opcode == 7:
            data[data[curr+3]] = 1 if A < B else 0
            curr += 4
        elif opcode == 8:
            data[data[curr+3]] = 1 if A == B else 0
            curr += 4
        else: 
            print('fatal error, opcode received: %d' % opcode)
            exit()
        datas[programCode] = (data, curr)
    return 

def new_data():
    return [int(x) for x in content[0].split(',')]

nextP = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'e',
    'e': 'a',
}

q = deque('abcde')
res = 0
p = []

phaseSettings = permutations([5,6,7,8,9])
for phase in phaseSettings:
    q = deque('abcde')
    outputs = {
        'a': deque([phase[0], 0]),
        'b': deque([phase[1]]),
        'c': deque([phase[2]]),
        'd': deque([phase[3]]),
        'e': deque([phase[4]]),
    }
    datas = {
        'a': (new_data(), 0),
        'b': (new_data(), 0),
        'c': (new_data(), 0),
        'd': (new_data(), 0),
        'e': (new_data(), 0),
    }
    while len(q) > 0:
        code = q.popleft()
        program(code)


    a = outputs['a'][0]
    if a > res:
        res = a
        p = phase

    
print("Part 2 solution: %d " % res)
