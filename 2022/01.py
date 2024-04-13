f = open('01.input', 'r')
content = [x.strip() for x in f.readlines()]
calories = [int(x) if x != '' else 0 for x in content]

def part1():
    prev = calories[0]
    count = 0
    max_calories = 0
    for x in calories[1:]:
        if prev == 0:
            count = 0
        count += x
        
        max_calories = count if count > max_calories else max_calories
        prev = x
    return max_calories

result1 = part1()
print("Part 1 solution: %d" % result1)

def part2():
    prev = calories[0]
    count = 0

    score = []
    for x in calories[1:]:
        if prev == 0:
            score.append(count)
            count = 0
        count += x
        prev = x
    
    score = sorted(score)
    three_sum = sum(score[-3:])
    return three_sum

result2 = part2()
print("Part 2 solution: %d" % result2)
