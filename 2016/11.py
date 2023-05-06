from itertools import combinations
from collections import deque

print(chr(27)+'[2j')
print('\033c', end='')

f = open('11.test', 'r')
f = open('11.input', 'r')
lines = [x.strip() for x in f.readlines()]

e = 0
obj = {}
for i, line in enumerate(lines):
    line = line.split('contains ')[1]
    if line == 'nothing relevant.':
        continue
    parts = line.removesuffix('.').replace(' and ',', ').split(', ')
    
    
    for part in parts:
        part = part.removeprefix('a ')
        acronym = part.split(' ')[1][0] + '_' +   part.split(' ')[0][:3]
        obj[acronym] = i

# part 2
obj['g_ele'] = 0
obj['m_ele'] = 0
obj['g_dil'] = 0
obj['m_dil'] = 0
# part 2 ☝️

def get_combinations(s):
    l = s.split(',')
    if len(l) == 1:
        return [l]
    else:
        c1 = combinations(l, 1)
        c2 = combinations(l, 2)
        return list(c1) + list(c2)

def valid_floor(s):
    arr = s.split(',')
    microchips = [x for x in arr if x.startswith('m_')]
    generators = [x for x in arr if x.startswith('g_')]
    if len(generators) == 0:
        return True
    for m in microchips:
        gen = [g for g in generators if g.replace('g_', 'm_') == m]
        if len(gen) == 0:
            return False
    return True

def is_valid(obj):
    floors = {}
    for o in obj:
        if obj[o] not in floors:
            floors[obj[o]] = []
        floors[obj[o]].append(o)
    for f in floors:
        if valid_floor(",".join(floors[f])):
            continue
        return False
    return True

# create counter 
def has_won(obj):
    for o in obj:
        if obj[o] != 3:
            return False
    return True

visited = set()
def get_next(obj, e, moves):
    s = str(e) + ":"
    for o in obj:
        s += o + str(obj[o]) + ","
    if s in visited:
        return []
    visited.add(s)

    same_floor = ",".join([o for o in obj if obj[o] == e])
    states = get_combinations(same_floor)

    possible_states = []
    for state in states:
        # move up
        if e < 3:
            obj2 = {}
            for o in obj:
                if o in state:
                    obj2[o] = e + 1
                else:
                    obj2[o] = obj[o]
            if is_valid(obj2):
                possible_states.append((obj2, e+1, moves+1))

        # move down
        if e > 0:
            obj2 = {}
            for o in obj:
                if o in state:
                    obj2[o] = e - 1
                else:
                    obj2[o] = obj[o]
            if is_valid(obj2):
                possible_states.append((obj2, e-1, moves+1))


    return possible_states
            

q = deque([(obj, e, 0)])
c = 0
max_moves = 0
while len(q) > 0:
    c += 1
    if c % 10000 == 0:
        print(c, len(q), max_moves)
    nxt = q.popleft()
    obj, e, moves = nxt
    if has_won(obj):
        print("Solution found in {} moves".format(moves))
        exit()
    max_moves = max(max_moves, moves)
    #print(len(q), nxt)
    next_states = get_next(obj, e, moves)
    for n in next_states:
        q.append(n)
