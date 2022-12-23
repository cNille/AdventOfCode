print(chr(27)+'[2j')
print('\033c')
f = open('23.test', 'r')
f = open('23.test2', 'r')
f = open('23.test3', 'r')
f = open('23.input', 'r')
lines = [x.strip() for x in f.readlines()]
print("Day 23")


elves = set()
for y in range(len(lines)):
    print(lines[y])
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            elves.add((x,y))
#print(elves)


#- If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
#- If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
#- If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
#- If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

DN = [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)]
SIDES = [
    [( 0,-1), (-1,-1), ( 1,-1)], # NORTH
    [( 0, 1), (-1, 1), ( 1, 1)], # SOUTH
    [(-1, 0), (-1,-1), (-1, 1)], # WEST
    [( 1, 0), ( 1,-1), ( 1, 1)], # EAST
]

def propose(elves, pos, ROUND):
    x,y = pos
    neighbours = [(x+dx, y+dy) for dx,dy in DN]
    if len([n for n in neighbours if n in elves]) == 0:
        return None 

    for offset in range(4):
        direction = SIDES[(ROUND + offset) % len(SIDES)]
        side = [(x+dx, y+dy) for dx,dy in direction]
        side_elves = [pos for pos in side if pos in elves]
        if (len(side_elves) != 0):
            continue 
        dx,dy = direction[0]
        new_pos = (x+dx, y+dy)
        return new_pos
    return None

def game_round(elves, ROUND):
    # Propose
    proposals = {} 
    for pos in elves:
        new_pos = propose(elves, pos, ROUND)
        if new_pos is not None:
            if new_pos not in proposals:
                proposals[new_pos] = [] 
            proposals[new_pos].append(pos) 
    new_elves = elves

    # Move
    moves = 0
    for new_pos in proposals:
        if len(proposals[new_pos]) > 1:
            continue
        #print("MOV", proposals[new_pos], new_pos)
        old = proposals[new_pos][0]
        new_elves.remove(old)
        new_elves.add(new_pos)
        moves += 1

    return new_elves, moves

def print_map(elves):
    print('-'*40)
    min_x, min_y, max_x, max_y = 99999999, 9999999, 0,0
    for x,y in elves:
        min_x = min(x,min_x)
        max_x = max(x,max_x)
        min_y = min(y,min_y)
        max_y = max(y,max_y)
    for y in range(min_y-1,max_y+2):
        line = ""
        for x in range(min_x-1,max_x+2):
            if (x,y) in elves:
                line += "#"
            else:
                line += "."
        print(line)


for i in range(10000):
    elves, moves = game_round(elves, i)
    #print_map(elves)
    if moves == 0:
        print("Solution part 2:", i+1)
        break
    if i == 9:
        # Part1
        min_x, min_y, max_x, max_y = 99999999, 9999999, 0,0
        for x,y in elves:
            min_x = min(x,min_x)
            max_x = max(x,max_x)
            min_y = min(y,min_y)
            max_y = max(y,max_y)
        empty_tiles = 0 
        for y in range(min_y, max_y+1):
            for x in range(min_x,max_x+1):
                if (x,y) not in elves:
                    empty_tiles += 1
        print("Solution part 1:", empty_tiles)
