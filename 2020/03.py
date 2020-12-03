f = open('03.input', 'r')
data = [x.strip() for x in f.readlines()]

def part1(data):
    x = 0
    total = 0
    for i in range(len(data)):
        char = data[i][x]
        if char == '#':
            total += 1
        x = (x + 3) % len(data[0])
    return total

def part2(data):
    def traverse(slope, down):
        x = 0
        total = 0
        for i in range(len(data)):
            if i % down != 0:
                continue
            char = data[i][x]
            if char == '#':
                total += 1
            x = (x + slope) % len(data[0])
        return total
    return traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2) 

print "Solution part 1: %d" % part1(data)
print "Solution part 2: %d" % part2(data)
