print(chr(27)+'[2j')
print('\033c')
f = open('04.input', 'r')
#f = open('04.test', 'r')
lines = [x.strip() for x in f.readlines()]

verbose = False


for line in lines:
    if verbose:
        print(line)

def pprint(found):
    if not verbose:
        return
    print('---')
    for y in range(len(lines)):
        line = ''
        for x in range(len(lines[0])):
            if (x,y) in found:
                line += lines[y][x] 
            else:
                line += "."
        print(line)


matrixes_part1 = [
    [
        'XMAS',
    ],
    [
        'SAMX',
    ],
    [
        'X',
        'M',
        'A',
        'S',
    ],
    [
        'S',
        'A',
        'M',
        'X',
    ],
    [
        'X...',
        '.M..',
        '..A.',
        '...S',
    ],
    [
        '...X',
        '..M.',
        '.A..',
        'S...',
    ],
    [
        '...S',
        '..A.',
        '.M..',
        'X...',
    ],
    [
        'S...',
        '.A..',
        '..M.',
        '...X',
    ],
]

matrixes_part2 = [
    [
        'M.M',
        '.A.',
        'S.S',
    ],
    [
        'S.M',
        '.A.',
        'S.M',
    ],
    [
        'S.S',
        '.A.',
        'M.M',
    ],
    [
        'M.S',
        '.A.',
        'M.S',
    ],
]

def solve(matrixes):
    total = 0
    found = []
    for m in matrixes:
        count = 0
        if verbose:
            print('-------')
            for row in m:
                print(row)
        for y in range(len(lines) - len(m)+1):
            for x in range(len(lines[0]) - len(m[0])+1):
                matches = True

                for my in range(len(m)):
                    for mx in range(len(m[0])):
                        if m[my][mx] == '.':
                            continue
                        if lines[y+my][x+mx] != m[my][mx]:
                            matches = False

                if matches:
                    count += 1

                    for my in range(len(m)):
                        for mx in range(len(m[0])):
                            if m[my][mx] != '.':
                                found.append((x+mx, y+my))
        total += count
        if verbose:
            print("Found %d (%d)"% (count, total))
    return total, found

# Part 1
count, found = solve(matrixes_part1)
pprint(found)
print("Solution part1:", count)

# Part 2
count, found = solve(matrixes_part2)
pprint(found)
print("Solution part2:", count)
