f = open('09.test', 'r')
# f = open('09.input', 'r')
lines = [x.strip() for x in f.readlines()]

def get_neighbour(lines,x,y):
    if y < 0 or y >= len(lines):
        return None
    if x < 0 or x >= len(lines[0]):
        return None
    return (x,y) 

def get_neighbours(lines,point):
    x,y = point
    neighbours = [
        get_neighbour(lines, x - 1, y + 0),
        get_neighbour(lines, x + 1, y + 0),
        get_neighbour(lines, x + 0, y - 1),
        get_neighbour(lines, x + 0, y + 1),
    ]
    neighbours = [n for n in neighbours if n is not None]
    return neighbours

total_risk = 0
low_points = [] 
for y in range(len(lines)):
    for x in range(len(lines[0])):
        point = int(lines[y][x])
        neighbours = get_neighbours(lines,(x,y))
        is_low_point = len([nx for nx,ny in neighbours if int(lines[ny][nx]) <= point]) == 0
        if not is_low_point:
            continue
        low_points.append((x,y))
        risk_level = point + 1
        total_risk += risk_level

print("Solution part 1: %d " % total_risk)

basins = []
basin_index = {}
def get_basin(basin_index, lines, point, idx):
    basin_index[point] = idx
    basin = {point}

    for n in get_neighbours(lines, point):
        if int(lines[n[1]][n[0]]) < 9 and n not in basin_index:
            basin |= get_basin(basin_index, lines, n, idx)
    return basin
    
for idx, point in enumerate(low_points):
    basin = get_basin(basin_index, lines, point, idx)
    basins.append(len(basin))

basins = sorted(basins)
basins.reverse()
print("Solution part 2: %d" % (basins[0] * basins[1] * basins[2]))
