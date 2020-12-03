f = open('03.input', 'r')
data = [x.strip() for x in f.readlines()]

def part1(data):
    x = 0
    total = 0
    for i in range(len(data)):
        if data[i][x] == '#':
            total += 1
        x = (x + 3) % len(data[0])
    return total

def part2(data):
    def traverse(right, down):
        x = 0
        total = 0
        for i in range(len(data)):
            if i % down != 0:
                continue
            if data[i][x] == '#':
                total += 1
            x = (x + right) % len(data[0])
        return total

    return traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2)

print "Solution part 1: %d" % part1(data)
print "Solution part 2: %d" % part2(data)


# Alternative solution

def part1functional(data):
    def encountered((idx, row)):
      x_position = (idx * 3) % len(row)
      return row[x_position] == '#'
    trees_encountered = filter(encountered, enumerate(data))
    return len(trees_encountered)
print "Solution part 1: %d" % part1functional(data)

def part2listcomp(data):
    def traverse(right, down):
      # Filter out jumped rows
      rows_hit = [
        r
        for idx, r
        in enumerate(data)
        if idx % down == 0
      ]

      # Filter out rows where we encounter a tree
      trees_encountered = [
        idx 
        for idx, row 
        in enumerate(rows_hit)
        if row[(idx * right) % len(row)] == '#'
      ]
      return len(trees_encountered)

    return traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2)

print "Solution part 2: %d" % part2listcomp(data)
