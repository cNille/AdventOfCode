area = [x.strip() for x in open('24.input', 'r').readlines()]

def biodiversity(area):
    return sum([2**(x) for x in range(25) if area[x/5][x%5] == '#'])

seen = set() 
bio = biodiversity(area)
deltas = [(1,0), (-1,0), (0,1), (0,-1)]
while bio not in seen:
    seen.add(bio)
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
    area = new_area
    bio = biodiversity(area)
print "Part 1: %d " % bio
