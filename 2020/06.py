f = open('06.input', 'r')
data = [x.strip() for x in f.readlines()]

from collections import Counter
def part1(data):
    groups = []
    group = ''
    for line in data:
        if line == '':
            groups.append(group)
            group = ''
        else:
                group += line
    total = 0
    for g in groups:
        total +=len(Counter(g).keys())
    return total

def part2(data):
    group = []
    total = 0
    for line in data:
        if line == '':
            oneline = "".join(group)
            unique = Counter(oneline)
            for u in unique:
                if unique[u] == len(group):
                    total += 1
            group = []
        else:
            group.append(line)
    return total

print "Solution part 1: %d" % part1(data)
print "Solution part 2: %d" % part2(data)
