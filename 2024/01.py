f = open('01.input', 'r')
#f = open('01.test', 'r')
content = [x.strip() for x in f.readlines()]
rows = [str(x) if x != '' else '' for x in content]

def part1():
    xs = []
    ys = []

    for line in rows:
        a,b = line.split()
        xs.append(int(a))
        ys.append(int(b))    
    xs.sort()
    ys.sort()

    tot = 0
    for i, x in enumerate(xs):
        tot += abs(ys[i] - x)

    return tot

result1 = part1()
print("Part 1 solution: %d" % result1)

def part2():
    xs = []
    ys = []

    for line in rows:
        a,b = line.split()
        xs.append(int(a))
        ys.append(int(b))    

    tot = 0
    for x in xs: 
        sim = 0

        for y in ys:
            if y == x:
                sim += 1

        score = x * sim
        tot += score

    return tot

result2 = part2()
print("Part 2 solution: %d" % result2)
