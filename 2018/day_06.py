import datetime
import operator
import re

# Import data
data = [x.strip() for x in open('day_06_input.txt','r').readlines()]
points = [x.split(', ') for x in data]
points = [(int(x[0]), int(x[1])) for x in points]

x = [p[0] for p in points]
y = [p[1] for p in points]
max_x = max(x)
max_y = max(y)
min_x = min(x)
min_y = min(y)

# Plot on graph
# import matplotlib.pyplot as plt
# plt.scatter(x, y)
# plt.title("Scatter Plot")
# plt.show()
# exit()

def sort_dic_by_values(d):
    return sorted(d.items(), key=operator.itemgetter(1))

def distance(p,x,y):
    return abs(x - p[0]) + abs(y - p[1])

areas = {}
min_x = min_x - 1
min_y = min_y - 1
max_x = max_x + 1
max_y = max_y + 1
within_range = 0
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        distances = {}
        for p in points:
            distances[p] = distance(p,x,y)

        # --------
        # Part B
        sum_dist = sum([distances[d] for d in distances])
        if sum_dist < 10000:
            within_range += 1
        # --------

        d = sort_dic_by_values(distances)
        if d[0][1] == d[1][1]: # Check for equal distances
            continue
        min_p = d[0][0]
        if min_p not in areas:
            areas[min_p] = []
        areas[min_p].append((x,y))

for p in areas:
    for (x,y) in areas[p]:
        if (x == min_x     or
            x == max_x - 1 or
            y == min_y     or
            y == max_y - 1 ):
            areas[p] = None
            break;

l = {}
for p in areas:
    if areas[p] is not None:
        l[p] = len(areas[p])

print('Part A: Winning area:', sort_dic_by_values(l)[-1])
print('Part B, amount within range:', within_range)
