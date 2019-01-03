# Import data
data = [line.strip() for line in open('25.in', 'r').readlines()]
points = [map(int, line.split(',')) for line in data]

constellations = []


def within_range(p1, p2):
    return sum([abs(a - b) for (a, b) in zip(p1, p2)]) <= 3


for p in points:
    constellation_found = False
    added = -1
    to_rm = []

    for i in range(len(constellations)):
        c = constellations[i]
        within_c = len([x for x in c if within_range(p, x)]) > 0

        if within_c and added >= 0:
            constellations[added] += constellations[i]
            to_rm.append(i)

        elif within_c:
            constellation_found = True
            constellations[i].append(p)
            added = i

    for rm in to_rm:
        del constellations[rm]

    if not constellation_found:
        constellations.append([p])

print('Part 1 solution: %d' % len(constellations))
