import math

road = open('my.input').read().split('\n')
road = [list(x) for x in road]
letters = []
delta = 1
going_vertical = True

for idx,item in enumerate(road[0]):
    if item == "|":
        [x, y] = (0, idx)
        break

count = 0
while True:
    count +=1
    if going_vertical:
        x += delta
    else:
        y += delta
    
    if road[x][y] == ' ':
        print('Road ended at',x,y)
        break

    if road[x][y] == '+':
        if going_vertical:
            if road[x][y-1] == '-':
               delta = -1 
            if road[x][y+1] == '-':
               delta = 1 
        else:
            if x-1 > 1 and road[x-1][y] == '|':
               delta = -1 
            if x+1 < len(road) - 1 and road[x+1][y] == '|':
               delta = 1 
        going_vertical = not going_vertical
        continue
        
    if road[x][y] != '|' and road[x][y] != '-':
        letters.append(road[x][y])

print('Steps', count)
