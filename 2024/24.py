from time import sleep
print(chr(27)+'[2j')
print('\033c')
f = open('24.test', 'r')
f = open('24.test2', 'r')
f = open('24.test3', 'r')
f = open('24.input', 'r')

RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"
LIGHT_BLUE_BG = "\033[104m"

reg, aoeu = f.read().split('\n\n')
instructions: list[str] = aoeu.strip().split('\n')

R = {}
for CAR in reg.split('\n'):
    CAR, val = CAR.split(': ')
    val = int(val)
    R[CAR] = val

def swap(instr_to_swap_in, a, b):
    instr = []
    for i in instr_to_swap_in:
        left, right = i.split(' -> ')
        if a in right:
            right = b
        elif b in right:
            right = a
        instr.append(' -> '.join([left,right]))
    return instr

instr = instructions.copy()
instr = swap(instr, 'z05', 'tst')
instr = swap(instr, 'z11', 'sps')
instr = swap(instr, 'z23', 'frt')
instr = swap(instr, 'cgh', 'pmd')


response = [
 'z05', 'tst',
 'z11', 'sps',
 'z23', 'frt',
 'cgh', 'pmd',
 ]
response.sort()
print(','.join(response))
exit()


# for i in instr:
#     print(i)
# exit()
#instr = swap(instr, 'pvd', 'jkm')

conns = {}
fwd = {}
uniq =  set()

ops = set() 
for x in instr:
    x = x.strip()
    inputs, out = x.split('->')
    out = out.strip()
    a, op, b = [x.strip() for x in inputs.split()]
    if out not in conns:
        conns[out] = []
    conns[out].append(a)
    conns[out].append(b)
    ops.add((min(a,b), max(a,b), op, out))
    uniq.add(out)
    if 'x' not in a and 'y' not in a:
        uniq.add(a)
    if 'x' not in b and 'y' not in b:
        uniq.add(b)

seen = set()
for i in range(45):
    z = f'z0{i}' if i < 10 else f'z{i}'
    xs = []
    ys = []
    nxts = [z]
    while len(nxts) > 0:
        nxt = nxts.pop(0)
        if 'x' in nxt and nxt not in xs:
            xs.append(nxt)
        if 'y' in nxt and nxt not in ys:
            ys.append(nxt)
        if nxt not in conns:
            continue
        before = conns[nxt]
        for b in before:
            nxts.append(b)
    #print(z)
    #print('---', xs)
    #print('---', ys)
    x1 = sorted(xs)
    x1.reverse()
    assert(''.join(x1) == ''.join(xs))
    y1 = sorted(ys)
    y1.reverse()
    assert(''.join(y1) == ''.join(ys))
    assert(xs[0][1:] == z[1:])
    assert(ys[0][1:] == z[1:])
    for x in xs: 
        seen.add(x)
    for y in ys:
        seen.add(y)

def run(R, instructions):
    queue = [x.strip() for x in instructions]
    while len(queue) > 0:
        nxt_queue = []
        is_rec = True
        for i in range(len(queue)):
            nxt = queue.pop(0)
            inputs, out = nxt.split('->')
            out = out.strip()
            a, op, b = [x.strip() for x in inputs.split()]
            if a not in R or b not in R:
                nxt_queue.append(nxt)
                continue
            is_rec = False
            if 'AND' == op:
                if R[a] == 1 and R[b] == 1:
                    R[out] = 1
                else:
                    R[out] = 0
            elif 'XOR' == op:
                if (R[a] + R[b])== 1:
                    R[out] = 1
                else:
                    R[out] = 0
            elif 'OR' == op:
                if (R[a] + R[b]) > 0:
                    R[out] = 1
                else:
                    R[out] = 0
        queue = nxt_queue
        if is_rec:
            return -1
    
    i = 0
    res = 0
    while True:
        z = f'z0{i}' if i < 10 else f'z{i}'
        if z not in R:
            break
    
        if R[z] == 1:
            res += 2 ** i
        i += 1
    return res

#clean_r = R.copy()
#run(clean_r, instructions)

Z_size = 6
Z_size = 45
def set_values(R, x_value, y_value):
    for i in range(Z_size):
        p = (2 << (i)) // 2
        x = f'x0{i}' if i < 10 else f'x{i}'
        y = f'y0{i}' if i < 10 else f'y{i}'
        R[x] = 1 if x_value == p  else 0
        R[y] = 1 if y_value == p  else 0
    return R

def test_run(R, instr):
    correct = 0
    for bit in range(Z_size):
        r = set_values(R.copy(), 2**bit, 2**bit)
        val = run(r, instr)
        should_be = 2 ** (bit+1)
        correct += 1 if val == should_be else 0
    return correct

for p in range(0, 45): 
    x = 2 << p 
    y = 2 << p 
    CAR = set_values(R.copy(), x,y)
    val = run(CAR, instructions)
    print(p, f'{x}+{y} = {val}', bin(val))

def search(term,op):
    res = ''
    for (a1,b1,op1, out) in ops:
        if op1 != op:
            continue
        if term == a1 or term == b1:
            res = out
    return res

def get(a,b,op):
    a0 = min(a,b)
    b0 = max(a,b)
    for (a1,b1,op1, out) in ops:
        if a0 == a1 and b0 == b1 and op == op1:
            return out
    return ''

CAR = 'ktr'
for i in range(2,45):
    z = f'z0{i}' if i < 10 else f'z{i}'
    x = f'x0{i}' if i < 10 else f'x{i}'
    y = f'y0{i}' if i < 10 else f'y{i}'
    AND = get(x,y,'AND')
    assert(AND != '')
    XOR = get(x,y,'XOR')
    assert(XOR != '')
    w = get(XOR, CAR, 'AND') 
    if w == '':
        print('------ ERR, look forward')
        if search(XOR, 'AND') == '':
            print(f'XOR "{XOR}" is incorrect.')
        if search(CAR, 'AND') == '':
            print(f'CAR "{CAR}" is incorrect.')
    assert(w != '')
    CAR = get(w, AND, 'OR')
    if CAR == '':
        print('------ ERR, look forward')
        if search(w, 'OR') == '':
            print(f'AND "{w}" is incorrect.')
        if search(AND, 'OR') == '':
            print(f'AND "{AND}" is incorrect.')

    assert(CAR != '')
    print(f'{i} == And: {AND}, XOR: {XOR}, w: {w}, r: {CAR}')


exit()


# ===================================================
# ===================================================
# ===================================================
# ===================================================


start = test_run(R, instructions)
print(start)
print(clean_r)
sus = []
for c in uniq:
    r0 = R.copy()
    if c in clean_r:
        r0[c] = 1 - clean_r[c]
    pre = test_run(r0, instructions)
    d = start - pre
    if d < 2:
        sus.append(c)
    print(f'Diff: {d}, start: {start}, after: {pre}')
#sus = ['z40', 'z19', 'ssd', 'vsr', 'z23', 'z09', 'z12', 'mkq', 'z24', 'z41', 'pgn', 'dws', 'whw', 'jth', 'nfd', 'vcb', 'nkv', 'pvb', 'z08', 'qcb', 'wtf', 'z36', 'sdc', 'pmd', 'z29', 'chk', 'wrs', 'kmg', 'z11', 'csc', 'z02', 'hhc', 'cwm', 'z10', 'wpn', 'ppk', 'qdm', 'wmk', 'kqd', 'vdr', 'z44', 'pjg', 'z14', 'jkk', 'dcr', 'tst', 'crq', 'z18', 'ngh', 'z27', 'dvg', 'z21', 'hfh', 'z01', 'fqr', 'jfh', 'z26', 'bmt', 'z42', 'gdq', 'z35', 'csp', 'mhg', 'kjs', 'jpf', 'rrr', 'kmw', 'rhf', 'knv', 'z37', 'jkm', 'z13', 'bbh', 'cnh', 'khg', 'pvd', 'wbk'] 

print(sus)
from itertools import combinations
count = 0 
pairs = []
for (a,b) in combinations(sus,2):
    print(clean_r[a], clean_r[b])

    if clean_r[a] == clean_r[b]:
        continue
    pairs.append((a,b))
print('pairs', len(pairs))
for c in combinations(pairs,4):
    count += 1
print(count)
exit()


exit()

    
good = set()
to_flip = set()
sus_bit = {}
sus_all = set()
uniq = set()
#for bit in range(Z_size):
for x in range(100):
    for y in range(100):
        sus = set() 
        CAR = set_values(R.copy(), x,y)
        val = run(CAR, instructions)
        should_be = x + y 
        correct = val == should_be
        bit = 0
        t = max(x,y)
        while t >= 2:
            t = t // 2
            bit += 1
        print(f'({x},{y}) => {val} ({should_be}), {correct}')


        z = f'z0{bit}' if bit < 10 else f'z{bit}'
        q = [z]
        if correct:
            good.add(z)
            while len(q) > 0:
                o = q.pop(0)
                if o not in conns:
                    continue
                for c in conns[o]:
                    if c not in sus:
                        q.append(c)
                    good.add(c)
            continue
        else:
            sus.add(z)

        print(f'{bit} => {val} ({should_be}), {correct}')
        print(good)
        print(sus)

        exit()

#    while len(q) > 0:
#        o = q.pop(0)
#        if o not in conns:
#            continue
#        for c in conns[o]:
#            if c not in sus:
#                q.append(c)
#            if correct:
#                good.add(c)
#            elif c not in good:
#                if 'y' not in c and 'x' not in c:
#                    sus.add(c)
#    
#    if len(sus) > 0:
#        sus_bit[bit] = sus
#        sus_all.update(sus)
#    uniq.update([
#        s 
#        for s in sus
#        if 'x' not in s and 'y' not in s
#    ])
#    uniq.update([
#        g 
#        for g in good
#        if 'x' not in g and 'y' not in g
#    ])
print(len(good))
print(len(sus_bit))
print(sus_bit)
print(sus_all)



def fix_bit(bit, sus, instructions):
    count = 0
    for a in sus:
        for a1 in sus_all:
            count += 1
            instr = instructions.copy()
            instr = swap(instr, a, a1)
            r = set_values(R.copy(), 2**bit, 2**bit)
            correct = test_run(r, instr)
            if correct > start:
                return (a,a1)  
    #for a in sus:
    #    for b in sus:
    #        for a1 in sus_all:
    #            for b1 in sus_all:
    #                if a1 == b1:
    #                    continue
    #                print(a,a1,b,b1)
    #                instr = instructions.copy()
    #                instr = swap(instr, a, a1)
    #                instr = swap(instr, b, b1)
    #                r = set_values(R.copy(), bit)
    #                val = run(r, instr)
    #                should_be = 2 ** (bit+1)
    #                if val == should_be:
    #                    return (a,a1, b,b1)  
    return None
                        

count = 0


fixed_instr = instructions.copy()
fixed_instr = swap(fixed_instr, 'z05', 'tst')
start = test_run(R, instructions)
for bit in sus_bit:
    sus = sus_bit[bit]
    print('-'*20)
    print(bit, sus)
    fix = fix_bit(bit,sus, fixed_instr)
    if fix is not None:
        print(RED, 'Fix:', fix, RESET)
    else:
        print('No fix')
print(count)



