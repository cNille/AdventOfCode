from intcode import *
from itertools import permutations
content = open('15.input', 'r').readline().strip()

def printview(view):
    xs = [x for x,y in view]
    if len(xs) > 0:
        xmin, xmax = min(xs), max(xs)
    else: 
        xmin, xmax = 0,0 
    ys = [y for x,y in view]
    if len(ys) > 0:
        ymin, ymax = min(ys), max(ys)
    else: 
        ymin, ymax = 0,0 

    xmin = -10 if xmin > -10 else xmin - 2
    xmax = 10 if xmax < 10 else xmax + 20
    ymin = -10 if ymin > -10 else ymin - 2
    ymax = 10 if ymax < 10 else ymax + 2

    for y in range(ymin, ymax):
        row = ""
        for x in range(xmin, xmax):
            if (x,y) not in view:
                row += " "
            else:
                row += view[(x,y)]
        print row

# Part 1 
input_code = content
stream = Streams(["A"])
intcode = IntCode(input_code)
program = Program(intcode, name="A", stream=stream)

# north (1), south (2), west (3), and east (4)
directions = [1,3,2,4]
delta = { 1: (0,-1), 2: (0,1), 3: (1,0), 4: (-1,0) }

current_direction = 0
x,y = 0,0
view = {}
verbose = False
while True:

    stream.add("A", directions[current_direction])
    for output in program.run():
        # 0 - wall
        # 1 - moved
        # 2 - moved, found X

        if output == 0:
            dx, dy = delta[directions[current_direction]]
            view[(x+dx, y+dy)] = '#'
            current_direction = (current_direction + 1) % 4 
            
        if output == 1:
            dx, dy = delta[directions[current_direction]]
            x,y = x+dx, y+dy
            view[(x, y)] = '.'
            current_direction = (current_direction - 1) % 4 

        if output == 2:
            dx, dy = delta[directions[current_direction]]
            x,y = x+dx, y+dy
            view[(x,y)] = '@'
            current_direction = (current_direction - 1) % 4 
            oxygen = (x,y)

    if x == 0 and y == 0 and current_direction == 0:
        break
            
    if verbose:
        printview(view)


from collections import deque
queue = deque()
queue.append((0, 0, 1))


visited = []

min_steps = 9999
while len(queue) != 0:
    
    x,y, s = queue.popleft()
    if (x,y) in visited:
        continue
    visited.append((x,y))


    neighbours = [ (x+dx, y+dy) for dx,dy in delta.values()]
    
    for n in neighbours:
        if view[n] == '@':
            min_steps = min_steps if s > min_steps else s
        if view[n] == '.':
            queue.appendleft((n[0],n[1], s+1))

print "Part 1: %d " % min_steps

# Part 2
x,y = oxygen
visited = []
queue.append((x,y, 1))
max_steps = 0
while len(queue) != 0:
    x,y, s = queue.popleft()
    if (x,y) in visited:
        continue
    visited.append((x,y))
    neighbours = [ (x+dx, y+dy) for dx,dy in delta.values()]
    
    for n in neighbours:
        if view[n] != '#' and view:
            view[n] = '#'
            queue.appendleft((n[0],n[1], s+1))
            max_steps = max_steps if max_steps > s else s

print "Part 2: %d " % max_steps

