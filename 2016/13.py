import heapq
print(chr(27)+'[2j')
print('\033c', end='')

puzzle_input = 1352 # My input
goal = (31,39)
#puzzle_input = 10 # Test input
#goal = (7,4)

def fn1(x,y):
    return x*x + 3*x + 2*x*y + y + y*y + puzzle_input

def fn2(x,y):
    return bin(fn1(x,y)).count("1") % 2 == 0 and x >= 0 and y >= 0

part1 =None
q = [(0,1,1)]
visited = set()
visited_max_50_steps = set()

while True:
    steps, x, y = heapq.heappop(q)
    if (x,y) == goal:
        part1 = steps
        break
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny, ns = x+dx, y+dy, steps+1
        if fn2(nx,ny) and (nx,ny) not in visited:
            visited.add((nx,ny))
            heapq.heappush(q, (ns, nx, ny))
            if ns <= 50:
                visited_max_50_steps.add((nx,ny))

print("Solution to part 1: %d" % part1)
print("Solution to part 2: %d" % len(visited_max_50_steps))
