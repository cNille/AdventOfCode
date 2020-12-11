numbers = [int(x.strip()) for x in open('10.input', 'r').readlines() if x != '']
testnumb = [int(x.strip()) for x in open('10.test', 'r').readlines() if x != '']
numbers = map(int,filter(None, open('10.input', 'r').readlines()))
testnumb = map(int,filter(None, open('10.test', 'r').readlines()))
testnumb2 = map(int,filter(None, open('10.test2', 'r').readlines()))


from collections import defaultdict
def part1(numbers):
    numbers.append(0)
    numbers.append(max(numbers)+3)
    numbers = sorted(numbers)
    count = defaultdict(int)
    for i, n in enumerate(numbers[:-1]):
        diff = numbers[i+1] - n
        if 0 < diff < 4:
            count[diff] += 1
        else:
            print 'nooo'
            break

    res = count[1] * count[3]
    print res

def valid(numbers):
    return [b - a for (a,b) in zip(numbers, numbers[1:])]


def part2(numbers):
    numbers = [0] + sorted(numbers) + [max(numbers) + 3]
    diff = valid(numbers)
    streaks = []
    streak = 0

    test = zip(diff, diff[1:])
    for i in range(len(diff)):
        if diff[i] == 1 and diff[i+1] ==1:
            streak += 1
        else: 
            streaks.append(streak)
            streak = 0
    print streaks

    streaks = []
    streak = 0
    for i, x in enumerate(diff[1:]):
        if x == 1 and diff[i] == 1: # Current and previous have diff 1
            streak += 1
        else: 
            streaks.append(streak)
            streak = 0
    print streaks
    exit()
    translate = { 1: 2, 2: 4, 3: 7 }
    values = [translate[s] for s in streaks if s != 0]
    result = reduce(lambda a, b: a * b, values)
    print result


part2(numbers)
part2(testnumb2)
part2(testnumb)
exit()
