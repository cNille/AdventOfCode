print(chr(27)+'[2j')
print('\033c')
f = open('11.test', 'r')
#f = open('11.test2', 'r')
f = open('11.input', 'r')
lines = [x.strip() for x in f.readlines()]

stones = []
for line in lines:
    for stone in line.split():
        stones.append(stone)
print('stones', stones)

cache = {}
def split(stone: str):
    if stone in cache:
        return cache[stone]
    new_stones = []
    if stone == '0':
        new_stones.append('1')
    elif len(stone) % 2 == 0:
        half = len(stone)//2
        left = stone[:half]
        right = stone[half:]
        new_stones.append(left)
        new_stones.append(right)
    else:
        new_s = int(stone) * 2024
        new_stones.append(str(new_s))

    cache[stone] = new_stones
    return new_stones

rounds = 6
rounds = 25 
rounds = 75 
for i in range(rounds):
    new_stones = []
    for s in stones:
        new_stones.extend(split(s))
    stones = new_stones

    #line = ' '.join([str(s) for s in stones])
    #print("Blink %d:" % (i+1), line)
    #print('-------')
    print("Blink %d: %d" % (i+1, len(new_stones)))

