from itertools import permutations

f = open('07.input', 'r')
content = [x.strip() for x in f.readlines()]

def program(phase, inputInt):
    data = [int(x) for x in content[0].split(',')]
    curr = 0
    output = ""
    inputCurr = 0
    while data[curr] != 99:
        opcode = data[curr] % 100
        mode_a = data[curr] % 1000
        mode_a = mode_a > 99
        mode_b = data[curr] % 10000
        mode_b = mode_b > 999
        mode_c = data[curr] % 100000
        mode_c = mode_c > 9999

        inputsArray = [phase, inputInt]

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
            data[data[curr+1]] = inputsArray[inputCurr]
            inputCurr += 1
            assert inputCurr < 3
            curr += 2
        elif opcode == 4:
            output = A
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
    return output

phaseSettings = permutations([0,1,2,3,4])
res = 0
p = []
values = {}
for phase in phaseSettings:
    a = program(phase[0], 0)
    b = program(phase[1], a)
    c = program(phase[2], b)
    d = program(phase[3], c)
    e = program(phase[4], d)
    if e > res:
        res = e
        p = phase

print('Part 1 result: %d ' % res)
