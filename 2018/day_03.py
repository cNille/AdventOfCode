f = open('day_03_input.txt','r')
content = [x.strip() for x in f.readlines()]
import numpy as np

# Calc max-width and max-height
max_width = 0
max_height = 0
for claim in content:
    c = claim.split(' ')
    [left, top] = c[2].replace(':','').split(',')
    [width, height] = c[3].split('x')
    left = int(left)
    top = int(top)
    width = int(width)
    height = int(height)
    max_width = max(left+width, max_width)
    max_height = max(top+height, max_height)
print(max_width, max_height)

matrix = np.zeros((1000,1000))

# Add each inch for every claim
for claim in content:
    c = claim.split(' ')
    [left, top] = c[2].replace(':','').split(',')
    [width, height] = c[3].split('x')
    left = int(left)
    top = int(top)
    width = int(width)
    height = int(height)

    for x in range(width):
        for y in range(height):
            matrix[x+left,y+top] += 1

# Count overlaps
count = 0
for i in range(1000):
    for j in range(1000):
        if matrix[i,j] > 1:
            count +=1
print('Count', count)

# Find no overlap
for claim in content:
    c = claim.split(' ')
    [left, top] = c[2].replace(':','').split(',')
    [width, height] = c[3].split('x')
    left = int(left)
    top = int(top)
    width = int(width)
    height = int(height)

    no_overlap = True
    for x in range(width):
        for y in range(height):
            if matrix[x+left,y+top] > 1:
                no_overlap = False
    if no_overlap:
        print(c[0])
