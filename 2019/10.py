from fractions import gcd
data = [x.strip() for x in open('10.input', 'r').readlines()]

asteroids = []
for row, d in enumerate(data):
    for col, c in enumerate(d):
        if c == '#':
            asteroids.append((col,row))

# Part 1
looky = []
best_count = 0
for x,y in asteroids:
    deltas = []
    for a,b in asteroids:
        dx, dy = (a-x, b-y)
        if dx == 0 and dy == 0:
            continue
        divi = abs(gcd(dx,dy))
        A,B = (dx/divi, dy/divi)
        deltas.append((A, B))
    can_see = len(set(deltas))
    looky.append(can_see)
    if can_see > best_count:
        best_count = can_see
        best = (x,y)
    
looky.sort()
print("Part 1 solution: %d" % looky[-1])


# Part 2
print(best)
X = best 
looky = []
deltas = []
for a,b in asteroids:
    x,y = X
    dx, dy = (a-x, b-y)
    if dx == 0 and dy == 0:
        continue
    divi = abs(gcd(dx,dy))
    deltas.append((dx/divi, dy/divi))

count = {}
for d in deltas:
    if d not in count:
        count[d] = []
    count[d].append(d)

right_count = {}
left_count = {}
for c in count:
    if c[0] == 0:
        print("On same X line", c)
    if c[0] > 0:
        right_count[c] = count[c]
    if c[0] < 0:
        left_count[c] = count[c]

def kill_side(counts, reverse):
    direction = counts.keys() 
    direction = sorted(direction, key= lambda (x,y): (1.0*y)/x, reverse=reverse)
    for d in direction:
        kills.append(counts[d].pop())

kills = [(0,1)] # Figured it out by print above
kill_side(right_count, True)
kills.append((0,-1)) # Figured it out by print above
kill_side(left_count, False)

a,b = kills[199]
x,y = X
a,b = a+x, b+y
res = a*100 + b
print("Part 2 solution: %d " % res)

