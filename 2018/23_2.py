import re
# Part 2

# https://www.reddit.com/r/adventofcode/comments/a8s17l/2018_day_23_solutions/ecdbux2?utm_source=share&utm_medium=web2x&context=3
# Using Z3

# https://www.reddit.com/r/adventofcode/comments/a8s17l/2018_day_23_solutions/ecdqzdg?utm_source=share&utm_medium=web2x&context=3
# Using overlaps and sorting edges

# Load data
DATA = [line.strip() for line in open('23.in', 'r').readlines()]

# Generate Bots
bots = []
for line in DATA:
    # Line format: "pos=<-33124555,22143443,77789621>, r=85920143"
    s = line.split("=")
    x,y,z = s[1][1:-4].split(',')
    r = s[2]
    b = (x,y,z,r)
    bots.append(map(int, b))

# Alternatively we could use priorityqueue
queue = []
for x,y,z,r in bots:
    center = abs(x) + abs(y) + abs(z)
    lower_bound = center - r
    upper_bound = center + r + 1

    queue.append((max(0, lower_bound), 1))
    queue.append((upper_bound, -1))

# Sort bounds according to distance.
queue.sort(key= lambda x: x[0])

count = 0
maxCount = 0
result = 0
for q in queue:
    distance, bound = q

    # Decrease for lower_bound, increment for upper_bound
    count += bound

    if count > maxCount:
        # New max found
        result = distance
        maxCount = count
print(result)
