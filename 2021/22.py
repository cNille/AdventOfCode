print(chr(27)+'[2j')
print('\033c')
f = open('22.test', 'r')
f = open('22.test2', 'r')
#f = open('22.input', 'r')
data = [x.strip() for x in f.readlines()]

# Import libraries
import matplotlib.pyplot as plt
from collections import deque
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from itertools import product, combinations
  
def show(cubes):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for cube in cubes:
        color = 'green' if cube[0] == 'on' else 'red'
        x,y,z = cube[2:]
        for s, e in combinations(np.array(list(product(x,y,z))), 2):
            if (
                np.sum(np.abs(s-e)) == x[1]-x[0]
                or
                np.sum(np.abs(s-e)) == y[1]-y[0]
                or
                np.sum(np.abs(s-e)) == z[1]-z[0]
            ):
                ax.plot3D(*zip(s, e), color="green")
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
            c1[2][0] < c2[2][0] < c1[2][1]
            or
            c1[2][0] < c2[2][1] < c1[2][1]
        ) and (
            c1[3][0] < c2[3][0] < c1[3][1]
            or
            c1[3][0] < c2[3][1] < c1[3][1]
        ) and (
            c1[4][0] < c2[4][0] < c1[4][1]
            or
            c1[4][0] < c2[4][1] < c1[4][1]
        )
    )

def within(cube, point):
    _, _, (xs, xe), (ys, ye), (zs, ze) = cube
    x,y,z = point
    return xs <= x <= xe and ys <= y <= ye and zs <= z <= ze

def get_all_points(c1):
    _, _, (xs, xe), (ys, ye), (zs, ze) = c1 
    return [ 
        (xs , ys, zs), (xe , ys, zs),
        (xs , ye, zs), (xe , ye, zs),
        (xs , ys, ze), (xe , ys, ze),
        (xs , ye, ze), (xe , ye, ze),
    ]

def intersect_points(c1,c2):
    points = [p for p in get_all_points(c1) if within(c2, p)]
    other = get_all_points(c2)
    points = [p for p in points if p not in other]
    return points 
    
def split(cube, p):
    sx, ex = cube[2]
    sy, ey = cube[3]
    sz, ez = cube[4]
    px, py, pz = p
    return [ 
        (cube[0], cube[1], (sx, px), (sy, py), (sz, pz)),
        (cube[0], cube[1], (px, ex), (sy, py), (sz, pz)),
        (cube[0], cube[1], (sx, px), (py, ey), (sz, pz)),
        (cube[0], cube[1], (px, ex), (py, ey), (sz, pz)),
        (cube[0], cube[1], (sx, px), (sy, py), (pz, ez)),
        (cube[0], cube[1], (px, ex), (sy, py), (pz, ez)),
        (cube[0], cube[1], (sx, px), (py, ey), (pz, ez)),
        (cube[0], cube[1], (px, ex), (py, ey), (pz, ez)),
    ]

def volume(cube):
    (xs, xe), (ys, ye), (zs, ze) = cube[2:]
    return (xe-xs) * (ye-ys) * (ze-zs)

def difference(c1,c2):
    splits = set()
    intersection_point = intersect_points(c2,c1)
    for ip in intersection_point:
        new_splits = split(c1, ip)
        for s in new_splits:
            if volume(s) > 0:
                splits.add(s)
    intersection_point = intersect_points(c1,c2)
    for ip in intersection_point:
        new_splits = split(c2, ip)
        for s in new_splits:
            if volume(s) > 0:
                splits.add(s)
    return splits 


on = set()
cubes = set()
for i, cube in enumerate(data):
    action, area = cube.split(' ')
    xarea, yarea,zarea = area.split(',')
    xrange = tuple(map(int, xarea[2:].split('..')))
    yrange = tuple(map(int, yarea[2:].split('..')))
    zrange = tuple(map(int, zarea[2:].split('..')))
    #xrange = (xrange[0], xrange[1]+1) # Define a cube "until" end.
    #yrange = (yrange[0], yrange[1]+1)
    #zrange = (zrange[0], zrange[1]+1)
    cubes.add((i,action, xrange, yrange, zrange))


#c1 = (1, 'on', (0,10), (0,10), (0,10))
#c2 = (2, 'off', (5,15), (5,15), (5,15))
#cubes = set([c1,c2])

partials = []
not_done = True
itr = 0
while not_done:
    itr+=1
    if itr % 100 == 0:
        print(itr, len(cubes))
    not_done = False
    add = set() 
    rm = None
    #print('='*20)
    #print("Cubes:", len(cubes))
    #for c1 in cubes:
    #    print(c1)
    for i, c1 in enumerate(cubes):
        for j, c2 in enumerate(cubes):
            if c1 == c2:
                continue
            ips = intersect_points(c1, c2)
            if len(ips) > 0 and (c1[2:] != c2[2:]) and c1[1] != c2[1]:
                rm = (c1, c2)
                add = difference(c1, c2)
                #show([c1,c2])
                #print("IPS", len(ips))
                print("Break at ", i,j, "of", len(cubes))
                break
        if rm is not None:
            break
    if rm is not None:
        #print('-'*10)
        #print("RM1:", rm[0])
        #print("RM2:", rm[1])
        #for a in add:
        #    print("Add", a)
        cubes = cubes | add
        cubes.remove(rm[0])
        cubes.remove(rm[1])
        not_done = True
    #show(cubes)

print('='*20)
print("Cubes:", len(cubes))
for c1 in cubes:
    print(c1)
print("LN", len(cubes))
exit()

partials = list(set(cubes))
partials.sort(key=lambda x: x[0])

tot = 0
for p in partials:
    v = volume(p)
    print(tot, p, "\t\t", v if p[1] == 'on' else -v)
    if p[1] == 'on':
        tot += v
    if p[1] == 'off':
        tot -= v
print("Total", tot)
