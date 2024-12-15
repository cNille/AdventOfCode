print(chr(27)+'[2j')
print('\033c')
f = open('15.test', 'r')
f = open('15.test2', 'r')
f = open('15.input', 'r')
grid, steps = f.read().split('\n\n')
steps = ''.join([x.strip() for x in steps])

g = {}
w = 0
h = 0
p = (0,0)
for y, line in enumerate(grid.split('\n')):
    for x, c in enumerate(line):
        g[(x,y)] = c
        h = max(h, y+1)
        w = max(w, x+1)
        if c == '@':
            p = (x,y)

def print_map(g, w, h):
    for y in range(h):
        line = ''
        for x in range(w):
            line += g[(x,y)]
        print(line)

def move(g, p, d):
    print(f'Move: {p}')
    x,y = p 
    dx,dy = d
    swap: list[tuple[int,int]] = [p]
    nx,ny = x,y
    while True:
        print(f'--- {p} ({d})')
        nx,ny = nx+dx, ny+dy
        print(nx,ny)
        print('Map:', g[(nx,ny)])
        if g[(nx,ny)] == '#': 
            print('BREAK')
            # break function
            return g, p 
        elif g[(nx,ny)] == 'O':
            print('TOSWAP')
            swap.append((nx,ny))
        elif g[(nx,ny)] == '.': 
            print('CANSWAP')
            # Continue after function
            break
        else: 
            print('ERROR', g[(nx,ny)])

    swap.reverse()
    for s in swap:
        xs, ys = s
        nx,ny = xs+dx, ys+dy
        g[(nx,ny)] = g[(xs, ys)]

    g[(x,y)] = '.'
    p = x+dx, y+dy

    return g, p

print_map(g,w,h)
print(steps)
print(p)
D = [(0,-1), (1,0), (0,1), (-1,0)]
ds = '^>v<'

for i, s in enumerate(steps): 
    print(f'============== ROUND {s} ({i})')
    #print_map(g,w,h)
    d = D[ds.index(s)]
    print(s, d)
    g, p = move(g, p, d)


print('FINISH ============')
print_map(g,w,h)

def get_score(g, w, h):
    s = 0
    for y in range(h):
        for x in range(w):
            if g[(x,y)] != 'O':
                continue
            s += y * 100 + x
    return s

score = get_score(g,w,h)
print(f'Score is: {score}')
