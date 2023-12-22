print(chr(27)+'[2j')
print('\033c')
f = open('22.test', 'r')
f = open('22.input', 'r')
lines = [x.strip() for x in f.readlines()]


cubes = []
for line in lines:
    start, end = line.split('~')
    a, b, c = map(int, start.split(','))
    d, e, f = map(int, end.split(','))
    cubes.append((a, b, c, d, e, f))

RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
PINK = '\033[95m'
colors = [RED, GREEN, BLUE, YELLOW, PINK]
aoeu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()'
ids = []
for color in colors:
    for i in aoeu:
        ids.append(color+i+RESET)


def print_cubes(cubes):
    min_x = min([x[0] for x in cubes])
    max_x = max([x[3] for x in cubes])
    min_y = min([x[1] for x in cubes])
    max_y = max([x[4] for x in cubes])
    max_z = max([x[5] for x in cubes])

    print('--- X axis ---')
    for z in range(max_z, 0, -1):
        for x in range(min_x, max_x+1):
            is_cube = None
            for idx, (a, b, c, d, e, f) in enumerate(cubes):
                if a <= x <= d and c <= z <= f:
                    is_cube = ids[idx % len(ids)]
                    break
            if is_cube:
                print(is_cube, end='')
            else:
                print('.', end='')
        print()

    print('--- Y axis ---')
    for z in range(max_z, 0, -1):
        for y in range(min_y, max_y+1):
            is_cube = None
            for idx, (a, b, c, d, e, f) in enumerate(cubes):
                if b <= y <= e and c <= z <= f:
                    is_cube = ids[idx % len(ids)]
                    break
            if is_cube:
                print(is_cube, end='')
            else:
                print('.', end='')
        print()


def update_space_used(space_used, i, new_pos):
    used = [s for s, v in space_used.items() if v == i]
    for u in used:
        del space_used[u]
    for x in range(new_pos[0], new_pos[3]+1):
        for y in range(new_pos[1], new_pos[4]+1):
            for z in range(new_pos[2], new_pos[5]+1):
                space_used[(x, y, z)] = i
    return space_used


space_used = {}
for i, cube in enumerate(cubes):
    space_used = update_space_used(space_used, i, cube)


cube_fell = True
count = 0
while cube_fell:
    count += 1

    cube_fell = False
    for i, cube in enumerate(cubes):
        a, b, c, d, e, f = cube
        if c <= 1 or f <= 1:
            continue
        can_fall = True
        for x in range(a, d+1):
            for y in range(b, e+1):
                for z in range(c, f+1):
                    below = space_used.get((x, y, z-1), None)
                    if below is not None and below != i:
                        can_fall = False
                        break
        if can_fall:
            cube_fell = True
            new_cube = (a, b, c-1, d, e, f-1)
            space_used = update_space_used(space_used, i, new_cube)
            cubes[i] = new_cube

# print_cubes(cubes)
# Check which cubes can be removed. They can if cubes resting on them are supported by other cubes
cubes_to_remove = []

down = {}
up: dict[int, set[int]] = {}
for i, cube in enumerate(cubes):
    a, b, c, d, e, f = cube

    supported_cubes = set()
    for x in range(a, d+1):
        for y in range(b, e+1):
            for z in range(c, f+1):
                over = (x, y, z+1)
                if over in space_used:
                    supported_cube = space_used[over]
                    if supported_cube == i:
                        continue
                    supported_cubes.add(supported_cube)

    for supported_cube in supported_cubes:
        if supported_cube not in down:
            down[supported_cube] = set()
        down[supported_cube].add(i)
        if i not in up:
            up[i] = set()
        up[i].add(supported_cube)

    supported = []
    not_supported = []
    for sc in supported_cubes:
        i2 = ids[sc % len(ids)]
        space = [s for s, v in space_used.items() if v == sc]

        supported_by_others = False
        for x, y, z in space:
            curr = space_used[(x, y, z)]
            if (x, y, z-1) in space_used:
                under = space_used[(x, y, z-1)]
                i2 = ids[under % len(ids)]
                if under == curr or under == i:
                    continue
                supported_by_others = True
                break
        if supported_by_others:
            supported.append(sc)
        else:
            not_supported.append(sc)

    can_be_removed = len(supported) == len(supported_cubes)
    name = ids[i % len(ids)]
    can = 'can' if can_be_removed else 'cannot'
    support_str = ''
    for c in supported:
        support_str += f"{ids[c % len(ids)]} is supported. "
    for c in not_supported:
        support_str += f"{ids[c % len(ids)]} is not supported. "

    #print(f'Brick {name} {can} be disintegrated safely;\n\t {support_str}')
    if can_be_removed:
        cubes_to_remove.append(i)

print('Part 1:', len(cubes_to_remove))


def chain_reaction(new_cubes, space_used, cube_idx: int):
    fell_count = set()

    # new_cubes.pop(cube_idx)
    cube_fell = True
    while cube_fell:
        cube_fell = False
        for i, cube in enumerate(new_cubes):
            a, b, c, d, e, f = cube
            if c <= 1 or f <= 1:
                continue
            can_fall = True
            for x in range(a, d+1):
                for y in range(b, e+1):
                    for z in range(c, f+1):
                        below = space_used.get((x, y, z-1), None)
                        if below is not None and below != i:
                            if below != i and cube_idx != below:
                                can_fall = False
                                break
            if can_fall:
                fell_count.add(i)
                cube_fell = True
                new_cube = (a, b, c-1, d, e, f-1)
                space_used = update_space_used(space_used, i, new_cube)
                new_cubes[i] = new_cube
    return(len(fell_count))


sum_count = 0
for i in range(len(cubes)):

    new_cubes = cubes.copy()
    new_space_used = space_used.copy()
    chain_length = chain_reaction(new_cubes, new_space_used, i)
    #print('Chain length for cube', ids[i % len(ids)], 'is', chain_length)
    sum_count += chain_length
print('Part 2:', sum_count)
