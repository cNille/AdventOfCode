print(chr(27)+'[2j')
print('\033c')
f = open('18.test', 'r')
#f = open('18.input', 'r')
lines = [x.strip() for x in f.readlines()]

print("Day 18")

cubes = set() 
MIN, MAX = 999999999, 0
for l in lines:
    x,y,z = l.split(',')
    x,y,z = (int(x), int(y), int(z))
    cubes.add((x,y,z))
    MIN = min(x,y,z,MIN)
    MAX = max(x,y,z,MAX)

def get_sides(cubes, c):
    x,y,z = c
    sides = 6
    for dz in D:
        n = (x,y,z+dz)
        if n in cubes and n != (x,y,z):
            sides -= 1
    for dy in D:
        n = (x,y+dy,z)
        if n in cubes and n != (x,y,z):
            sides -= 1
    for dx in D:
        n = (x+dx,y,z)
        if n in cubes and n != (x,y,z):
            sides -= 1
    return sides

p1 = 0
D = [-1,1]
for c in cubes:
    p1 += get_sides(cubes, c)

def get_neighbours(cubes, c):
    x,y,z = c
    ns = [
        (x+1,y,z),
        (x-1,y,z),
        (x,y+1,z),
        (x,y-1,z),
        (x,y,z+1),
        (x,y,z-1),
    ]
    ns = [c for c in ns if c not in cubes]
    return set(ns)

p2 = p1
is_pocket = {}
for z in range(MIN,MAX+1):
    for y in range(MIN,MAX+1):
        for x in range(MIN,MAX+1):
            if (x,y,z) in cubes:
                continue
            sides = get_sides(cubes,(x,y,z))
            if sides == 0:
                p2 -= 6
                continue
            ns = get_neighbours(cubes, (x,y,z))
            while (x,y,z) not in is_pocket:
                old_ns = len(ns)
                limit_reached = False
                for n in ns:
                    nx,ny,nz = n
                    x_oob = (MAX < nx or nx < MIN)
                    y_oob = (MAX < ny or ny < MIN)
                    z_oob = (MAX < nz or nz < MIN)
                    if x_oob or y_oob or z_oob: 
                        limit_reached = True
                        continue
                    ns = ns | get_neighbours(cubes,n)
                if limit_reached:
                    for n in ns:
                        is_pocket[n] = False
                    is_pocket[(x,y,z)] = False
                if len(ns) == old_ns: # No new neighbour added
                    for n in ns:
                        is_pocket[n] = True
                    is_pocket[(x,y,z)] = True

            if is_pocket[(x,y,z)]:
                p2 -= (6-sides)

print("Solution part 1:", p1)
print("Solution part 2:", p2)
