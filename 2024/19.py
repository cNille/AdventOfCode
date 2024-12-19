from functools import cache
print(chr(27)+'[2j')
print('\033c')
f = open('19.test', 'r')
f = open('19.input', 'r')

towels, designs = f.read().split('\n\n')

towels = set([x.strip() for x in towels.split(',')])
designs = designs.strip().split('\n')

print(towels)

@cache
def verify(d):
    if len(d) < 1:
        return 0 
    is_valid = 0 
    if d in towels:
        is_valid += 1
    for i in range(1, len(d)):
        l, r = d[:i], d[i:]
        if l not in towels:
            continue
        r = verify(r)
        if l and r:
            add = r
            is_valid += add 
    return is_valid

part1 = 0
part2 = 0
for d in designs:
    v = verify(d)
    print(f'Design {d}: {v}')
    if v:
        part1 += 1 
        part2 += v

print('Result', part1)
print('Result', part2)
