# Import data
data = [x.strip() for x in open('day_10_input.txt','r').readlines()]

min_x = 10000
min_y = 10000
max_x = 10000
max_y = 10000

points = []
for line in data:
    p_x = int(line[10:16])
    p_y = int(line[18:24])
    v_x = int(line[36:38])
    v_y = int(line[40:42])
    min_x = min(p_x, min_x)
    min_y = min(p_y, min_y)
    max_x = max(p_x, max_x)
    max_y = max(p_y, max_y)
    points.append([p_x, p_y, v_x, v_y])


print('MinMax', min_x, min_y, max_x, max_y)

for i in range(10):
    print(points[i])

print('Type "y" to get next...')
# y = ''
# nxt = input()
# print(nxt, ':', y)
# while nxt == 'y':
import matplotlib.pyplot as plt

curr= 0

graph_size = [99999,99999]

while curr < 20000000:
    # Plot on graph

    if curr > 10100 :
        print(curr)
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        plt.scatter(x, y)
        plt.title("Scatter Plot")
        plt.ylim(150,250)
        plt.show(block=True)
        plt.pause(0.1)
        plt.close()
        for i in range(len(points)):
            points[i][0] += points[i][2] * 0.1
            points[i][1] += points[i][3] * 0.1

    else:
        for i in range(len(points)):
            points[i][0] += points[i][2]
            points[i][1] += points[i][3]

            for p in points:
                min_x = min(p[0], min_x)
                min_y = min(p[1], min_y)
                max_x = max(p[0], max_x)
                max_y = max(p[1], max_y)
            delta_x = max_x - min_x
            delta_y = max_y - min_Y

            getting_smaller = delta_x < graph_size[0] and delta_y < graph_size[1]

    curr += 1
    #nxt = input()

# Wrong: GPEPPEJ
# Wrong: JEPPEPG
# Wrong: JEPPPEPG
# Correct: GPEPPPEJ

# Part 2:
# Wrong: 10100
# Test: 10101
