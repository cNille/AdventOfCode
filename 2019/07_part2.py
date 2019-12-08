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
