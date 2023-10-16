print(chr(27)+'[2j')
print('\033c', end='')

print("Day 21")
f = open('21.input', 'r')
# f = open('21.test', 'r')
lines = [x.strip() for x in f.readlines()]


# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
def swap_position(pw: list[str], x: int, y: int):
    assert (x >= 0 and y >= 0)
    assert (x < len(pw) and y < len(pw))
    pw[x], pw[y] = pw[y], pw[x]
    return pw


# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
def swap_letter(pw: list[str], x: str, y: str):
    assert (x in pw)
    assert (y in pw)
    new_pw = []
    for l in pw:
        if l == x:
            new_pw.append(y)
        elif l == y:
            new_pw.append(x)
        else:
            new_pw.append(l)
    return new_pw


# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
def rotate_position(pw: list[str], direction: str, x: int):
    assert (direction == 'left' or direction == 'right')
    assert (x >= 0)
    for _ in range(x):
        if direction == 'left':
            first = pw.pop(0)
            pw.append(first)
        else:
            last = pw.pop()
            pw.insert(0, last)
    return pw


# rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
def rotate_letter(pw: list[str], x: str):
    assert (x in pw)
    direction = 'right'
    idx = pw.index(x)
    steps = idx + 1
    if steps > 4:
        steps += 1
    return rotate_position(pw, direction, steps)


def unrotate_letter(pw: list[str], x: str):
    assert (x in pw)
    direction = 'left'
    idx = pw.index(x)
    steps_dict = {
        0: 1,
        1: 1,
        2: 6,
        3: 2,
        4: 7,
        5: 3,
        6: 0,
        7: 4,
    }
    steps = steps_dict[idx]
    return rotate_position(pw, direction, steps)

# Rotation scheme:
# 01234567
# abcdefgh
# 7 -> 0
# 0 -> 1
# 4 -> 2
# 1 -> 3
# 5 -> 4
# 2 -> 5
# 6 -> 6
# 3 -> 7


# reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
def reverse(pw: list[str], x: int, y: int):
    assert (x >= 0 and y >= 0)
    assert (x < len(pw) and y < len(pw))
    assert (x < y)
    rev = pw[x:y+1]
    rev.reverse()
    return pw[:x] + rev + pw[y+1:]


# move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
def move(pw: list[str], x: int, y: int):
    assert (x != y)
    assert (x >= 0 and y >= 0)
    assert (x < len(pw) and y < len(pw))
    l = pw[x]
    pw = pw[:x] + pw[x+1:]
    pw.insert(y, l)
    return pw


pw = [x for x in 'abcde']
pw = [x for x in 'abcdefgh']
for l in lines:
    prev = [x for x in pw]
    if l.startswith("swap position"):
        _, _, x, _, _, y = l.split()
        pw = swap_position(pw, int(x), int(y))
    elif l.startswith("swap letter"):
        _, _, x, _, _, y = l.split()
        pw = swap_letter(pw, x, y)
    elif l.startswith("reverse"):
        _, _, x, _, y = l.split()
        pw = reverse(pw, int(x), int(y))
    elif l.startswith("rotate based"):
        _, _, _, _, _, _, x = l.split()
        pw = rotate_letter(pw, x)
    elif l.startswith("rotate"):
        _, direction, x, _ = l.split()
        pw = rotate_position(pw, direction, int(x))
    elif l.startswith("move position"):
        _, _, x, _, _, y = l.split()
        pw = move(pw, int(x), int(y))
    else:
        print("Unknown:", l)
        exit()
print("Part 1", "".join(pw))

# exit()

# Part 2
pw = [x for x in 'fbgdceah']
lines = lines[::-1]
for l in lines:
    prev = [x for x in pw]
    if l.startswith("swap position"):
        _, _, x, _, _, y = l.split()
        pw = swap_position(pw, int(x), int(y))
    elif l.startswith("swap letter"):
        _, _, x, _, _, y = l.split()
        pw = swap_letter(pw, x, y)
    elif l.startswith("reverse"):
        _, _, x, _, y = l.split()
        pw = reverse(pw, int(x), int(y))
    elif l.startswith("rotate based"):
        _, _, _, _, _, _, x = l.split()
        pw = unrotate_letter(pw, x)
    elif l.startswith("rotate"):
        _, direction, x, _ = l.split()
        rev_direction = 'left' if direction == 'right' else 'right'
        pw = rotate_position(pw, rev_direction, int(x))
    elif l.startswith("move position"):
        _, _, x, _, _, y = l.split()
        pw = move(pw, int(y), int(x))
    else:
        print("Unknown:", l)
        exit()
print("Part 2", "".join(pw))


# Tests
# pw = [x for x in 'abcde']
# assert (swap_position(pw, 0, 3) == ['d', 'b', 'c', 'a', 'e'])
# pw = [x for x in 'abcde']
# assert (swap_letter(pw, 'a', 'd') == ['d', 'b', 'c', 'a', 'e'])
# pw = [x for x in 'abcde']
# assert (rotate_position(pw, 'right', 2) == ['d', 'e', 'a', 'b', 'c'])
# pw = [x for x in 'abcde']
# assert (rotate_position(pw, 'left', 3) == ['d', 'e', 'a', 'b', 'c'])
# pw = [x for x in 'abcde']
# assert (rotate_letter(pw, 'c') == ['c', 'd', 'e', 'a', 'b'])
