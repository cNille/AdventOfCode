f = open('05.input', 'r')
content = [x.strip() for x in f.readlines()]

data = [int(x) for x in content[0].split(',')]
curr = 0
inputInt = 5
print(data)

while data[curr] != 99:
    opcode = data[curr] % 100
    mode_a = data[curr] % 1000
    mode_a = mode_a > 99
    mode_b = data[curr] % 10000
    mode_b = mode_b > 999
    mode_c = data[curr] % 100000
    mode_c = mode_c > 9999

    print(curr, "OPCODE: %d" % opcode, data[curr])

    A = data[curr+1] if mode_a else data[data[curr+1]]
    if opcode in [1,2,5,6,7,8]:
        B = data[curr+2] if mode_b else data[data[curr+2]]
        # print(data[curr+1], data[curr+2], data[curr+3])
        # print(mode_a, mode_b, mode_c)
        # print(A,B)
    
    if opcode == 1:
        data[data[curr+3]] = A + B
        curr += 4
    elif opcode == 2:
        data[data[curr+3]] = A * B
        curr += 4
    elif opcode == 3:
        data[data[curr+1]] = inputInt
        curr += 2
    elif opcode == 4:
        if A != 0:
            print("SHOULD BE FINAL OUTPUT: %d" % A)
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

