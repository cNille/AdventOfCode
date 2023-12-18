print(chr(27)+'[2j')
print('\033c')
#f = open('18.input', 'r')
f = open('18.test', 'r')
lines = [x.strip() for x in f.readlines()]

DIR = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
R, D, L, U = DIR['R'], DIR['D'], DIR['L'], DIR['U']
directions = [R, D, L, U]
min_x, min_y = 0, 0
max_x, max_y = 0, 0

start = (0, 0)
pos = start
corners = []
print('Starting...')
for l in lines:
    direction, steps, color = l.split(' ')
    color = color[1:-1]

    hex_steps = int(color[1:-1], 16)
    d = int(color[-1])
    hex_direction = directions[d]
    dx, dy = hex_direction
    dx *= hex_steps
    dy *= hex_steps

    corners.append((d, pos[0], pos[1]))
    pos = (pos[0] + dx, pos[1] + dy)
    min_x = min(min_x, pos[0])
    min_y = min(min_y, pos[1])
    max_x = max(max_x, pos[0])
    max_y = max(max_y, pos[1])
print('Corners extracted: {}'.format(len(corners)))
print(min_x, min_y, max_x, max_y)

end = corners[1:]
end.append(corners[0])
end.append(corners[1])
pairs = list(zip(corners, end))
print('Pairs: {}'.format(len(pairs)))

edge_length = 0
for p in pairs:
    edge_length += abs(p[0][1] - p[1][1]) + abs(p[0][2] - p[1][2])


def shoelace_formula(corners):
    n = len(corners)  # Number of corners
    area = 0

    # Sum over each edge
    for i in range(n):
        j = (i + 1) % n  # Next vertex index
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]

    area = abs(area) / 2
    return area


def get_area(corners):
    area = shoelace_formula(corners)
    return int(area)


corners = [(d[1], d[2]) for d in corners]
area = get_area(corners)
print('Area:\t\t {}'.format(area))
edge_length = edge_length // 2
area = area + edge_length + 1
print('Edge length:\t      {}'.format(edge_length))
print('Area minus edge: {}'.format(area))
test_answer = 952408144115
print('Answer:\t\t {}'.format(test_answer))
diff = abs(test_answer - area)
print('Difference:\t      {}'.format(diff))
exit()
