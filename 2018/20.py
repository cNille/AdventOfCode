# Import data
data = [r.strip() for r in open('20.in', 'rb').readlines()]
input = data[0][1:-1]

doors = set()
rooms = set()

x_min = 0
y_min = 0
x_max = 0
y_max = 0

path = input
pos = {(0, 0)}
stack = []
starts = {(0, 0)}
ends = set()

for i, ch in enumerate(path):
    if i % 500 == 0:
        print('%d of %d' % (i, len(path)))

    if ch == '(':
        stack.append((starts, ends))
        ends = set()
        starts = pos
        continue
    if ch == '|':
        ends.update(pos)
        pos = starts
        continue
    if ch == ')':
        pos.update(ends)
        starts, ends = stack.pop()
        continue

    if ch == 'N':
        delta_d = (-1, 0)
        delta_r = (-2, 0)
    if ch == 'S':
        delta_d = (1, 0)
        delta_r = (2, 0)
    if ch == 'W':
        delta_d = (0, -1)
        delta_r = (0, -2)
    if ch == 'E':
        delta_d = (0, 1)
        delta_r = (0, 2)

    for (y, x) in pos:
        doors.add((y + delta_d[0], x + delta_d[1]))
        rooms.add((y + delta_r[0], x + delta_r[1]))
    pos = {(y + delta_r[0], x + delta_r[1]) for (y, x) in pos}

    for (y, x) in pos:
        y_min = min(y, y_min)
        y_max = max(y, y_max)
        x_min = min(x, x_min)
        x_max = max(x, x_max)

print(y_min, x_min)
print(y_max, x_max)

karta = ['#' * (x_max - x_min + 5)]
karta.append('#' * (x_max - x_min + 5))
for y in range(y_min, y_max + 1):
    karta.append(['##'])
    for x in range(x_min, x_max + 1):
        if (y, x) == (0, 0):
            karta[-1].append('X')
        elif (y, x) in doors:
            karta[-1].append(' ')
        elif (y, x) in rooms:
            karta[-1].append('.')
        else:
            karta[-1].append('#')
    karta[-1].append('##')
karta.append('#' * (x_max - x_min + 5))
karta.append('#' * (x_max - x_min + 5))

print(len(karta))
print(len(karta[0]))
print(len(karta[-1]))

# Print map
for k in karta:
    print(''.join(k))

# Get start position
checked = set()
for y, line in enumerate(karta):
    for x, ch in enumerate(line):
        if ch == 'X':
            checked.add((x, y))

print('Starting pos:', checked)
count = 0
depth = []
res2 = 0
while len(checked) < len(rooms):
    if count == 999:
        # 1 for the starting room
        res2 = len(rooms) - len(checked) + 1
    if count % 20 == 0:
        print('Iteration: %d, checked %d of %d' % (count, len(checked),
                                                   len(rooms)))

    to_add = set()
    for (x, y) in checked:
        if karta[y][x + 1] == ' ':
            to_add.add((x + 2, y))
        if karta[y][x - 1] == ' ':
            to_add.add((x - 2, y))
        if karta[y + 1][x] == ' ':
            to_add.add((x, y + 2))
        if karta[y - 1][x] == ' ':
            to_add.add((x, y - 2))
    depth.append([a for a in to_add if a not in checked])
    for a in to_add:
        checked.add(a)
    count += 1

print('Part 1: %d' % (count + 1))
print('Part 2: %d' % res2)
