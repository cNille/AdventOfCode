print(chr(27)+'[2j')
print('\033c')
f = open('22.input', 'r')
f = open('22.test', 'r')
f = open('22.test2', 'r')
data = [x.strip() for x in f.readlines()]
data = data[:-2]


# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from itertools import product, combinations
  
def show(cubes):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for cube in cubes:
        color = 'green' if cube[0] == 'on' else 'red'
        x,y,z = cube[1:]
        for s, e in combinations(np.array(list(product(x,y,z))), 2):
            if (
                np.sum(np.abs(s-e)) == x[1]-x[0]
                or
                np.sum(np.abs(s-e)) == y[1]-y[0]
                or
                np.sum(np.abs(s-e)) == z[1]-z[0]
            ):
                ax.plot3D(*zip(s, e), color="green")
    #ax.voxels(data, facecolors=colors)
    plt.show()

def clamp(x, minimum, maximum):
    a,b = x
    # fully_outside = (a < minimum and b < minimum) or (a > maximum and b > maximum)
    # if fully_outside:
    #     return None
    return (
        max(min(a, maximum), minimum),
        max(min(b, maximum), minimum),
    )


def cubes_intersect(c1,c2):
    return  (
        (  
            c1[1][0] < c2[1][0] < c1[1][1]
            or
            c1[1][0] < c2[1][1] < c1[1][1]
        ) and (
            c1[2][0] < c2[2][0] < c1[2][1]
            or
            c1[2][0] < c2[2][1] < c1[2][1]
        ) and (
            c1[3][0] < c2[3][0] < c1[3][1]
            or
            c1[3][0] < c2[3][1] < c1[3][1]
        )
    )

def get_ranges(x1,x2):
    ranges = [
        (x1[0], x2[0]),
        (x2[0] + 1, x2[1]),
        (x2[1] + 1, x1[1]) if x2[1] != x1[1] else (x2[1], x1[1])
    ]
    ranges = [(a,b) for (a,b) in ranges if a != b]
    return ranges

def difference(c1,c2, second=False):
    action1 = c1[0]
    action2 = c2[0]
    x1,y1,z1 = c1[1:]
    x2,y2,z2 = c2[1:]
    x2 = clamp(x2, x1[0], x1[1])
    y2 = clamp(y2, y1[0], y1[1])
    z2 = clamp(z2, z1[0], z1[1])
    #print(x1,y1,z1)
    #print(x2,y2,z2)
    xranges = get_ranges(x1,x2)
    yranges = get_ranges(y1,y2)
    zranges = get_ranges(z1,z2)
    cubes = []
    for z in zranges: 
        for y in yranges:
            for x in xranges:
                if x == x2 and y == y2 and z == z2:
                    # Skip c2
                    continue
                cubes.append((action1, x,y,z))
    if not second:
        other = difference(c2, c1, True)
        #print('c1', c1)
        #print('c2', c2)
        #print('--- other')
        #for o in other:
        #    print(o)
        #print('--- cubes')
        #for o in cubes:
        #    print(o)
        cubes.append((c2[0], x2,y2,z2))
        for o in other:
            cubes.append(o)

        # print('----Difference')
        # print('c1', c1)
        # print('c2', c2)
        # print('--- cubes')
        # for o in cubes:
        #     print(o)
    return cubes


from collections import deque
def part2(data):
    on = set()
    cubes = []
    for cube in data:
        action, area = cube.split(' ')
        xarea, yarea,zarea = area.split(',')
        xrange = tuple(map(int, xarea[2:].split('..')))
        yrange = tuple(map(int, yarea[2:].split('..')))
        zrange = tuple(map(int, zarea[2:].split('..')))
        cubes.append((action, xrange, yrange, zrange))

    cubes = deque(cubes)
    i = 0
    while len(cubes) > 0:
        c1 = cubes.pop()
        count = 0
        to_remove = []
        to_add = []
        added_cubes = deque(on)
        while len(added_cubes) > 0:
            c2 = added_cubes.pop()
            if cubes_intersect(c1,c2):
                count += 1
                # print("---")
                # print("Overlap count %d" % count)
                # print(c1)
                # print(c2)
                # print("---")
                on.remove(c2)
                partials = difference(c1,c2)
                cubes.extendleft(partials)
                break
        if count == 0:
            #if len(on) > 10:
            #    print('show')
            #    show(on)
            #    exit()
            if c1[0] == 'on':
                on.add(c1)

            i += 1
            if i % 1000 == 0:
                print('Done with a cube. Left: %d, On: %d' % (len(cubes), len(on)))
                total = 0
                for c in on:
                    if c[0] == 'off':
                        continue
                    x,y,z = c[1:]
                    dx = x[1] - x[0]
                    dy = y[1] - y[0]
                    dz = z[1] - z[0]
                    total += (dx * dy * dz)
                print('TOTAL', total)

    total = 0
    for c in on:
        if c[0] == 'off':
            continue
        x,y,z = c[1:]
        dx = x[1] - x[0]
        dy = y[1] - y[0]
        dz = z[1] - z[0]
        total += (dx * dy * dz)
    print('TOTAL', total)



part2(data)





exit()

def clamp1(x, minimum, maximum):
    a,b = x
    fully_outside = (a < minimum and b < minimum) or (a > maximum and b > maximum)
    if fully_outside:
        return None
    return (
        max(min(a, maximum), minimum),
        max(min(b, maximum), minimum),
    )




def part1(data):
    on = set()
    for cube in data:
        action, area = cube.split(' ')
        xarea, yarea,zarea = area.split(',')
        xrange = tuple(map(int, xarea[2:].split('..')))
        yrange = tuple(map(int, yarea[2:].split('..')))
        zrange = tuple(map(int, zarea[2:].split('..')))
        xrange = clamp1(xrange, -50, 50)
        yrange = clamp1(yrange, -50, 50)
        zrange = clamp1(zrange, -50, 50)
        if not xrange or not yrange or not zrange:
            continue

        count = 0
        if action =='on':
            for z in range(zrange[0], zrange[1] + 1):
                for y in range(yrange[0], yrange[1] + 1):
                    for x in range(xrange[0], xrange[1] + 1):
                        if (x,y,z) not in on:
                            on.add((x,y,z))
                            count += 1
        else: 
            for z in range(zrange[0], zrange[1] + 1):
                for y in range(yrange[0], yrange[1] + 1):
                    for x in range(xrange[0], xrange[1] + 1):
                        if (x,y,z) in on:
                            on.remove((x,y,z))
                            count += 1
    print('Solution part 1: %d' % len(on))
# part1(data)
