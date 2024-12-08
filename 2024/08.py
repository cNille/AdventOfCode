print(chr(27)+'[2j')
print('\033c')
f = open('08.test', 'r')
#f = open('08.test2', 'r')
#f = open('08.input', 'r')
lines = [x.strip() for x in f.readlines()]

nodes = {}
g = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        g[(x,y)] = c
        if c == '.':
            continue
        if c not in nodes:
            nodes[c] = []
        nodes[c].append((x,y))

loc1 = set()
loc2 = set()
for k in nodes:
    pos = nodes[k]

    for a in pos:
        for b in pos:
            if a == b:
                loc2.add(a)
                continue
            x1,y1 = a
            x2,y2 = b

            dx,dy = x1-x2, y1-y2 
            x = x1 + dx 
            y = y1 + dy 
            if (x,y) in g:
                loc1.add((x,y))
            while (x,y) in g:
                loc2.add((x,y))
                x = x + dx 
                y = y + dy 
            

def print_map(loc):
    for y, line in enumerate(lines):
        l = ''
        for x, c in enumerate(line):
            if c != '.':
                l += c
            elif (x,y) in loc:
                l += '#'
            else:
                l += c
        print(l)

print_map(loc1)
print('Solution part 1:', len(loc1))
print()
print_map(loc2)
print('Solution part 2:', len(loc2))
