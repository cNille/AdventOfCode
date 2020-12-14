from collections import defaultdict
import re
lines = [x.strip() for x in open('14.input', 'r').readlines() if x != '']

def maskvalue(mask, number):
    b = list(bin(number)[2:])
    for i, x in enumerate(mask[::-1]):
        if i >= len(b):
            b.insert(0, x if x != 'X' else '0')
        if x != 'X':
            b[-i-1] = x
    return int("".join(b), 2)

mem = defaultdict(int)
def part1(lines):
    for line in lines:
        if 'mask' in line:
            mask = line.split()[2]

        if 'mem' in line:
            register, value = map(int, re.match(r'mem\[(\d+)\] = (\d+)', line).groups())
            mem[int(register)] = maskvalue(mask, value)
    print "Solution part 1: %d" % sum(mem.values())
part1(lines)

mem = defaultdict(int)
def get_registers(mask, register):
    b = list(bin(register)[2:])
    for i, x in enumerate(mask[::-1]):
        if i >= len(b):     # Need to iterate whole mask in search of '1' and 'X'
            b.insert(0, x)
        if x != '0':
            b[-i-1] = x

    while b[0] == '0': # Clean from unnecessary zeros at beginning
        b.pop(0)

    def create_registers(bstring):
        if len(bstring) == 0:
            return ['']
        tails = create_registers(bstring[1:])
        if bstring[0] == 'X':
            # Create versions where X is 1 and where X is 0
            return ['1' + t for t in tails] + ['0' + t for t in tails]
        else:
            return [bstring[0] + t for t in tails]
    return [int("".join(r), 2) for r in create_registers(b)] 

def part2(lines):
    for line in lines:
        if 'mask' in line:
            mask = line.split()[2]

        if 'mem' in line:
            register, value = map(int, re.match(r'mem\[(\d+)\] = (\d+)', line).groups())
            for r in get_registers(mask, register):
                mem[int(r)] = value
    print "Solution part 2: %d" % sum(mem.values())
part2(lines)
