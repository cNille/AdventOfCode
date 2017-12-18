from collections import Counter

data = open('my.input').read().split()[0].split(',')

path = []
max_dist = 0

for d in data:
    path.append(d)

    counter = Counter(path)
    deltaN = abs(counter['n'] - counter['s'])
    deltaNe = abs(counter['ne'] - counter['sw'])
    deltaNw = abs(counter['nw'] - counter['se'])
    currDistance = deltaN + max(deltaNw, deltaNe)

    max_dist = max(max_dist, currDistance)

print(max_dist)

