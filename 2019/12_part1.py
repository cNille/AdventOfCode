import re
f = open('12.input', 'r')

# Test
content = [
    '<x=-1, y=0, z=2>',
    '<x=2, y=-10, z=-7>',
    '<x=4, y=-8, z=8>',
    '<x=3, y=5, z=-1>',
]
content = [
    '<x=-8, y=-10, z=0>',
    '<x=5, y=5, z=10>',
    '<x=2, y=-7, z=3>',
    '<x=9, y=-8, z=-3>',
]
content = [x.strip() for x in f.readlines()]

def printpoints(points, step):
    print(step)
    for p in points:
        print(p)

def energy(points):
    return sum(
        [ 
            sum(map(abs,x[:3])) * sum(map(abs,x[3:]))
            for x
            in points
        ]
    )

points = []
for c in content:
    x,y,z = re.findall(r'<x=([-\d]+), y=([-\d]+), z=([\d-]+)>', c)[0]
    points.append((int(x), int(y), int(z), 0,0,0)) 


for i in range(1000):

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
        
   
    printpoints(points, i+1)
print(energy(points))



