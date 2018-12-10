import matplotlib.pyplot as plt
import sys

# Import data
data = [x.strip() for x in open('day_10_input.txt','r').readlines()]

points = []
for line in data:
    p_x = int(line[10:16])
    p_y = int(line[18:24])
    v_x = int(line[36:38])
    v_y = int(line[40:42])
    points.append([p_x, p_y, v_x, v_y])

graph_size = [sys.maxint, sys.maxint]
getting_smaller = True
iteration = 0
while getting_smaller:
    min_x = sys.maxint
    min_y = sys.maxint
    max_x = 0
    max_y = 0
    for i in range(len(points)):
        points[i][0] += points[i][2]
        points[i][1] += points[i][3]
        min_x = min(points[i][0], min_x)
        min_y = min(points[i][1], min_y)
        max_x = max(points[i][0], max_x)
        max_y = max(points[i][1], max_y)

    delta_x = abs(max_x - min_x)
    delta_y = abs(max_y - min_y)

    getting_smaller = delta_x <= graph_size[0] and delta_y <= graph_size[1]
    graph_size[0] = delta_x
    graph_size[1] = delta_y

# Part 2
print('Iteration : %d' % (iteration-1))

# Part 1
for i in range(len(points)):
    points[i][0] -= points[i][2]
    points[i][1] -= points[i][3]
x = [p[0] for p in points]
y = [p[1] for p in points]
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.ylim(150,250)
plt.show(block=True)
