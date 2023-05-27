print(chr(27)+'[2j')
print('\033c', end='')
f = open('18.input', 'r')
lines = [x.strip() for x in f.readlines()] 

mtx = []
for line in lines:
    mtx.append([x for x in line])

def get_adjacent(mtx, x, y, part2 = False):
    adj = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if x+i < 0 or y+j < 0:
                continue
            try:
                if part2 and is_corner(mtx, x+i, y+j):
                    adj.append('#')
                    continue
                adj.append(mtx[x+i][y+j])
            except IndexError:
                continue
    return adj

def is_corner(mtx, x, y):
    return ( x == 0 or x == len(mtx)-1) and ( y == 0 or y == len(mtx[x])-1)

def get_next(mtx, part2 = False):
    new_mtx = []
    for i in range(len(mtx)):
        new_mtx.append([])
        for j in range(len(mtx[i])):
            if part2 and is_corner(mtx, i, j):
                new_mtx[i].append('#')
                continue
            adj = get_adjacent(mtx, i, j, part2)
            if mtx[i][j] == '#':
                adj_on = adj.count('#')
                stay_on = adj_on in [2, 3]
                new_mtx[i].append('#' if stay_on else '.')
            elif mtx[i][j] == '.':
                adj_on = adj.count('#')
                new_mtx[i].append('#' if adj_on == 3 else '.')
    return new_mtx

def count_lights(mtx):
    are_on = 0
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] == '#':
                are_on += 1
    return are_on 

# Part 1
lights_on = 0
mtx_1 = mtx
for i in range(100):
    mtx_1 = get_next(mtx_1)
    lights_on = count_lights(mtx_1)
print("Solution part 1:", lights_on)

# Part 2
lights_on = 0
mtx_2 = mtx
for i in range(100):
    mtx_2 = get_next(mtx_2, True)
    lights_on = count_lights(mtx_2)
print("Solution part 2:", lights_on)
