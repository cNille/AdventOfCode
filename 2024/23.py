print(chr(27)+'[2j')
print('\033c')
f = open('23.test', 'r')
f = open('23.input', 'r')

RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"
LIGHT_BLUE_BG = "\033[104m"

lines = [x.strip() for x in f.readlines()]


nodes = set()
conns = {}
for line in lines:
    a,b = line.split('-')
    if a not in conns:
        conns[a] = set()
    if b not in conns:
        conns[b] = set()
    conns[a].add(b) 
    conns[b].add(a) 
    nodes.add(a)
    nodes.add(b)


sets = set()
for n1 in nodes:
    middle = conns[n1]
    for n2 in middle:
        last = conns[n2]
        for n3 in last:
            cmps = tuple(sorted([n1,n2,n3]))
            if n1 not in conns[n3]:
                continue
            sets.add(cmps)

found = 0
for s in sorted(list(sets)):
    has_t = -1
    out = []
    for i,n in enumerate(s):
        if n.startswith('t'):
            has_t = i
            out.append(f'{LIGHT_BLUE_BG}{n}{RESET}')
        else: 
            out.append(f'{n}')

    if has_t >= 0:
        found += 1
print('Solution part1:', found)


# Part 2 ======================

sets = set()
max_size = 0
biggest = []
for line in lines:
    n1,n2 = line.split('-')
    lan = set([n1,n2])
    can_add = True
    while can_add:
        can_add = False
        for n in nodes:
            c1 = conns[n]
            intersect = lan.intersection(c1)
            if len(intersect) == len(lan):
                lan.add(n)
                can_add = True 
                break

    if len(lan) > max_size:
        max_size = len(lan)
        biggest = lan
print('--')
print(f'Size: {max_size}, {biggest}')

lan = sorted(biggest)
print('Solution part2:', ','.join(lan))

