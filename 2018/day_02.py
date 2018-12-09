f = open('day_02_input.txt','r')
content = [x.strip() for x in f.readlines()]

# Part 1
two = 0
three = 0
for row in content:
    twos = [1 for l in row if row.count(l) == 2]
    threes = [1 for l in row if row.count(l) == 3]
    if len(twos) > 0:
        two += 1
    if len(threes) > 0:
        three += 1
print('Part 1 result: %d' % (two * three))

# Part 2
for row in content:
    for row2 in content:
        z = zip(row, row2)
        common = [x[0] for x in z if x[0] == x[1]]
        if len(z) - len(common) == 1:
            print('Part 2 result: %s' % ''.join(common))
            exit()
