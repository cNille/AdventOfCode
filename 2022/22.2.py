print(chr(27)+'[2j')
print('\033c')
f = open('22.test', 'r')
f = open('22.input', 'r')
lines = f.read()
tiles, instructions = lines.split('\n\n')
print("Day 22")
from colorama import Fore, Back, Style

tiles = tiles.split('\n')
max_width = max([len(t) for t in tiles])
mtx = []

# Build map
for y in range(len(tiles)):
    row = []
    for x in range(max_width):
        if x >= len(tiles[y]):
            row.append('@')
        elif tiles[y][x] == ' ':
            row.append('@')
        else:
            row.append(tiles[y][x])
    mtx.append(row)

def print_mtx(mtx, visited, extras = None):
    D_str = ">v<A"
    print('---')
    for y in range(len(mtx)):
        line = ""
        for x in range(len(mtx[0])):
            if extras is not None and (x,y) in extras:
                line += Back.WHITE + Fore.RED + '@' + Style.RESET_ALL
            elif (x,y) in visited:
                f = visited[(x,y)]
                line += Fore.GREEN + D_str[f] + Style.RESET_ALL
            elif mtx[y][x] == '@':
                line += Fore.LIGHTBLACK_EX + '@' + Style.RESET_ALL
            elif mtx[y][x] == '#':
                line += Fore.LIGHTRED_EX + '#' + Style.RESET_ALL
            else:
                line += mtx[y][x]
        print(line)

# Set startposition
pos = (0,0,0)
for i, ch in enumerate(mtx[0]):
    if ch == '.':
        pos = (i, 0, 0)
        break
print("Startpos", pos)
visited = {} 
visited[(pos[0], pos[1])] = pos[2]
#print_mtx(mtx, visited)

print(instructions)

def map_pos(pos):
    x, y ,_ = pos
    x2, y2, f2 = pos
    if 50 <= x and x <= 99 and 199 <= y and y <= 199: # 2U -> 10L ✅
        x2, y2, f2 = 0, 150 + (x-50), R 
        dx,dy = DIR[R] 
        return (x2, y2, f2), dx, dy
    elif 49 <= x and x <= 49 and 0 <= y and y <= 49: # 2L -> 7L  ✅
        x2, y2, f2 = 0, 149-(y), R
        dx,dy = DIR[R] 
        return (x2, y2, f2), dx, dy
    elif 100 <= x and x <= 149 and 199 <= y and y <= 199: # 3U -> 10D ✅
        x2, y2, f2 = x-100, 199, U 
        dx,dy = DIR[U] 
        return (x2, y2, f2), dx, dy
    elif 0 <= x and x <= 0 and 0 <= y and y <= 49: # 3R -> 8R ✅
        x2, y2, f2 = 99, 149-y, L 
        dx,dy = DIR[L]
        return (x2, y2, f2), dx, dy
    elif 100 <= x and x <= 149 and 50 <= y and y <= 50: # 3D -> 5R ✅
        x2, y2, f2 = 99, 50+(x-100), L 
        dx,dy = DIR[L]
        return (x2, y2, f2), dx, dy
    elif 100 <= x and x <= 100 and 50 <= y and y <= 99: # 5R -> 3D  ✅
        x2, y2, f2 = 100+(y-50), 49, U 
        dx,dy = DIR[U]
        return (x2, y2, f2), dx, dy
    elif 49 <= x and x <= 49 and 50 <= y and y <= 99: # 5L -> 7U  ✅
        x2, y2, f2 = y-50, 100, D
        dx,dy = DIR[D] 
        return (x2, y2, f2), dx, dy
    elif 0 <= x and x <= 49 and 99 <= y and y <= 99: # 7U -> 5L ✅
        x2, y2, f2 = 50, 50+x, R
        dx,dy = DIR[R] 
        return (x2, y2, f2), dx, dy
    elif 149 <= x and x <= 149 and 100 <= y and y <= 149: # 7L -> 2L ✅
        x2, y2, f2 = 50, 149-y, R
        dx,dy = DIR[R] 
        return (x2, y2, f2), dx, dy
    elif 100 <= x and x <= 100 and 100 <= y and y <= 149: # 8R -> 3R ✅
        x2, y2, f2 = 149, 149-y, L 
        dx,dy = DIR[L] 
        return (x2, y2, f2), dx, dy
    elif 50 <= x and x <= 99 and 150 <= y and y <= 150: # 8D -> 10R ✅
        x2, y2, f2 = 49, 150+(x-50), L 
        dx,dy = DIR[L] 
        return (x2, y2, f2), dx, dy
    elif 50 <= x and x <= 50 and 150 <= y and y <= 199: # 10R -> 8D ✅
        x2, y2, f2 = 50+(y-150), 149, U
        dx,dy = DIR[U] 
        return (x2, y2, f2), dx, dy
    elif 0 <= x and x <= 49 and 0 <= y and y <= 0: # 10D -> 3U  
        x2, y2, f2 = 100 + x, 0, D 
        dx,dy = DIR[D] 
        return (x2, y2, f2), dx, dy
    elif 149 <= x and x <= 149 and 150 <= y and y <= 199: # 10L -> 2U 
        x2, y2, f2 = 50+(y-150), 0, D
        dx,dy = DIR[D] 
        return (x2, y2, f2), dx, dy
    else:
        extras = set()
        extras.add((x,y))
        extras.add((x2,y2))
        print_mtx(mtx, visited, extras)
        print(past_instr)
        print("ERROR", x,y )
        print(extras)
        print("MAP", pos)
        print("NEW", (x2,y2)) 
        exit()

R, D, L, U= 0, 1, 2, 3
DIR = [(1,0), (0,1), (-1,0), (0,-1)]
def move(mtx, pos, steps, visited):
    x,y,f = pos
    dx,dy = DIR[f]
    h,w = len(mtx), len(mtx[0])
    new_pos = pos
    x2,y2 = x,y
    prev_pos = (x,y,f)
    prev_dx, prev_dy = dx,dy
    while True:
        x2 = (x2+dx) % w
        y2 = (y2+dy) % h
        if mtx[y2][x2] == '@':
            new_pos, dx, dy = map_pos((x2, y2, f))
            x2, y2, f = new_pos
            #print_mtx(mtx, visited)
        if mtx[y2][x2] == '.':
            new_pos = (x2,y2,f)
            visited[(x2,y2)] = f
            prev_pos= (x2,y2,f)
            prev_dx, prev_dy = dx,dy
            steps -= 1
            if steps == 0:
                break
        elif mtx[y2][x2] == '#':
            new_pos = prev_pos 
            x2,y2,_ = prev_pos
            dx, dy = prev_dx, prev_dy 
            break
        else:
            extras = set()
            extras.add((x2,y2))
            print_mtx(mtx, visited, extras)
            print("PREV", prev_pos, prev_dx, prev_dy)
            print("NEW", new_pos, dx, dy)
            print("ERR")
            exit()
    return new_pos, visited

def turn_right(pos):
    x,y,f = pos
    return (x,y, (f+1)%4)
def turn_left(pos):
    x,y,f = pos
    return (x,y, (f-1)%4)

steps = ""
past_instr = "" 
for instr in instructions:
    past_instr += instr
    if instr == "R":
        pos, visited = move(mtx, pos, int(steps), visited)
        steps = ""
        pos = turn_right(pos)
    elif instr == "L":
        pos, visited = move(mtx, pos, int(steps), visited)
        steps = ""
        pos = turn_left(pos)
    else:
        steps += instr
    visited[(pos[0], pos[1])] = pos[2]
    #print_mtx(mtx, visited)
if steps != "":
    pos, visited =move(mtx,pos,int(steps), visited)

print_mtx(mtx, visited)
def calc(pos):
    x,y,f = pos
    return (
        1000 * (y+1) + 
        4 * (x+1) + 
        f
    )
print("Solution part 2:", calc(pos))
