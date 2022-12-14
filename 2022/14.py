print(chr(27)+'[2j')
print('\033c')
f = open('14.test', 'r')
#f = open('14.input', 'r')
lines = [x.strip() for x in f.readlines()]

def print_map(rock: set[tuple[int,int]], sands: set[tuple[int,int]]):
    xs = [p[0] for p in rock] + [p[0] for p in sands]
    ys = [p[1] for p in rock] + [p[1] for p in sands]
    
    for y in range(min(ys)-3, max(ys)+3):
        line = ""
        for x in range(min(xs)-3, max(xs)+3):
            if (x,y) in rock:
                line += "#"
            elif (x,y) in sands:
                line += "o"
            else: 
                line += "."
        print(line)
        
rock = set()
sands = set() 
for line in lines:
    paths = line.split(' -> ')
    paths = [p.split(',') for p in paths]
    paths = [(int(p[0]), int(p[1])) for p in paths]
    prev = paths[0]
    rock.add(prev)
    for p in paths[1:]:
        direction = (0, 0)
        if p[1] == prev[1] and p[0] > prev[0]:
            direction = (1, 0)
        if p[0] == prev[0] and p[1] > prev[1]:
            direction = (0, 1)
        if p[1] == prev[1] and p[0] < prev[0]:
            direction = (-1, 0)
        if p[0] == prev[0] and p[1] < prev[1]:
            direction = (0, -1)

        current = prev
        while current != p:
            current = (current[0] + direction[0], current[1] + direction[1])
            rock.add(current)
        prev = p

ys = [p[1] for p in rock]
Y_LIMIT = max(ys)

finished_part1 = False
finished_part2 = False
while not finished_part2:
    sand = (500, 0)
    is_resting = False
    while not is_resting:
        down = (sand[0], sand[1]+1)
        downleft = (sand[0]-1, sand[1]+1)
        downright = (sand[0]+1, sand[1]+1)

        if not finished_part1 and down[1] > (Y_LIMIT + 1):
            print("Solution part 1:", len(sands))
            finished_part1 = True
        elif down[1] > (Y_LIMIT + 1):
            is_resting = True
            sands.add(sand)
        elif down not in rock and down not in sands:
            sand = down
        elif downleft not in rock and downleft not in sands:
            sand = downleft
        elif downright not in rock and downright not in sands:
            sand = downright
        else:
            if down[1] == 1:
                finished_part2 = True
            is_resting = True
            sands.add(sand)
        
    #print_map(rock,sands)
print("solution part 2:", len(sands))
