from time import sleep
print(chr(27)+'[2j')
print('\033c')
f = open('15.test', 'r')
f = open('15.test2', 'r')
#f = open('15.test3', 'r')
f = open('15.input', 'r')
grid, steps = f.read().split('\n\n')
steps = ''.join([x.strip() for x in steps])

def fresh():
    print("\033[H\033[J", end="")  # Clear screen and move cursor

RED = "\033[31m"
BLUE = "\033[36m"
RESET = "\033[0m"
BG = "\033[101m"

D = [(0,-1), (1,0), (0,1), (-1,0)]
ds = '^>v<'

def parse(grid):
    g = {}
    w = 0
    h = 0
    p = (0,0)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            g[(x,y)] = c
            h = max(h, y+1)
            w = max(w, x+1)
            if c == '@':
                p = (x,y)
    return g,w,h,p

def print_map(g, w, h, s='@'):
    for y in range(h):
        line = ''
        for x in range(w):
            c = g[(x,y)]
            if c == '@':
                line += BG + s + RESET
            elif c in 'O[]':
                line += BLUE + c + RESET
            elif c == '#':
                line += RED + c + RESET
            else:
                line += g[(x,y)]
        print(line)

def get_score(g, w, h):
    s = 0
    for y in range(h):
        for x in range(w):
            if g[(x,y)] not in 'O[':
                continue
            s += y * 100 + x
    return s


def move(g, p, d):
    x,y = p 
    dx,dy = d
    swap: list[tuple[int,int]] = [p]
    nx,ny = x,y
    while True:
        nx,ny = nx+dx, ny+dy
        if g[(nx,ny)] == '#': 
            return g, p 
        elif g[(nx,ny)] == 'O':
            swap.append((nx,ny))
        elif g[(nx,ny)] == '.': 
            break
        else: 
            exit(1)
    swap.reverse()
    for s in swap:
        xs, ys = s
        nx,ny = xs+dx, ys+dy
        g[(nx,ny)] = g[(xs, ys)]
    g[(x,y)] = '.'
    np = x+dx, y+dy
    return g, np

def part1():
    g,w,h,p = parse(grid.split('\n'))
    for i, s in enumerate(steps): 
        #print(f'============== ROUND {s} ({i+1})')
        d = D[ds.index(s)]
        g, p = move(g, p, d)
        #print_map(g,w,h)

    print('FINISH ============')
    print_map(g,w,h, '@')

    score = get_score(g,w,h)
    return score

def widen(grid):
    lines = []
    for row in grid: 
        line = ''
        for col in row:
            if col == '#':
                line += '##'
            if col == 'O':
                line += '[]'
            if col == '.':
                line += '..'
            if col == '@':
                line += '@.'
        lines.append(line)
    return lines

def part2():
    wide_grid = widen(grid.split('\n'))
    g,w,h,p = parse(wide_grid)
    #print('Initial state: ')
    #print_map(g,w,h, '@')
    every = 1000
    for i, s in enumerate(steps): 
        if i % every == 0:
            fresh()
            print(f'.............. ROUND {s} ({i+1})')
        d = D[ds.index(s)]
        g, p = move2(g, p, d)
        if i % every == 0:
            print_map(g,w,h, s)
            sleep(0.3)

    print('FINISH ============')

    score = get_score(g,w,h)
    return score

def vertical(d):
    dx, _ = d
    return dx == 0

def move2(g, p, d):
    x,y = p 
    dx,dy = d
    swap: list[tuple[int,int]] = [p]
    pushes = [(x,y)]
    while True:
        can_move = 0
        while pushes:
            nx,ny = pushes.pop(0)
            x2,y2 = nx+dx, ny+dy
            c = g[(x2,y2)]
            if c == '#': 
                return g, p 
            elif c in 'O[]':
                if vertical(d) and c == '[':
                    pushes.append((x2+1,y2))
                    swap.append((x2+1,y2))
                if vertical(d) and c == ']':
                    pushes.append((x2-1,y2))
                    swap.append((x2-1,y2))
                pushes.append((x2,y2))
                swap.append((x2,y2))
            elif g[(nx,ny)] == '.': 
                can_move += 1

        if can_move == len(pushes):
            break
    # print('swap', swap)
    swap.reverse()
    to_add = []
    for s in swap:
        xs, ys = s
        nx,ny = xs+dx, ys+dy
        to_add.append((nx,ny,g[(xs, ys)]))
    for s in swap:
        xs, ys = s
        nx,ny = xs+dx, ys+dy
        g[(xs, ys)] = '.'
    for (x1,y1,c) in to_add:
        g[(x1,y1)] = c 

    np = x+dx, y+dy
    return g, np


score1= part1()
score2 = part2()
print(f'Solution part1: {score1}')
print(f'Solution part2: {score2}')
