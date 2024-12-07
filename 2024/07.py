print(chr(27)+'[2j')
print('\033c')
f = open('07.input', 'r')
f = open('07.test', 'r')
lines = [x.strip() for x in f.readlines()]

def part1(value, xs):
    if len(xs) == 1:
        return value == xs[0]
    rest = xs[2:]

    mul = [xs[0]*xs[1]] + rest 
    if part1(value, mul):
        return True
    add = [xs[0]+xs[1]] + rest 
    if part1(value, add):
        return True
    return False

def part2(value, xs):
    if len(xs) == 1:
        return value == xs[0]
    rest = xs[2:]

    mul = [xs[0]*xs[1]] + rest 
    if part2(value, mul):
        return True
    add = [xs[0]+xs[1]] + rest 
    if part2(value, add):
        return True
    concat = [int(str(xs[0])+str(xs[1]))] + rest
    if part2(value, concat):
        return True
    return False

result1 = 0
result2 = 0
for line in lines:
    value, parts = line.split(':')
    value = int(value.strip())
    parts = [int(x) for x in parts.split()] 
    if part1(value, parts):
        result1 += value
    if part2(value, parts):
        result2 += value
print("Solution part 1:", result1)
print("Solution part 2:", result2)
