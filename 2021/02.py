f = open('02.input', 'r')
instr = [x.strip() for x in f.readlines()]

def part1():
    x = y = 0
    for line in instr:
        comm, steps = line.split(' ')
        steps = int(steps)
        if comm == 'forward':
            x += steps
        if comm == 'down':
            y += steps
        if comm == 'up':
            y -= steps
    result = x * y
    print("Solution part 1: %d" % result)
part1()

def part2():
    x = aim = y = 0
    for line in instr:
        comm, steps = line.split(' ')
        steps = int(steps)

        if comm == 'forward':
            x += steps
            y += aim * steps
        if comm == 'down':
            aim += steps
        if comm == 'up':
            aim -= steps

    result = x * y
    print("Solution part 2: %d" % result)
part2()
