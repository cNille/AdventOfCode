import sys
from collections import defaultdict
from time import sleep

# Import data
data = [l.strip() for l in open('16.in', 'r').readlines()]

clay = {}

y_max = 0
y_min = 0
y_minst = 100
x_max = 0
x_min = 0
for d in data:
    values = d.split(', ')
    for v in values:
        if v.startswith('x'):
            if '..' in v:
                r1, r2 = map(int, v[2:].split('..'))
                x = range(r1,r2+1)
            else:
                x = [int(v[2:])]
        if v.startswith('y'):
            if '..' in v:
                r1, r2 = map(int, v[2:].split('..'))
                y = range(r1,r2+1)
            else:
                y = [int(v[2:])]
            y_max = max([y_max] + list(y))
            y_minst = min([y_minst] + list(y))
            x_max = max([x_max] + list(x))
            x_min = min([x_min] + list(x))
    for i in x:
        for j in y:
            clay[(i,j)] = True
grid = []
flowing = [(500,1)]
flowed = set()
infinite = set()
for i in range(y_min-1, y_max+2):
    grid.append([])
    for j in range(x_min-1, x_max+2):
        grid[i].append('.')
for (x,y) in clay:
    grid[y][x-x_min] = '#'
grid[0][500] = '+'

def print_grid(pos=(500,0)):
    global grid, count
    x_delta = 30
    y_delta = 30
    y_min = max(0, pos[1]-x_delta)
    y_max = min(len(grid), pos[1]+x_delta)
    x_min = max(0, pos[0]-y_delta)
    x_max = min(len(grid[0]), pos[0]+y_delta)
    print('Count: %d' % count)
    for i, row in enumerate(grid[y_min:y_max]):
        new_r = [r for r in row]
        if i+y_min == pos[1]:
            new_r[pos[0]] = 'x'
        print(str(i+y_min) + '\t' + ''.join(new_r[x_min:x_max]))
    print('')
    print('')

def g((x,y)):
    global grid
    gy = y-y_min
    gx = x-x_min
    if len(grid) -1 <= gy or len(grid[0]) -1 <= gx:
        return '@' # Errormsg...
    return grid[gy][gx]

def update((x,y), ch):
    global grid
    grid[y][x] = ch

def below((x,y)): return (x, y+1)
def left((x,y)): return (x-1, y)
def right((x,y)): return (x+1, y)

def has_infinite_bound((x,y)):
    L = left((x,y))
    left_bound = False
    while L[0] >= x_min+2:
        if g(below(L)) == '.':
            break
        if g(L) == '#':
            break
        if g(L) == '.':
            break
        if L in infinite:
            left_bound = True
            break
        L = left(L)
    if left_bound:
        return True
    R = right((x,y))
    right_bound = False
    while R[0] < x_max+2:
        if g(below(R)) == '.':
            break
        if g(R) == '#' :
            break
        if g(R) == '.' :
            break
        if R in infinite:
            right_bound = True
            break
        R = right(R)
    if right_bound:
        return True
    return False
def isBound((x,y)):
    L = left((x,y))
    left_bound = False
    while L[0] >= x_min+2:
        if g(below(L)) == '.':
            break
        if g(L) == '#' :
            left_bound = True
            break
        L = left(L)
    if not left_bound:
        return False
    R = right((x,y))
    right_bound = False
    while R[0] < x_max+2:
        if g(below(R)) == '.':
            break
        if g(R) == '#' :
            right_bound = True
            break
        R = right(R)
    if not right_bound:
        return False
    return True
def withingrid((x,y)):
    within_x = x_min <= x <= x_max+1
    within_y = y_min <= y <= y_max
    return within_x and within_y

def pop(pos):
    global flowing, flowed
    flowing = [f for f in flowing if f != pos]
    flowed.add(pos)
def push(pos):
    global flowing, flowed
    if pos not in flowed and withingrid(pos):
        flowing.append(pos)
        flowed.add(pos)
        return True
    else:
        return False


count = 0
verbose_start = 24965
verbose = True
verbose = False
while len(flowing) > 0:

    pos = flowing[-1]
    x, y = pos
    B = below(pos)
    L = left(pos)
    R = right(pos)

    if g(pos) == '#':
        pop(pos)
    elif B in infinite:
        pop(pos)
        infinite.add(pos)
    elif g(B) == '.':
        success = push(B)
        if not success:
            pop(pos)
            infinite.add(pos)
        update(pos, '|')
    elif g(pos) in ['.', '|']:
        if g(B) == '|' and has_infinite_bound(B):
            update(pos, '|')
            pop(pos)
            infinite.add(pos)
        elif isBound(pos):
            update(pos, '~')
            pop(pos)
            push(L)
            push(R)
        else:
            update(pos, '|')
            pop(pos)
            push(L)
            push(R)



    count += 1
    if verbose and verbose_start <= count:
        print('pos', pos)
        print('Dir', B, L, R)
        print(infinite)
        print(flowing[-10:])
        print_grid(pos)
        sleep(0.5)
    else:
        if count % 5000 == 0:
            print_grid(pos)

water_count = 0
for row in grid[y_minst:]:
    for c in row:
        if c == '~' or c == '|':
            water_count +=1
print('Part 1:', water_count)

for y in range(1,len(grid)):
    if y % 100 == 0:
        print(y)
    for x in range(1,len(grid[0])-1):
        if withingrid((x,y)) and g((x,y)) == '|':

            L = left((x,y))
            while withingrid(L):
                if g(L) == '#' or g(L) == '.':
                    break
                if g(L) == '~':
                    update((x,y), '~')
                    break
                L = left(L)

            R = right((x,y))
            while withingrid(R) :
                if (g(R) != '#' or g(R) != '.'):
                    break
                if g(R) == '~':
                    update((x,y), '~')
                    break
                R = right(R)

water_count = 0
for row in grid:
    for c in row:
        if c == '~':
            water_count +=1
print('Part 2:', water_count)


