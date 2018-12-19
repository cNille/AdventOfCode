from time import sleep

# import data
data = [line.strip() for line in open('18.in', 'r').readlines()]

def getadjacent((x,y)):
    adjacent = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            adjacent.append((x+i, y+j))
    return adjacent

def withinborder((x,y)):
    global state
    within_x = 0 <= x < len(state[0])
    within_y = 0 <= y < len(state)
    return within_x and within_y

def open(pos):
    global state
    adjacents = filter(withinborder, getadjacent(pos))
    trees = filter(lambda (x,y): state[y][x] == '|', adjacents)
    if len(trees) >= 3:
        return '|'
    return '.'
def trees(pos):
    global state
    adjacents = filter(withinborder, getadjacent(pos))
    lumberyards = filter(lambda (x,y): state[y][x] == '#', adjacents)
    if len(lumberyards) >= 3:
        return '#'
    return '|'
def lumberyard(pos):
    global state
    adjacents = filter(withinborder, getadjacent(pos))
    lumberyards = filter(lambda (x,y): state[y][x] == '#', adjacents)
    trees = filter(lambda (x,y): state[y][x] == '|', adjacents)
    if len(lumberyards) >= 1 and len(trees) >= 1:
        return '#'
    return '.'
def countresult():
    global state
    trees_count = 0
    lumberyard_count = 0
    for row in state:
        for cell in row:
            if cell == '|':
                trees_count += 1
            if cell == '#':
                lumberyard_count += 1
    result = trees_count * lumberyard_count
    return result

# Noticed repeating pattern from around ~ 480. Start collecting
# results from then to get the repeat-chain.
start_counting = 00
state = data
scores = []
for i in range(1,529):
    new_state = []
    for y, row in enumerate(state):
        new_state.append([])
        for x, cell in enumerate(row):
            if cell == '.':
                new_state[-1].append(open((x,y)))
            if cell == '|':
                new_state[-1].append(trees((x,y)))
            if cell == '#':
                new_state[-1].append(lumberyard((x,y)))
    state = new_state
    print('='*80)
    print('Iteration: %d' % (i+1))

    if i == 10:
        result = countresult()
        print('Part 1 result:', result)

    if start_counting <= i:
        result = countresult()
        if result not in scores:
            scores.append(result)
            print('Result: %d', result)

    for row in state:
        print(''.join(row))
    sleep(0.1)

result = scores[(1000000000 - 500) % len(scores)]
print('Part 2: %d' % result)
