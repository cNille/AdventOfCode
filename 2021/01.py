# f = open('01.test', 'r')
f = open('01.input', 'r')
content = [x.strip() for x in f.readlines()]
depths = [int(x) for x in content]

def part1():
    prev = depths[0]
    count = 0
    for x in depths[1:]:
        if x > prev:
            count += 1
        prev = x
    return count

def part1_minimal():
    return sum([
        a < b 
        for a,b 
        in zip(depths, depths[1:])
    ])

result1 = part1()
result1 = part1_minimal()
print("Part 1 solution: %d" % result1)

def part2():
    prev = 99999
    count = 0
    for i in range(len(depths) - 2):
        a,b,c = depths[i:i+3]
        current = a + b + c
        if current > prev:
            count += 1
        prev = current 
    return count

def part2_func():
    sums = [a+b+c for (a,b,c) in zip(depths, depths[1:], depths[2:])]
    increases = [1 for (a,b) in zip(sums, sums[1:]) if b > a]
    return len(increases)

# When comparing a sliding window of 3 we actually only need to compare 
# depths[i] with depths[i+3]. As the two other numbers in the window are
# identical. i.e:
# window 0:  0 1 2
# window 1:    1 2 3
def part2_minimal():
    increases = [a < b for a,b in zip(depths, depths[3:])]
    return sum(increases)

result2 = part2()
result2 = part2_func()
result2 = part2_minimal()
print("Part 2 solution: %d" % result2)
