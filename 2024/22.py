print(chr(27)+'[2j')
print('\033c')
f = open('22.test', 'r')
f = open('22.input', 'r')
f = open('22.test2', 'r')

RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"
LIGHT_BLUE_BG = "\033[104m"

lines = [x.strip() for x in f.readlines()]
secrets = [int(x) for x in lines]

def mix(a,b):
    return a ^ b
assert(mix(42,15) == 37)
def prune(a):
    return a % 16777216 
assert(prune(100000000) == 16113920)



def next_secret(secret):
    result = secret * 64
    new_secret = mix(secret, result)
    new_secret = prune(new_secret)

    result = new_secret // 32
    new_secret = mix(new_secret, result)
    new_secret = prune(new_secret)

    result = new_secret * 2048
    new_secret = mix(new_secret, result)
    new_secret = prune(new_secret)
    return new_secret

secret = next_secret(123)
assert(secret == 15887950)

def daily(secret, size=2000):
    s = [secret]
    for _ in range(size):
        last = s[-1]
        s.append(next_secret(last))
    return s

def get_ends(ns):
    return [
        n % 10
        for n 
        in ns
    ]


def get_changes(changes, ns):
    ends = get_ends(ns)
    seen = set()
    for i in range(4, len(ends)):
        d1 = ends[i-3] - ends[i-4]
        d2 = ends[i-2] - ends[i-3]
        d3 = ends[i-1] - ends[i-2]
        d4 = ends[i-0] - ends[i-1]
        nxt = (d1,d2,d3,d4)
        if nxt in seen:
            continue
        seen.add(nxt)
        if nxt not in changes:
            changes[nxt] = 0
        changes[nxt] += ends[i]
    return changes

part1 = 0
nodes = set()
changes = {}
for i, s in enumerate(secrets):
    ns = daily(s)
    part1 += ns[-1]
    if i % 100 == 0:
        print(f'{i} of {len(secrets)} == {s}: {ns[-1]}')

    changes = get_changes(changes, ns)
    nodes.update(changes.keys())

top = 0
change = (0,0,0,0)
for c in changes: 
    if changes[c] > top:
        top = changes[c]
        change = c

print(f'Part1: {part1}')
print(f'Part2: {top}')
