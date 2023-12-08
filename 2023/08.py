print(chr(27)+'[2j')
print('\033c')
f1 = open('08.input', 'r')
#f2 = open('08.test', 'r')
#f3 = open('08.test2', 'r')
#f4 = open('08.test3', 'r')
lines1 = [x.strip() for x in f1.readlines()]
#lines2 = [x.strip() for x in f2.readlines()]
#lines3 = [x.strip() for x in f3.readlines()]
#lines4 = [x.strip() for x in f4.readlines()]

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print('Day 08')

def solve(lines, part2=False):
    instructions = lines[0] 
    positions = {} 
    curr = []
    for line in lines[2:]:
        node, nxt = line.split(' = ')
        node = node.strip()
        left,right = nxt.strip()[1:-1].split(', ')
        positions[node] = (left, right) 
        if part2 and node[-1] == 'A':
            curr.append(node)
        elif not part2 and node == 'AAA':
            curr.append(node)

    cycles = []
    for node in curr:
        i = 0   
        cycle = 0 
        while cycle == 0:
            instr = instructions[i % len(instructions)]
            if instr == 'L':
                node = positions[node][0]
            elif instr == 'R':
                node = positions[node][1]
            i += 1
            if node.endswith('Z'):
                cycle = i
        cycles.append(cycle)
    # Find the LCM of the cycles
    lcm = cycles[0]
    for i in cycles[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

print('Part 1: %d' % solve(lines1))
print('Part 2: %d' % solve(lines1, part2=True))
#print('Test: %d' % solve(lines2))
#print('Test2: %d' % solve(lines3))
#print('Test3: %d' % solve(lines4, part2=True))
