import ast

# Import data
data = open('day_16_input.txt','r').readlines()
data = [s.strip() for s in data]

def equal_reg(reg1, reg2):
    for i in range(4):
        if reg1[i] != reg2[i]:
            return False
    return True

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
    addr,
    addi,
    mulr,
    muli,
    banr,
    bari,
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
fun = {}
for i in range(16):
    fun[i] = [o.__name__ for o in opcodes]

def test(before, instr, after):
    global fun
    success = 0
    for op in opcodes:
        reg = [b for b in before]
        op(reg, instr[1], instr[2], instr[3])
        if equal_reg(after, reg):
            success +=1
        else:
            if op.__name__ in fun[instr[0]]:
                fun[instr[0]].remove(op.__name__)
    return success

part1 = data[:3236]
program = data[3238:]

before = after = instr = []
count = 0
for line in part1:
    if line.startswith('Before: '):
        before = ast.literal_eval(line[8:])
    elif line.startswith('After: '):
        after = ast.literal_eval(line[8:])
    elif line == '':
        successes = test(before, instr, after)
        if successes >= 3:
            count += 1
    else:
        instr = []
        for i in line.strip().split():
             instr.append(int(i))

print('Part 1 result: %d' % count)

# Part 2
fixed = {}
def nop(): print('panic!')
for i in range(16):
    fixed[i] = nop.__name__

done = 0
while done < 16:
    to_rm = []
    for f in fun:
        if len(fun[f]) == 1:
            done +=1
            fixed[f] = fun[f][0]
            to_rm.append(fun[f][0])

    for r in to_rm:
        for f in fun:
            if r in fun[f]:
                fun[f].remove(r)

reg = [0,0,0,0]
for line in program:
    l = [int(i) for i in line.split()]
    for op in opcodes:
        if op.__name__ == fixed[l[0]]:
            op(reg, l[1],l[2], l[3])
print('Part 2 result: %d ' % reg[0])
