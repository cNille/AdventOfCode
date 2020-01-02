area = [x.strip() for x in open('24.input', 'r').readlines()]


def biodiversity(area):
    res = 0
    count = 0
    for y, row in enumerate(area):
        for x, ch in enumerate(row):
            if ch == '#':
                res += 2**count
            count += 1
    return res



for a in area:
    print a


seen = {}
bio = biodiversity(area)

deltas = [(1,0), (-1,0), (0,1), (0,-1)]
while bio not in seen:
    seen[bio] = 0

    new_area = []
    for Y, row in enumerate(area):
        new_area.append('')
        for X, ch in enumerate(row):

            neighbours = [(X+dx, Y+dy) for dx,dy in deltas]
            neighbours = [(x,y) for (x,y) in neighbours if x >= 0 and x < 5 and y >=0 and y < 5]
            bugneighbours = [(x,y) for (x,y) in neighbours if area[y][x] == '#'] 
            bugs = len(bugneighbours)

            if area[Y][X] == '#' and bugs != 1:
                new_area[Y] += '.'
            elif area[Y][X] == '.' and bugs == 1 or bugs == 2:
                new_area[Y] += '#'
            else:
                new_area[Y] += area[Y][X]

    print '='*20
    for n in new_area:
        print n
    print '='*20

    area = new_area
    bio = biodiversity(area)


print seen
print bio

# too low:  14567263
# too high  33546111
