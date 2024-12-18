import heapq
print(chr(27)+'[2j')
print('\033c')

f = open('18.input', 'r')
boundary = 70
size = (0,70)
to_corrupt = 1024

# f = open('18.test', 'r')
# boundary = 6
# size = (0,6)
# to_corrupt = 12

def print_map(g, visited):
    for y in range(boundary+1):
        line = ''
        for x in range(boundary+1):
            if (x,y) in visited:
                line += 'O'
            else:
                line += g[(x,y)]
        print(line)


lines = [x.strip() for x in f.readlines()]
B = []
for line in lines:
    x,y = line.split(',')
    x,y = int(x), int(y)
    B.append((x,y))

G = {}
for y in range(boundary+1):
    for x in range(boundary+1):
        G[(x,y)] = '.'


def path_find(g):
    D = [(0,-1), (1,0), (0,1), (-1,0)]
    djikstra = {}
    q = [(0, 0, 0, 0, set())]
    best = boundary*boundary
    best_visited = set()
    found = False
    heapq.heapify(q)
    i = 0
    while q:
        i += 1
        if i % 1000000 == 0:
            print(f'Iteration {i}')

        _, cost, x, y, steps = heapq.heappop(q)
        if (x,y) in djikstra and cost > djikstra[(x,y)]:
            continue
        if cost > best:
            continue
        djikstra[(x,y)] = cost
        if (x,y) == (boundary, boundary): 
            best = min(cost,best)
            best_visited = steps 
            #print(f"FOUND: {len(steps)}, new best: {best}")
            found = True
            continue 
    
        ns = steps.copy()
        ns.add((x,y))
        for d in D:
            dx,dy = d
            nx, ny = x+dx, y+dy
            if (nx,ny) in ns:
                continue
            c = cost+1
            if (nx,ny) in djikstra and c >= djikstra[(nx,ny)]:
                continue
            djikstra[(x,y)] = cost
    
            if (nx,ny) not in g or g[(nx,ny)] != '.':
                continue
            nh = cost + (boundary * boundary) - (nx*ny)
            heapq.heappush(q, (nh, cost+1, nx,ny, ns))

    #print_map(g, best_visited)
    return found, i, best


g = G.copy()
for i in range(to_corrupt):
    b = B[i]
    g[b] = '#'
_, _, best = path_find(g)
print(f'Solution part1: {best}')

last_corrupt = None
for to_corrupt in range(len(B), 0, -1):
    g = G.copy()
    for b in range(to_corrupt):
        g[B[b]] = '#'
    found, iterations, _ = path_find(g)
    if found:
        break
    else: 
        last_corrupt = B[to_corrupt-1]
print(f'Solution part2: {last_corrupt}')
