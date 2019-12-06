f = open('06.input', 'r')
content = [x.strip() for x in f.readlines()]

# Improvements:
# - Implement function instead of repetitiveness
# - List comprehension and sort at the end
# - Recursive functions?
# - Dequeue and search distance to all.
# - Use networkx.DiGraph
# - Part 2: Traversing the paths in reverse. And calculating how many orbits
#           that are left when they start to differ


# ================================================
# Part 1

orbit = {}
for c in content:
    a, b = c.split(')')
    orbit[b] = a 

count = 0
for o in orbit:
    curr = o
    while curr in orbit:
        count += 1
        curr = orbit[curr]
print("Solution part 1: %d" % count)

# ================================================
# Part 2

orbit = {}
for c in content:
    a, b = c.split(')')
    orbit[b] = a 

you_path = []
curr = "YOU"
while curr in orbit:
    you_path.append(curr)
    curr = orbit[curr]

san_path = []
curr = "SAN"
while curr in orbit:
    san_path.append(curr)
    curr = orbit[curr]

sd = {}
for i, s in enumerate(san_path[1:]):
    sd[s] = i

yd = {}
for i, s in enumerate(you_path[1:]):
    yd[s] = i 

mini = 999999
for s in sd:
    if s in yd:
        res = yd[s] + sd[s]
        mini = res if res < mini else mini

print("Solution part 2: %d" % mini)
