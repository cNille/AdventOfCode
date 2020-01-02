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


area = [x.strip() for x in open('24.input', 'r').readlines()]

levels = {}
levels[0] = area
levels[-1] = ['.....' for _ in range(5)]
levels[1] = ['.....' for _ in range(5)]

z_min = -1
z_max = 1
for oeu in range(200):
    new_areas = {}

    for level in range(z_min, z_max+1):
        area = levels[level]
        new_area = []
        for Y, row in enumerate(area):
            new_area.append('')
            for X, ch in enumerate(row):
                if (X,Y) == (2,2):
                    new_area[Y] += '.'
                    continue
                sides = [(X+dx, Y+dy, level) for dx,dy in deltas]
                neighbours = []
                for (x,y,z) in sides:
                    if z > 200 or z < -200:
                        continue
                    if x < 0:
                        neighbours.append((1,2,z-1))
                        continue
                    if y < 0:
                        neighbours.append((2,1,z-1))
                        continue
                    if x == 5:
                        neighbours.append((3,2,z-1))
                        continue
                    if y == 5:
                        neighbours.append((2,3,z-1))
                        continue
                    if (x,y) == (2,2):
                        if (X, Y) == (1,2):
                            neighbours += [(0,i,z+1) for i in range(5)]
                        if (X, Y) == (2,1):
                            neighbours += [(i,0,z+1) for i in range(5)]
                        if (X, Y) == (3,2):
                            neighbours += [(4,i,z+1) for i in range(5)]
                        if (X, Y) == (2,3):
                            neighbours += [(i,4,z+1) for i in range(5)]
                        continue
                    neighbours.append((x,y,z))
                        
                for _,_,z in neighbours:
                    if z not in levels:
                        levels[z] = ['.....' for _ in range(5)]
                        new_areas[z] = levels[z]
                
                bugneighbours = [z for (x,y,z) in neighbours if levels[z][y][x] == '#'] 
                zneighbours = [z for (x,y,z) in neighbours] 
                z_min = min([z_min] + zneighbours)
                z_max = max([z_max] + zneighbours)
                bugs = len(bugneighbours)

                if area[Y][X] == '#' and bugs != 1:
                    new_area[Y] += '.'
                elif area[Y][X] == '.' and bugs == 1 or bugs == 2:
                    new_area[Y] += '#'
                else:
                    new_area[Y] += area[Y][X]
        new_areas[level] = new_area
    levels = new_areas

total_count = 0
for level in levels:
    area = levels[level]
    lines = "".join(area)
    bugs = len([l for l in lines if l == "#"])
    total_count += bugs
print "Part 2: %d" % total_count
