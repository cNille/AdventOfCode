print(chr(27)+'[2j')
print('\033c')
f = open('03.input', 'r')
#f = open('03.test', 'r')
content = [x.strip() for x in f.readlines()]
lines = content

mtx = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        mtx[(x,y)] = c

def get_all_neighbours(visited, mtx,x,y):
    neighbours = []
    for i in range(-1,2):
        for j in range(-1,2):
            x1: int = x+i
            y1: int = y+j
            if (x1,y1) in visited:
                continue
            if i == j == 0:
                continue
            if (x1,y1) not in mtx:
                continue
            if mtx[(x1,y1)] == '.':
                continue
            neighbours.append((x1,y1))
            visited.add((x1,y1))
            neighbours.extend(get_all_neighbours(visited, mtx, x+i, y+j))
    return neighbours

symbols = set()
groups = []
visited = set()
gear_pos = set()
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        if mtx[(x,y)] == '.':
            continue
        if mtx[(x,y)].isdigit():
            continue
        if (x,y) in visited:
            continue
        symbols.add(mtx[(x,y)])
        neighbours = get_all_neighbours(visited, mtx, x, y)
        if mtx[(x,y)] == '*':
            gear_pos.add((x,y))
        groups.append(neighbours)
        visited.add((x,y))

numbers = []
gear = 0
for g in groups:
    keys = g.copy()
    keys = sorted(keys, key=lambda x: x[1] * 1000 + x[0])
    prev = keys[0]
    num = [mtx[prev]]
    group_numbers = []

    is_gear = False
    for k in keys:
        if k in gear_pos:
            is_gear = True

    for k in keys[1:]:
        is_next = k[0] - prev[0] == 1 and k[1] - prev[1] == 0

        if is_next:
            num.append(mtx[k])
            prev = k 
        elif len(num) > 0:
            new_num: str = ''.join(num)
            arr = []
            for s in symbols:
                if s in new_num:
                    arr = new_num.split(s)
            if len(arr) == 0:
                arr = [new_num]
            for n in arr:
                if n.isdigit():
                    group_numbers.append(int(n))
            num = [mtx[k]]
            prev = k

    new_num = ''.join(num)
    arr = []
    for s in symbols:
        if s in new_num:
            arr = new_num.split(s)
    if len(arr) == 0:
        arr = [new_num]
    for n in arr:
        if n.isdigit():
            group_numbers.append(int(n))

    if is_gear and len(group_numbers) == 2:
        gear += group_numbers[0] * group_numbers[1]


    numbers.extend(group_numbers)


print('Part 1:', sum(numbers))
print('Part 2:', gear)
