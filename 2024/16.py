from heapq import heapify, heappop, heappush
print(chr(27)+'[2j')
print('\033c')
f = open('16.test', 'r')
#f = open('16.input', 'r')
lines = [x.strip() for x in f.readlines()]

def print_map(g,p):
    for y, row in enumerate(lines):
        line = ''
        for x, _ in enumerate(row):
            if (x,y) in p:
                line += 'O'
            else: 
                line += g[(x,y)]
                
        print(line)

g = {}
pos = (0,0)
end = (0,0)
for y, line in enumerate(lines):
    for x,c in enumerate(line):
        if c == 'S':
            pos = (x,y)
            g[(x,y)] = '.'
        elif c == 'E':
            end = (x,y)
            g[(x,y)] = '.' 
        else:
            g[(x,y)] = c
x,y = pos
x2, y2 = end

D = [(0,-1), (1,0), (0,1), (-1,0)]
ds = '^>v<'
d = 1

# h = abs(x2-x) + abs(y2-y) + 0
h = 0
queue = [(h,0, x,y,d, set())]
heapify(queue)
i = 0
best_score = 999999999
best_paths = set()
djikstra = {}
seats = {}

while len(queue) != 0:
    i += 1
    h,s,x,y,d,p = heappop(queue)
    if i % 100000 == 0:
        print(f'Round {i}, score {s}. ({x},{y})', len(queue))
    if (x,y,d) in p:
        continue
    np = p.copy()
    np.add((x,y,d))

    if (x,y,d) not in djikstra or s < djikstra[(x,y,d)]:
        djikstra[(x,y,d)] = s 
    elif s > djikstra[(x,y,d)]:
        continue

    if best_score < s:
        continue
    if (x,y) == end:
        best_score = min(best_score, s)
        best_paths.update(np)
        seats = set([(x,y) for x,y,_ in best_paths])
        print(f'FOUND: {s}, Seats: {len(seats)}')
        continue

    h = abs(x2-x) + abs(y2-y) + s
    left = (d+1) % 4
    heappush(queue, (h,s+1000, x,y, left, np))
    right = (d-1) % 4
    heappush(queue, (h,s+1000, x,y, right,np))
    dx,dy = D[d]
    x1,y1 = x+dx,y+dy
    if g[(x1,y1)] == '#':
        continue
    heappush(queue, (h,s+1, x1,y1, d, np))

print_map(g, seats)
