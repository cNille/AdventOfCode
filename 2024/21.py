from functools import cache
print(chr(27)+'[2j')
print('\033c')
f = open('21.test', 'r')
f = open('21.input', 'r')
RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"
LIGHT_BLUE_BG = "\033[104m"

lines = [x.strip() for x in f.readlines()]

mode1 = 1
keypad1 = 1
kp1 = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [None,'0','A'],
]
start1 = (2,3)
g1 = {}
for y, row in enumerate(kp1):
    for x, col in enumerate(row):
        if col != None:
            g1[col] = (x,y) 
keypad2 = 2
mode2 = 2
kp2 = [
    [None,'^','A'],
    ['<','v','>'],
]
g2 = {}
for y, row in enumerate(kp2):
    for x, col in enumerate(row):
        if col != None:
            g2[col] = (x,y) 
start2 = (2,0)

@cache
def get(mode, x,y):
    keypad = kp1 if mode == 1 else kp2
    if 0 > y or y >= len(keypad):
        return None
    if 0 > x or x >= len(keypad[y]):
        return None
    return keypad[y][x]

D = [(0, -1), (1,0), (0, 1), (-1,0)]
M = {
    (0, -1): '^',
    (1, 0): '>',
    (0, 1): 'v',
    (-1, 0): '<',
}

@cache
def press(mode, pos, btn):
    #print(RED + 'CACHE PRESS' + RESET)
    g = g1 if mode == 1 else g2
    to = g[btn]
    x1,y1 = pos
    x2,y2 = to
    dx, dy = x2-x1, y2-y1
    dv = (0, dy // abs(dy)) if dy != 0 else None
    dh = (dx // abs(dx), 0) if dx != 0 else None 
    steps = abs(dx) + abs(dy)
    paths = [(pos, '')]
    for _ in range(steps):
        p = len(paths)
        for _ in range(p):
            pos, moves = paths.pop(0)
            x,y = pos
            if dv != None and y != to[1]:
                xv, yv = x+dv[0], y+dv[1]
                if get(mode, xv, yv) is not None:
                    pos = (xv, yv)
                    move = moves + M[dv]
                    nxt = (pos, move)
                    paths.append(nxt)
            if dh != None and x != to[0]:
                xh, yh = x+dh[0], y+dh[1]
                if get(mode, xh, yh) is not None:
                    pos = (xh, yh)
                    move = moves + M[dh]
                    nxt = (pos, move)
                    paths.append(nxt)

    moves = [] 
    for (p,m) in paths:
        moves.append(m + 'A')
    return to, moves

@cache
def press_code(mode, p, code, multi=True):
    moves = set([''])
    for btn in code:
        btn_moves: set[str] = set()
        start = p
        for move in moves:
            p, new_moves = press(mode, start, btn)
            if not multi:
                new_moves = new_moves[:1]
            for m in new_moves:
                btn_moves.add(move + m)
        moves = btn_moves
    return moves, p

@cache
def do_move(start, to):
    transform = {
        (2,0): { # A
            (2,0): 'A', # A
            (0,1): 'v<<A', #< !!!!!!!!
            (1,0): '<A', # ^
            (1,1): '<vA', # v
            (2,1): 'vA', # >
        },
        (0,1): { # <
            (2,0): '>>^A', # A !!!!!!!!
            (0,1): 'A', #<
            (1,0): '>^A', # ^ !!!!!!!!!!
            (1,1): '>A', # v
            (2,1): '>>A', # >
        },
        (1,0): { # ^
            (2,0): '>A', # A
            (0,1): 'v<A', # < !!!!!!!!!!
            (1,0): 'A', # ^
            (1,1): 'vA', # v
            (2,1): 'v>A', # >
        },
        (1,1): { # v
            (2,0): '^>A', # A
            (0,1): '<A', #<
            (1,0): '^A', # ^
            (1,1): 'A', # v
            (2,1): '>A', # >
        },
        (2,1): { # >
            (2,0): '^A', # A
            (0,1): '<<A', #<
            (1,0): '<^A', # ^
            (1,1): '<A', # v
            (2,1): 'A', # >
        },
    }
    return transform[start][to]


@cache
def get_moves(btn, start, level):
    to = g2[btn]
    #print(start, to)
    #print(f'get_moves L{level}, {btn}: {start} -> {g2[btn]}')
    path = do_move(start, to)
    if level == 0:
        size = len(path)
        #print(f'path: {path}, size: {RED}{size}{RESET}')
        return size

    pos = start2
    size = 0
    for step in path:
        #print(LIGHT_BLUE_BG, f'\tCheck {step}', RESET)
        size += get_moves(step, pos, level-1)
        pos = g2[step]
        #print(RED,f'{step} L{level}: {size}',RESET)
    #print(RED, f'Level {level}:', size, RESET)
    return size



def recursor(moves, levels):
    #print('========================')
    paths = [] 
    #print(moves)
    pos = start2
    for path in moves:
        size = 0
        #print('--- path = ',path)
        for step in path:
            #print(BLUE, f'STEP: {step}',RESET)
            step_moves = get_moves(step, pos, levels)
            size += step_moves 
            #print(f'-- Move {step}: {step_moves}, size: {size}')
            pos = g2[step]
        paths.append(size)

    #for p in paths:
    #    print('POTH_',p)

    shortest = min(paths)
    #print('========================')
    return shortest


#moves, p = press_code(mode1, start1, '980A')
#print('move', moves)
#exit()
 
# t = ('^^^A<AvvvA>A', 60)
# t = ('<A^A>^^AvvvA', 68)
# level = 1
# res = recursor([t[0]], start2, level)
# print('Shortest',res)
# facit1 = len('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')
# facit2 = len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')
# print(res, t[1])
# assert (res == t[1])

test = True
test = False
rounds = 2 if test else 25

result = 0 
for code in lines:
    move1 = ''
    move2 = ''
    move3 = ''

    # Numeric pad
    moves, p = press_code(mode1, start1, code)
    moves = list(moves)
    moves.sort()

    #print(RED, '@'*40, RESET)
    #print(f'MOVES: {moves}')
    shortest = recursor(moves, rounds-1)
    #print(f'CODE: {code}, shortest: {shortest}')

    # Complexity 
    numval = int(code[:-1])
    complexity = numval * shortest
    result += complexity
    print(f'Code {code}: {numval} * {shortest} = {complexity}')
    
# Too high : 1053601423230440
# 26rounds : 422056735001040
# Too high : 415029892022154
# incorrect: 384361222449882
# incorrect: 172604482142956 
# Too low  : 163486690526044

# to guess : 258369757013802

last = 415029892022154
last = 84485380584214 # buggy
last = 83271015756208 # buggy
last = 53068906762876 # buggy
last = 172604482142956 # buggy
last = 296360022792276 
last = 214377236572368 
last = 214183571003190 
last = 384361222449882
last = 258369757013802
should_be = 213536 if test else last
print('Last guess:', last)
print('Should be', should_be)
if result == should_be:
    print(LIGHT_BLUE_BG, 'SAMESIES', result, RESET)
if result < should_be:
    print(GREEN, 'BETTER!!!!', result, RESET)
if result > last:
    print(RED, 'WORSE!!!!', result, RESET)

