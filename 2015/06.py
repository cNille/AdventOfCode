import numpy as np
data = open('06.input').readlines()

lights = np.zeros((1000,1000))
for i, line in enumerate(data):
    #print("%d %s" % (i, line))
    t = line.strip().split(' ')
    if 'toggle' in line:
        src = t[1]
        des = t[3]
    else:   
        src = t[2]
        des = t[4]

    on_off = 1 if t[1] == 'on' else 0

    x1,y1 = [int(x) for x in src.split(',')]
    x2,y2 = [int(x) for x in des.split(',')]

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if 'toggle' in line:
                lights[x][y] = 1 if lights[x][y] == 0 else 0 
            else:
                lights[x][y] = on_off


count = 0
for a in range(1000):
    for b in range(1000):
        if lights[a][b] == 1:
            count += 1

print("Part 1: %d" % count)

# Part 2
lights = np.zeros((1000,1000))
for i, line in enumerate(data):
    #print("%d %s" % (i, line))

    t = line.strip().split(' ')
    if 'toggle' in line:
        src = t[1]
        des = t[3]
    else:   
        src = t[2]
        des = t[4]

    on_off = 1 if t[1] == 'on' else -1

    x1,y1 = [int(x) for x in src.split(',')]
    x2,y2 = [int(x) for x in des.split(',')]

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if 'toggle' in line:
                lights[x][y] += 2 
            else:
                lights[x][y] += on_off
                lights[x][y] = 0 if lights[x][y] < 0 else lights[x][y]

count = 0
for a in range(1000):
    for b in range(1000):
        count += lights[a][b] 
print("Part 2: %d" % count)
