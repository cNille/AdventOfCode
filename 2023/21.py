from heapq import heappush, heappop
print(chr(27)+'[2j')
print('\033c')
f = open('21.input', 'r')
#f = open('21.test', 'r')
lines = [x.strip() for x in f.readlines()]
RESET = '\033[0m'
RED = '\033[91m'
RED_BACKGROUND = '\033[41m'
GREEN = '\033[92m'
BLUE = '\033[94m'


def print_map(visited, rocks, lines):
    min_x = min([x[0] for x in visited])
    max_x = max([x[0] for x in visited])
    min_y = min([x[1] for x in visited])
    max_y = max([x[1] for x in visited])
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            nx = x % len(lines[0])
            ny = y % len(lines)
            if (x, y) in visited:
                print(GREEN+"O" + RESET, end='')
            elif (nx, ny) in rocks:
                print(lines[ny][nx], end='')
            else:
                print(RED + lines[ny][nx] + RESET, end='')
        print()


def get_rocks(lines):
    rocks = set()
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == '#':
                rocks.add((x, y))
    return rocks


def solve1(steps, rocks):
    N, E, SIDE, S = (0, -1), (1, 0), (-1, 0), (0, 1)
    DIRECTIONS = [N, E, SIDE, S]
    start = (65, 65)
    queue = []
    heappush(queue, (0, start))
    step_list = {}
    while queue:
        depth, pos = heappop(queue)
        x, y = pos
        if depth > steps:
            continue

        nx = x % len(lines[0])
        ny = y % len(lines)
        if (nx, ny) in rocks:
            continue
        even = depth % 2 == 0
        if even not in step_list:
            step_list[even] = set()
        if pos in step_list[even]:
            continue
        step_list[even].add(pos)

        for d in DIRECTIONS:
            dx, dy = d
            new_pos = (x+dx, y+dy)
            #new_pos = (new_pos[0] % len(lines[0]), new_pos[1] % len(lines))
            heappush(queue, (depth+1, new_pos))
    return step_list


rocks = get_rocks(lines)
results = []
print()
for x in range(202300+1):
    s = 65 + 131 * x
    res = solve1(s, rocks)
    if x == 0:
        print("Part 1:", len(res[1]))
    results.append(len(res[1 - s % 2]))
    if len(results) > 2:
        break


def sequence(steps, points):
    x0 = points[0]
    x1 = points[1]
    x2 = points[2]
    a = (x2+x0-2*x1)/2
    b = x1-x0-a
    c = x0
    return int(a*steps**2+b*steps+c)


print('Part 2:', sequence(202300, results))

exit()


steps = 50
width = len(lines[0])
height = len(lines)
assert(width == height)
print("Width:", width)
print("Height:", height)
print("Steps:", steps)
print('-'*20)

SIDE = 202300

even_spots = 0
odd_spots = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        steps_from_middle = abs(x-65) + abs(y-65)
        is_within_diamond = steps_from_middle < 66
        # Opposite, due to start being in odd position
        is_even = steps_from_middle % 2 == 0
        if (x, y) not in rocks:
            if is_even:
                even_spots += 1
            else:
                odd_spots += 1
        if is_within_diamond:
            if is_even:
                if (x, y) in rocks:
                    print('#', end='')
                else:
                    print(GREEN+'.'+RESET, end='')
            else:
                if (x, y) in rocks:
                    print('#', end='')
                else:
                    print(GREEN+'O'+RESET, end='')
        else:
            if is_even:
                if (x, y) in rocks:
                    print('#', end='')
                else:
                    print(RED+'O'+RESET, end='')
            else:
                if (x, y) in rocks:
                    print('#', end='')
                else:
                    print(BLUE+'.'+RESET, end='')
    print()

SIDE = 202300
squares_visited = 0
odd_squares = 1
even_squares = 0
last_odd_addition = 0
last_even_addition = 0
for i in range(SIDE):
    squares_visited += (i)*4 + 4
    is_even = i % 2 == 0
    if is_even:
        last_even_addition = (i)*4 + 4
        even_squares += (i)*4 + 4
    else:
        last_odd_addition = (i)*4 + 4
        odd_squares += (i)*4 + 4

print('Squares visited', squares_visited)
print('Even squares', even_squares)
print('Odd squares', odd_squares)
print('Last even addition', last_even_addition)
print('Last odd addition', last_odd_addition)
print(odd_squares+even_squares)
print('-'*10)

# Calculate diagonals that are double counted.
perimeter = (26501365)*2
print('Perimeter', perimeter)

print('even spots', even_spots)
print('odd spots', odd_spots)

print('-'*20)

half_odds = last_odd_addition
print('half odds', half_odds)
half_odds = last_odd_addition

SIDE = 202300
SIDE = SIDE*2+1
AREA = (SIDE*SIDE)//2
TOO_MUCH = half_odds * even_spots
print('too much', TOO_MUCH)

print('W', SIDE)
print('AREA', AREA)
#odd_squares = AREA // 2
#print('odd squares', odd_squares)
#even_squares = AREA - odd_squares
#print('even squares', even_squares)

A = even_spots * odd_squares
B = odd_spots * even_squares
print('A', A)
print('B', B)
C = A+B - TOO_MUCH
print('=', C)
answer = 628206330073385
if C == answer:
    print(GREEN+'C', answer, RESET)
else:
    print(RED+'C', answer, RESET)
    print('D', C-answer)
