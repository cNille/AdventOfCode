f = open('11.test', 'r')
#f = open('11.input', 'r')
lines = [x.strip() for x in f.readlines()]

# Make to matrix of integers
for y in range(len(lines)):
    lines[y] = [int(char) for char in lines[y]] 

def print_map(lines):
    for y in range(len(lines)):
        print(''.join([str(x) for x in lines[y]]))

def get_neighbour(lines,x,y):
    if y < 0 or y >= len(lines):
        return None
    if x < 0 or x >= len(lines[0]):
        return None
    return (x,y) 

def get_neighbours(lines,point):
    x,y = point
    neighbours = [
        get_neighbour(lines, x - 1, y - 1),
        get_neighbour(lines, x - 1, y + 0),
        get_neighbour(lines, x - 1, y + 1),
        get_neighbour(lines, x + 0, y - 1),
        get_neighbour(lines, x + 0, y + 1),
        get_neighbour(lines, x + 1, y - 1),
        get_neighbour(lines, x + 1, y + 0),
        get_neighbour(lines, x + 1, y + 1),
    ]
    return [n for n in neighbours if n is not None]

def increase(lines,x,y, flashed):
    current = lines[y][x]
    if current <= 9 or (x,y) in flashed:
        return
    flashed.add((x,y))

    for (nx, ny) in get_neighbours(lines, (x,y)):
        lines[ny][nx] += 1 
        if lines[ny][nx] > 9 and (nx,ny) not in flashed:
            increase(lines, nx, ny, flashed)

steps = 100
step = 0
all_flashes = 0
octopus_count = len(lines) * len(lines[0])

print_map(lines)
while True:
    step += 1
    flashed = set()
    # Increase by one
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            current = lines[y][x]
            current += 1
            lines[y][x] = current
    # Flashes
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            increase(lines, x, y, flashed)
    # Reset flashed to 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] > 9:
                lines[y][x] = 0
    print_map(lines)

    print('Step %d, flashes: %d (%d)' % (step, len(flashed), octopus_count))
    if len(flashed) == octopus_count:
        print('All octopus_count are synchronized!')
        break
    if step <= 100:
        all_flashes += len(flashed) 

print("Solution part 1: %d" % all_flashes)
print("Solution part 2: %d" % step)
