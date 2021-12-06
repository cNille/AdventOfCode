from collections import defaultdict
# f = open('06.input', 'r')
# lines = [x.strip() for x in f.readlines()]
lines = ['3,4,3,1,2']
timers = lines[0].split(',')
timers = list(map(int, timers))

def part1(timers):
    days = 80
    for i in range(days):
        new_timers = []
        for t in timers:
            if t == 0:
                new_timers.append(8)
                new_timers.append(6)
            else:
                new_timers.append(t - 1)
        timers = new_timers
    return len(timers)
print("Solution part 1: %d" % part1([t for t in timers]))

def part2(timers):
    days = 256 
    mods = [0,0,0,0,0,0,0,0,0] 
    for t in timers:
        mods[t] += 1

    for i in range(days):
        new_mods = [0,0,0,0,0,0,0,0,0]
        for i, m in enumerate(mods):
            if i == 0:
                new_mods[8] += m
                new_mods[6] += m
            else:
                new_mods[i-1] += m
        mods = new_mods
    return sum(mods)
print("Solution part 2: %d" % part2(timers))
