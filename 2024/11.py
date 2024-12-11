print(chr(27)+'[2j')
print('\033c')
f = open('11.test', 'r')
#f = open('11.test2', 'r')
#f = open('11.input', 'r')
lines = [x.strip() for x in f.readlines()]

stones: list[str] = []
for line in lines:
    for stone in line.split():
        stones.append(stone)

cache = {}
def split(stone: str, level: int) -> int:
    if (stone, level) in cache:
        return cache[(stone, level)]
    if level == 0:
        cache[(stone, level)] = 1
        return 1

    next_level = level - 1
    res = 0
    if stone == '0':
        res = split('1', next_level)
    elif len(stone) % 2 == 0:
        half = len(stone)//2
        left = str(int(stone[:half]))
        right = str(int(stone[half:]))
        res = split(left, next_level) + split(right, next_level)
    else:
        new_s = int(stone) * 2024
        res = split(str(new_s), next_level)

    cache[(stone, level)] = res
    return res

rounds = 25
print("Solution part1: %d" % (sum([split(s,rounds) for s in stones])))

rounds = 75 
print("Solution part2: %d" % (sum([split(s,rounds) for s in stones])))
