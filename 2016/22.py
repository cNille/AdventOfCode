print(chr(27)+'[2j')
print('\033c', end='')

print("Day 22")
f = open('22.input', 'r')
# f = open('21.test', 'r')
lines = [x.strip() for x in f.readlines()]


# part 1
nodes = [l.split() for l in lines[2:]]
count = 0
for n1 in nodes:
    for n2 in nodes:
        # print(l)
        file1, size1, used1, avail1, use1 = n1
        file2, size2, used2, avail2, use2 = n2
        assert (used1.endswith('T'))
        assert (used2.endswith('T'))
        if used1.startswith('0'):
            continue
        if file1 == file2:
            continue
        used = int(used1[:-1])
        avail = int(avail2[:-1])
        if used <= avail:
            count += 1
print("Part 1:", count)

max_x, max_y = 0, 0
grid = {}
for n in nodes:
    file, size, used, avail, use = n
    _, x, y = file.split('-')
    x = int(x[1:])
    y = int(y[1:])
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    if x == 15 and y == 29:
        print(file, size, used, avail, use)
    if len(size) >= 4:
        grid[(x, y)] = '#'
    elif used.startswith('0'):
        print("Empty on", x, y)
        grid[(x, y)] = '_'
    else:
        grid[(x, y)] = '.'
    # print(file, x, y)

mtx = []
print("MAX x", max_x)
print("MAX y", max_y)
for y in range(max_y + 1):
    mtx.append('')
    for x in range(max_x + 1):
        mtx[-1] += grid[(x, y)]


def print_mtx(mtx):
    for r in mtx:
        print(r)


print_mtx(mtx)

# Steps necessary:
to_left = 15 - 3
up = 29
to_right = 32 - 3

# 29 + 29 + 12 = 70
total = to_left + up + to_right
steps_left = 31
per_step = 5
total += 31 * 5
print("Part 2:", total)
