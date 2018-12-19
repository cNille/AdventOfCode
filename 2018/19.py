# Import data
data = open('19.in','r').readlines()
data = [s.strip() for s in data]

def addr(reg, a, b, c): reg[c] = reg[a] + reg[b]
def addi(reg, a, b, c): reg[c] = reg[a] + b
def mulr(reg, a, b, c): reg[c] = reg[a] * reg[b]
def muli(reg, a, b, c): reg[c] = reg[a] * b
def banr(reg, a, b, c): reg[c] = reg[a] & reg[b]
def bari(reg, a, b, c): reg[c] = reg[a] & b
def borr(reg, a, b, c): reg[c] = reg[a] | reg[b]
def bori(reg, a, b, c): reg[c] = reg[a] | b
def setr(reg, a, b, c): reg[c] = reg[a]
def seti(reg, a, b, c): reg[c] = a
def gtir(reg, a, b, c): reg[c] = 1 if a > reg[b] else 0
def gtri(reg, a, b, c): reg[c] = 1 if reg[a] > b else 0
def gtrr(reg, a, b, c): reg[c] = 1 if reg[a] > reg[b] else 0
def eqir(reg, a, b, c): reg[c] = 1 if a == reg[b] else 0
def eqri(reg, a, b, c): reg[c] = 1 if reg[a] == b else 0
def eqrr(reg, a, b, c): reg[c] = 1 if reg[a] == reg[b] else 0
opcodes = [
    addr, addi, mulr, muli,
    banr, bari, borr, bori,
    setr, seti, gtir, gtri,
    gtrr, eqir, eqri, eqrr,
]

# Part 1
def part1():
    reg = [0,0,0,0,0,0]
    ip = int(data[0].split()[1])
    program = data[1:]
    count = 0
    r = []
    while 0 <= reg[ip] < len(program):
        i = reg[ip]
        before = list(reg)
        instr, a, b, c = program[i].split()
        fn = [o for o in opcodes if o.__name__ == instr][0]
        fn(reg, int(a), int(b), int(c))

        bstr = ','.join(map(str,before))
        rstr = ','.join(map(str,reg))
        #if reg[0] != before[0]:
        if True:
            r.append(reg[0])
            print('ip=%d\t%s\t%s\t%s' % (i, bstr, program[i], rstr))
            #if len(r) >= 2:
            #    print(r[-1] - r[-2])
            #print(r)
        reg[ip] += 1

        count +=1
        if count > 100:
            exit()
    print('Part 1 is done')
    print(reg)

# Part 2
def part2():
    reg = [1,0,0,0,0,0]
    ip = int(data[0].split()[1])
    program = data[1:]
    for _ in range(20):
        i = reg[ip]
        instr, A, B, C = program[i].split()
        fn = [o for o in opcodes if o.__name__ == instr][0]
        fn(reg, int(A), int(B), int(C))
        reg[ip] += 1

    nbr = reg[2]
    res = []
    for i in range(1,nbr+1):
        if i % 500000 == 0:
            print('Iteration: %d of %d' % (i, nbr))
        if nbr % i == 0:
            res.append(i)
    print('Part 2 result: %d' % sum(res))

#part1()
part2()
