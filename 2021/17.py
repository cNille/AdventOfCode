print(chr(27)+'[2j')
print('\033c')
import math
import functools
f = open('17.input', 'r')
testdata = 'target area: x=20..30, y=-10..-5'
inputdata = [x.strip() for x in f.readlines()][0]
data = testdata 
#data = inputdata 

xrange, yrange = data.split(': ')[1].split(', ')
xmin, xmax = map(int, xrange[2:].split('..'))
ymin, ymax = map(int, yrange[2:].split('..'))
outerbound = (xmax, ymin) 

print("Input data: %s" % data)
print('Outerbound:', outerbound)

def step(dx,dy,pos):
    # New pos
    pos = (
        pos[0] + dx,
        pos[1] + dy
    )
    # Drag
    if dx != 0:
        dx += -1 if dx > 0 else 1
    # Gravity
    dy -= 1
    return dx,dy,pos

def is_within(pos):
    global xmin, xmax, ymin, ymax
    x,y = pos
    return xmin <= x <= xmax and ymin <= y <= ymax

matches = []
for dx_initial in range(1,abs(outerbound[0])+1):
    for dy_initial in range(-abs(outerbound[1]),abs(outerbound[1])+1):
        pos = (0,0)
        dx = dx_initial if dx_initial > 0 else -dx_initial
        dy = dy_initial 
        highest = 0
        while pos[0] < outerbound[0] and pos[1] > outerbound[1]:
            dx,dy, pos = step(dx,dy, pos)
            highest = max(highest, pos[1])
            if(is_within(pos)):
                matches.append((dx_initial, dy_initial, highest))
                break

matches = sorted(matches, key =lambda x: x[2])
# print("Found:")
# for m in matches:
#     print("x = %d , y = %d, highest point: %d" % m)

print('---')
print("Highest point reached: %d" % (matches[-1][2]))
print("Total matches: %d" % len(matches))
