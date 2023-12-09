print(chr(27)+'[2j')
print('\033c')
f = open('09.input', 'r')
f = open('09.test', 'r')
lines = [x.strip() for x in f.readlines()]

print('Day 09')

def only_zeros(xs):
    for x in xs:
        if x != 0:
            return False
    return True

def solve():
    part1 = 0
    part2 = 0
    for line in lines:
        original_xs = [int(x) for x in line.split()]
        xs = [original_xs.copy()]

        count  = 0
        diff = []
        while not only_zeros(xs[-1]):
            curr = xs[-1]

            # Zip the list with itself, but offset by one
            line_diffs = []
            for x, y in zip(curr, curr[1:]):
                line_diffs.append(y - x)
            xs.append(line_diffs)
            diff.append(line_diffs[-1])

            if count > 100:
                break
            count += 1

        prefix = [0]
        suffix = [0] 
        for x in xs[::-1][1:]:
            prefix.append(x[0] - prefix[-1])
            suffix.append(x[-1] + suffix[-1])

        part1 += suffix[-1] 
        part2 += prefix[-1]

    print('Part 1:', part1)
    print('Part 2:', part2)
solve()


# Refactored with recursion
def predict_next(xs):
    if not any(xs):
        return 0 

    zipped = zip(xs, xs[1:])
    line_diffs = [b - a for a, b in zipped]
    return xs[-1] + predict_next(line_diffs)

def predict_prev(xs):
    if not any(xs):
        return 0 

    zipped = zip(xs, xs[1:])
    line_diffs = [b - a for a, b in zipped]
    return xs[0] - predict_prev(line_diffs)


def refactored(lines):
    part1 = 0
    part2 = 0
    for line in lines:
        xs = [int(x) for x in line.split()]
        part1 += predict_next(xs)
        part2 += predict_prev(xs)


    print('Part 1:', part1)
    print('Part 2:', part2)
refactored(lines)
