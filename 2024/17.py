from time import sleep, time
print(chr(27)+'[2j')
print('\033c')
#f = open('17.test', 'r')
#facit = '4,6,3,5,6,3,5,2,1,0'

# f = open('17.test2', 'r')
# facit = 'B == 1'
# 
# f = open('17.test3', 'r')
# facit = 'output: 0,1,2'
# 
# f = open('17.test4', 'r')
# facit = 'A == 0, output: 4,2,5,6,7,7,7,7,3,1,0'
# 
# f = open('17.test5', 'r')
# facit = 'B == 26'
# 
# f = open('17.test6', 'r')
# facit = 'B == 44354'
 
#f = open('17.test7', 'r')
#facit = 'Init A == 117440, out: 0,3,5,4,3,0'

f = open('17.input', 'r')
facit = 'output: ????'

lines = [x.strip() for x in f.readlines()]

R = {}
P = []
for line in lines:
    if line.startswith('Register'):
        r, v = line.split(': ')
        r = r.split(' ')[1]
        v = int(v)
        R[r] = v
    if line.startswith('Program'):
        _, p = line.split(': ')
        P = [int(x) for x in p.split(',')]

def combo(P, p, R):
    v = P[p]
    assert(v < 7)
    if 0 <= v and v <= 3:
        return v
    elif v == 4:
        return R['A']
    elif v == 5:
        return R['B']
    elif v == 6:
        return R['C']
    return 0 


def run(R,P):
    p = 0
    i = 0
    out = []
    #visited = set()
    #print('RRR ===', R)


    while True:
        i += 1
        #print('-------------------')
        #print(f'Round {i}: {p} {out}', R)
        if p >= len(P):
            #print('HALT')
            break
        #v = (R['A'], R['B'], R['C'], p)
        #assert(v not in visited)
        #visited.add(v)
        
        opcode = P[p]

        if opcode == 0: # adv, division
            #print('adv')
            num = R['A']
            v = combo(P, p+1, R)
            den = pow(2, v)
            R['A'] = num // den
            #print(num, den, '===', R['A'])
        elif opcode == 1: # bxl, bitwise XOR
            #print('bxl, bitwise XOR')
            R['B'] = R['B'] ^ P[p+1]
        elif opcode == 2: 
            #print('bst save to B')
            R['B'] = combo(P, p+1, R) % 8 
        elif opcode == 3: 
            #print('jnz , nothing if A == 0')
            if R['A'] != 0:
                #print('jump to', P[p+1])
                p = P[p+1]
                continue
        elif opcode == 4: 
            #print('bcx, bitwise XOR on B and C')
            R['B'] = R['B'] ^ R['C'] 
        elif opcode == 5: 
            o = combo(P, p+1, R) % 8
            #print('out, outputs value:', o)
            out.append(o)
        elif opcode == 6: 
            #print('bdv, adv but stored in B')
            num = R['A']
            den = pow(2, combo(P, p+1, R))
            R['B'] = num // den
        elif opcode == 7: 
            #print('cdv, adv but stored in C')
            num = R['A']
            den = pow(2, combo(P, p+1, R))
            R['C'] = num // den


        # Done
        p += 2
    return out, R

#print('Part 1:')
#out, _ = run(R,P)
#print('Print    :', ','.join([str(o) for o in out]))

def fresh():
    print("\033[H\033[J", end="")  # Clear screen and move cursor

# bst. B = A % 8
# bxl. B = B ^ 3
# cdv. C = A // 2^B
# bxc. B = B ^ C
# bxl. B = B ^ 3
# adv. A = A // 2^3
# out. B % 8
# jnz. 0 if A != 0

def upphojt(X: int) -> int:
    return pow(2, X)

def run_min(A,B,C):
    out = []
    while A != 0:
        B = A % 8
        B = B ^ 3
        C = A // upphojt(B) 
        B = B ^ C
        B = B^3 
        A = A // 8 
        out.append(B % 8)
    return out, R 

# Found by binary search, manually
x = 108107572260000 
a = 0
start = time()
while True:
    a += 1
    x += 1
    out, r = run_min(x, 0, 0)
    if a % 1000000 == 0:
        fresh()
        print(f'{x}: ', len(out), out)
        print(f'#XXXXXXxXXXXXXX: ', 'XX', P)
        print(r)
        ellapsed = time() - start
        print(f'Time: {ellapsed}, per round: {ellapsed/1000000}')
        start = time()
    if out == P:
        print(f'SAME AT {x}')
        print(out, P)
        break



