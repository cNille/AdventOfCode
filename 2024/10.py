print(chr(27)+'[2j')
print('\033c')
f = open('10.test', 'r')
f = open('10.test2', 'r')
f = open('10.test3', 'r')
f = open('10.test4', 'r')
f = open('10.test5', 'r')
f = open('10.input', 'r')
lines = [x.strip() for x in f.readlines()]

g = {}
trailheads = []
trailends = []
for y, line in enumerate(lines):
    print(line)
    for x, c in enumerate(line):
        g[(x,y)] = c
        if c == '0':
            trailheads.append((x,y))
        if c == '9':
            trailends.append((x,y))
print(g)
print(trailheads)
print(trailends)

D = [(0,1), (0,-1), (1,0), (-1,0)]
def hike(g, pos, visited):
    x,y = pos
    ends = set()
    new_visited = set()
    new_visited.update(visited)
    new_visited.add(pos)
    for dx,dy in D:
        x1 = x + dx
        y1 = y + dy
        if (x1, y1) in visited: 
            continue
        if (x1,y1) not in g:
            continue
        if g[(x1,y1)] == '.':
            continue

        v1 = int(g[(x1,y1)])
        v =  int(g[(x,y)])
        if (v1-v) != 1:
            continue

        if v1 == 9:
            ends.add((x1,y1))
            continue
        
        ends.update(hike(g, (x1,y1), new_visited))
    return ends

total_score = 0
for head in trailheads:
    ends = hike(g, head, set()) 
    score = len(ends)
    print('HEAD',head, '->', score)
    total_score += score

print('Total score:',total_score)
