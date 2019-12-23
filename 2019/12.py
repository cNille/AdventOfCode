import re
import numpy as np
f = open('12.input', 'r')

# Test
content = [x.strip() for x in f.readlines()]

def energy(points):
    kinetic = [sum(map(abs,x[:3])) for x in points]
    kin = sum(map(abs,points[1][:3]))
    potential = [sum(map(abs,x[3:])) for x in points]
    pot = sum(map(abs,points[1][3:]))
    total = sum([ k*p for k,p in zip(kinetic, potential)])
    tot = pot * kin
    return total

initial_points = []
for c in content:
    x,y,z = re.findall(r'<x=([-\d]+), y=([-\d]+), z=([\d-]+)>', c)[0]
    initial_points.append((int(x), int(y), int(z), 0,0,0)) 
points = initial_points

i = 0
def round(points):
    global i
    i +=1
    # Calculate new velocity
    new_points = []
    for m1 in points:
        dx, dy, dz = 0,0,0
        for m2 in points:
            if m1 == m2:
                continue
            dx += 0 if m1[0] == m2[0] else 1 if m1[0] < m2[0] else -1
            dy += 0 if m1[1] == m2[1] else 1 if m1[1] < m2[1] else -1
            dz += 0 if m1[2] == m2[2] else 1 if m1[2] < m2[2] else -1

        new_point = (
            m1[0],
            m1[1],
            m1[2],
            m1[3] + dx,
            m1[4] + dy,
            m1[5] + dz,
        )
        new_points.append(new_point)
    points = new_points

    # Calculate new position
    new_points = []
    for m1 in points:
        new_point = (
            m1[0] + m1[3],
            m1[1] + m1[4],
            m1[2] + m1[5],
            m1[3],
            m1[4],
            m1[5],
        )
        new_points.append(new_point)
    return new_points


for i in range(1000):
    points = round(points)
    energy(points)
print "Part 1: %d" % energy(points)

energy(points)
points = round(points)
energy(points)
count = 0
x_round = None
y_round = None
z_round = None
xseen = None
yseen = None
zseen = None

while True:
    points = round(points)
    x = tuple((x[0], x[3]) for x in points)
    if x == xseen:
        if x_round == None:
            x_round = count 
    elif xseen == None:
            xseen = x

    y = tuple((y[1], y[4]) for y in points)
    if y == yseen:
        if y_round == None:
            y_round = count
    elif yseen == None:
            yseen = y

    z = tuple((z[2], z[5]) for z in points)
    if z == zseen:
        if z_round == None:
            z_round = count
    elif zseen == None:
            zseen = z

    if x_round != None and y_round != None and z_round != None:
        res = np.lcm.reduce([x_round, y_round, z_round])
        print "Part 2: %d " % res
        exit()
    count += 1
