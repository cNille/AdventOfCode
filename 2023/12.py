import sys
from functools import lru_cache
sys.setrecursionlimit(50000)
print(chr(27)+'[2j')
print('\033c')
f = open('12.input', 'r')
#f = open('12.test', 'r')
lines = [x.strip() for x in f.readlines()]

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'


@lru_cache(maxsize=None)
def solve(line: str):
    condition, springs = line.split(' ')
    springs = springs.strip().split(',') if springs.strip() else []
    if len(springs) == 0:
        if '#' not in condition:
            return 1
        else:
            return 0
    if len(condition) == 0:
        return 0
    if condition[-1] != '.':
        condition += '.'
    springs = list(map(lambda x: int(x), springs))

    result = 0
    if condition[0] == '#' or condition[0] == '?':
        length = springs[0]
        long_enough = length <= len(condition)
        no_dot = '.' not in condition[:length]
        no_nxt = length < len(condition) and condition[length] != '#'
        if no_dot and long_enough and no_nxt:
            c = condition[length+1:]
            springs_str = ",".join(map(str, springs[1:]))
            r = solve(c + " " + springs_str)
            result += r
    if condition[0] == '.' or condition[0] == '?':
        springs_str = ",".join(map(str, springs))
        r = solve(condition[1:] + " " + springs_str)
        result += r

    return result


def unfold(line: str):
    conditions, springs = line.split()
    return"?".join([conditions]*5) + " " + ",".join([springs]*5)


def solve2(line: str):
    return solve(unfold(line))


# assert(solve('?#?#?#?#?#?#?#? 1,3,1,6') == 1)
# assert(solve('?###???????? 3,2,1') == 10)
# assert(solve('???.### 1,1,3') == 1)
# assert(solve('') == 4)
# assert(solve('????.#...#... 4,1,1') == 1)
# assert(solve('????.######..#####. 0,6,5') == 4)
# assert(solve2('?#?#?#?#?#?#?#? 1,3,1,6') == 1)
# assert(solve2('???.### 1,1,3') == 1)
# assert(solve2('????.#...#... 4,1,1') == 16)
# assert(solve2('????.######..#####. 1,6,5') == 2500)
# assert(solve2('.??..??...?##. 1,1,3') == 16384)
# assert(solve2('?###???????? 3,2,1') == 506250)

total = 0
for i, line in enumerate(lines):
    res = solve2(line)
    total += res
print("Total:", total)
