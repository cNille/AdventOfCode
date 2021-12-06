from collections import defaultdict
# f = open('05.input', 'r')
f = open('05.test', 'r')
rows = [x.strip() for x in f.readlines()]

part1_lines = []
part2_lines = []
for r in rows:
    a,b = r.split(' -> ')
    x1, y1 = map(int,a.split(','))
    x2, y2 = map(int,b.split(','))
    line = (x1, y1, x2, y2)

    dx = x2 - x1
    dy = y2 - y1
    # Part 1: Horizontal or vertical lines only
    if dx == 0 or dy == 0:
        part1_lines.append(line)

    # Part 2: Include diagonal lines
    if dx == 0 or dy == 0 or dx == dy or dx == -dy:
        part2_lines.append(line)

def print_graph(points):
    min_x = min_y = 0
    max_x = max_y = 0
    for (x,y) in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    for y in range(min_y-1, max_y+1):
        print(''.join([
           '.' if (x,y) not in points else str(points[(x,y)])
            for x in range(min_x-1, max_x+1)
        ]))

def count_points(lines):
    points = defaultdict(int)
    for (x1,y1,x2,y2) in lines:
        dx = x2 - x1
        dy = y2 - y1
        dx = 0 if dx == 0 else dx / abs(dx)
        dy = 0 if dy == 0 else dy / abs(dy)

        x = x1 
        y = y1 
        while (x != (x2 + dx) or y != (y2 + dy)):
            points[(x,y)] += 1
            x += dx
            y += dy
    more_than_two_lines = [k for k in points if points[k] > 1]
    print_graph(points)
    return len(more_than_two_lines)

print("Solution part1: %d" % count_points(part1_lines))
print("Solution part2: %d" % count_points(part2_lines))
