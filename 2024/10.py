print(chr(27)+'[2j')
print('\033c')
#f = open('10.test', 'r')
#f = open('10.test2', 'r')
#f = open('10.test3', 'r')
#f = open('10.test4', 'r')
#f = open('10.test5', 'r')
#f = open('10.test6', 'r')
#f = open('10.test7', 'r')
#f = open('10.test8', 'r')
f = open('10.test5', 'r')
#f = open('10.input', 'r')
lines = [x.strip() for x in f.readlines()]

g = {}
trailheads = []
trailends = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        g[(x,y)] = c
        if c == '0':
            trailheads.append((x,y))
        if c == '9':
            trailends.append((x,y))

D = [(0,1), (0,-1), (1,0), (-1,0)]
def hike(g, pos, path):
    x,y = pos
    ends = set()
    new_path = [p for p in path]
    new_path.append(pos)
    paths = []
    for dx,dy in D:
        x1 = x + dx
        y1 = y + dy
        if (x1, y1) in new_path: 
            continue
        if (x1,y1) not in g:
            continue
        if g[(x1,y1)] == '.':
            continue

        v  = int(g[(x,y)])
        v1 = int(g[(x1,y1)])
        if (v1-v) != 1:
            continue

        if v1 == 9:
            paths.append(new_path) 
            ends.add((x1,y1))
            continue
        
        new_ends, p = hike(g, (x1,y1), new_path)
        paths.extend(p)
        ends.update(new_ends)
    return ends, paths

total_score = 0
total_rating = 0
for head in trailheads:
    ends, paths = hike(g, head, set()) 
    score = len(ends)
    total_score += score
    rate = len(paths)
    total_rating += rate

print('Solution part1:',total_score)
print('Solution part2:', total_rating)
