print(chr(27)+'[2j')
print('\033c')
f = open('13.input', 'r')
#f = open('13.test', 'r')

patterns = f.read().split('\n\n')
patterns = [p.strip().split('\n') for p in patterns]
f.close()


def find_vertical_mirror(pattern, smudge_allow):
    mirror_idx = 1
    smudge_count = 0
    length = len(pattern[0])
    while mirror_idx < len(pattern[0]):
        smudge_count = 0
        width = min(mirror_idx, length - mirror_idx)
        for row in pattern:
            left_start = mirror_idx - width
            left = row[left_start:mirror_idx]
            right_end = mirror_idx + width
            right = row[mirror_idx:right_end]
            assert(len(left) == len(right))
            c1 = left
            c2 = right[::-1]
            for i in range(len(c1)):
                if c1[i] != c2[i]:
                    smudge_count += 1
        if smudge_count == smudge_allow:
            break
        mirror_idx += 1
    if smudge_count == smudge_allow:
        return mirror_idx
    return -1


# Use zip to transpose the matrix
def rotate(pattern):
    return list(zip(*pattern))


def find_horisontal_mirror(pattern, smudge_allow):
    p2 = rotate(pattern)
    return find_vertical_mirror(p2, smudge_allow)


def solve(smudge_allow: int):
    total = 0
    for p in patterns:
        vertical_mirror = find_vertical_mirror(p, smudge_allow)
        if vertical_mirror != -1:
            total += vertical_mirror
        horisontal_mirror = find_horisontal_mirror(p, smudge_allow)
        if horisontal_mirror != -1:
            total += horisontal_mirror * 100
        assert(not (vertical_mirror == -1 and horisontal_mirror == -1))
        assert(not (vertical_mirror != -1 and horisontal_mirror != -1))
    return total


print('Part1', solve(0))
print('Part2', solve(1))
