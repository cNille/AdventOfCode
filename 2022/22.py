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

def print_mtx(mtx, visited):
    D_str = ">v<A"
    print('---')
    for y in range(len(mtx)):
        line = ""
        for x in range(len(mtx[0])):
            if (x,y) in visited:
                f = visited[(x,y)]
                line += Fore.GREEN + D_str[f] + Style.RESET_ALL
                continue
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

D = [(1,0), (0,1), (-1,0), (0,-1)]
def move(mtx, pos, steps, visited):
    x,y,f = pos
    dx,dy = D[f]
    h,w = len(mtx), len(mtx[0])
    new_pos = pos
    x2,y2 = x,y
    prev_pos = (x,y,f)
    while True:
        x2 = (x2+dx) % w
        y2 = (y2+dy) % h
        if mtx[y2][x2] == '.':
            new_pos = (x2,y2,f)
            visited[(x2,y2)] = f
            prev_pos= (x2,y2,f)
            steps -= 1
            if steps == 0:
                break
        if mtx[y2][x2] == '#':
            new_pos = prev_pos 
            break

    return new_pos, visited

def turn_right(pos):
    x,y,f = pos
    return (x,y, (f+1)%4)
def turn_left(pos):
    x,y,f = pos
    return (x,y, (f-1)%4)

steps = ""
for instr in instructions:
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
print("Solution part 1:", calc(pos))
