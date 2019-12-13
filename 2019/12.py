import re
f = open('12.input', 'r')

# Test
content = [x.strip() for x in f.readlines()]
content = [ '<x=-8, y=-10, z=0>', '<x=5, y=5, z=10>', '<x=2, y=-7, z=3>', '<x=9, y=-8, z=-3>' ]
content = [ '<x=-1, y=0, z=2>', '<x=2, y=-10, z=-7>', '<x=4, y=-8, z=8>', '<x=3, y=5, z=-1>' ]

def printpoints(points, step):
    print(step)
    for p in points:
        print(p)

def energy(points):
    kinetic = [sum(map(abs,x[:3])) for x in points]
    potential = [sum(map(abs,x[3:])) for x in points]
    total = sum([ k*p for k,p in zip(kinetic, potential)])
    #print(kinetic, potential, sum(kinetic), sum(potential), total)
    print(sum(kinetic), sum(potential), total, points)
    return total
    #return sum(
    #    [ 
    #        sum(map(abs,x[:3])) * sum(map(abs,x[3:]))
    #        for x
    #        in points
    #    ]
    #)

initial_points = []
for c in content:
    x,y,z = re.findall(r'<x=([-\d]+), y=([-\d]+), z=([\d-]+)>', c)[0]
    initial_points.append((int(x), int(y), int(z), 0,0,0)) 
points = initial_points


def round(points):
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
    points = new_points
    #printpoints(points, i+1)
    return points

# origin = (0,0,0)
# def round_smart(points):
#     new_points = []
#     for m1 in points:
#         dx, dy, dz = 0,0,0
#         for m2 in points:
#             if m1 == m2:
#                 continue
#             dx = m2[0] - m1[0]
#             dy = m2[1] - m1[1]
#             dz = m2[2] - m1[2]
# 
#         new_point = (
#             m1[0] + dx ,
#             m1[1],
#             m1[2],
#             m1[3] + dx,
#             m1[4] + dy,
#             m1[5] + dz,
#         )
#         new_points.append(new_point)
#     points = new_points
#     #printpoints(points, i+1)
#     return points
        

energy(points)
for i in range(2800):
    print(i)
    points = round(points)
    energy(points)
#print("Part 1:", energy(points))
exit()

def get_pos(p):
    return [x[:3] for x in p]
def get_vel(p):
    return [x[3:] for x in p]
def is_zero(points):
    vel = get_vel(points)
    for x,y,z in vel:
        if x != 0 or y != 0 or z != 0:
            return False
    return True
        
def equalstart(points):
    for i, p in enumerate(points):
        if p != initial_points[i]:
            return False
    return True


print("Points", points)


points = round(points)
count = 1

count, points = (283000000, [(511, 116, -260, 23, 16, -17), (-39, 196, -361, 17, 34, -4), (-99, -217, 846, 14, -24, 28), (-367, -69, -222, -54, -26, -7)]) 

while not equalstart(points):
    count += 1
    points = round(points)
    print(count, energy(points))
    if count % 1000000 == 0:
        print(count, points, energy(points))
points = round(points)
print("should be same", points)

