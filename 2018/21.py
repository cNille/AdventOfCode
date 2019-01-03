# Import data
data = open('21.in', 'r').readlines()
data = [s.strip() for s in data]


def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]


def addi(reg, a, b, c):
    reg[c] = reg[a] + b


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]


def muli(reg, a, b, c):
    reg[c] = reg[a] * b


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]


def bani(reg, a, b, c):
    reg[c] = reg[a] & b


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]


def bori(reg, a, b, c):
    reg[c] = reg[a] | b


def setr(reg, a, b, c):
    reg[c] = reg[a]


def seti(reg, a, b, c):
    reg[c] = a


def gtir(reg, a, b, c):
    reg[c] = 1 if a > reg[b] else 0


def gtri(reg, a, b, c):
    reg[c] = 1 if reg[a] > b else 0


def gtrr(reg, a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0


def eqir(reg, a, b, c):
    reg[c] = 1 if a == reg[b] else 0


def eqri(reg, a, b, c):
    reg[c] = 1 if reg[a] == b else 0


def eqrr(reg, a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0


opcodes = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
]


# Part 1
def part1():
    start = 10
    reg = [start, 0, 0, 0, 0, 0]
    ip = int(data[0].split()[1])
    program = data[1:]
    count = 0
    while 0 <= reg[ip] < len(program):
        i = reg[ip]
        before = list(reg)
        instr, a, b, c = program[i].split()
        fn = [o for o in opcodes if o.__name__ == instr][0]
        fn(reg, int(a), int(b), int(c))

        reg[ip] += 1
        if instr == 'eqrr':
            # By understanding the code, only when start equals reg[3]
            # here, then it will halt.
            return reg[3]

        count += 1


res = part1()
print('Part 1 solution: %d' % res)


def part2():
    start = 10
    reg = [start, 0, 0, 0, 0, 0]
    ip = int(data[0].split()[1])
    program = data[1:]
    values = set()
    last = 0
    while 0 <= reg[ip] < len(program):
        i = reg[ip]
        before = list(reg)
        instr, a, b, c = program[i].split()
        fn = [o for o in opcodes if o.__name__ == instr][0]
        if i != 8:
            fn(reg, int(a), int(b), int(c))
        elif i == 8:
            reg[3] += (reg[2] & 255)
            reg[3] &= 16777215
            reg[3] *= 65899
            reg[3] &= 16777215

            if reg[2] < 256:
                l1 = len(values)
                values.add(reg[3])
                l2 = len(values)
                if l2 == l1:
                    return last

                last = reg[3]
                reg[4] = 0
                reg[1] = 5
            else:
                reg[4] = int(reg[2] / 256)
                reg[5] = 1
                reg[2] = reg[4]
                reg[1] = 7
        reg[ip] += 1


res = part2()
print('Part 2 Solution: %d' % res)
