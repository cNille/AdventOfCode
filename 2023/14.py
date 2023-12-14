print(chr(27)+'[2j')
print('\033c')
#f = open('14.input', 'r')
f = open('14.test', 'r')
lines = [x.strip() for x in f.readlines()]


def roll_north(lines):
    changed = True
    while changed:
        changed = False
        for y in range(1, len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == 'O' and lines[y-1][x] == '.':
                    lines[y-1] = lines[y-1][:x] + 'O' + lines[y-1][x+1:]
                    lines[y] = lines[y][:x] + '.' + lines[y][x+1:]
                    changed = True
    return lines


def roll_south(lines):
    changed = True
    while changed:
        changed = False
        for y in range(len(lines)-2, -1, -1):
            for x in range(len(lines[y])):
                if lines[y][x] == 'O' and lines[y+1][x] == '.':
                    lines[y+1] = lines[y+1][:x] + 'O' + lines[y+1][x+1:]
                    lines[y] = lines[y][:x] + '.' + lines[y][x+1:]
                    changed = True
    return lines


def roll_east(lines):
    changed = True
    while changed:
        changed = False
        for y in range(len(lines)):
            for x in range(len(lines[y])-1):
                if lines[y][x] == 'O' and lines[y][x+1] == '.':
                    lines[y] = lines[y][:x] + '.' + lines[y][x+1:]
                    lines[y] = lines[y][:x+1] + 'O' + lines[y][x+2:]
                    changed = True
    return lines


def roll_west(lines):
    changed = True
    while changed:
        changed = False
        for y in range(len(lines)):
            for x in range(len(lines[y])-1, 0, -1):
                if lines[y][x] == 'O' and lines[y][x-1] == '.':
                    lines[y] = lines[y][:x-1] + 'O' + lines[y][x:]
                    lines[y] = lines[y][:x] + '.' + lines[y][x+1:]
                    changed = True
    return lines


def calculate_value(lines):
    rev = lines[::-1]
    total = 0
    for i, line in enumerate(rev):
        count = line.count('O')
        total += count * (i+1)
    return total


def part1(lines):
    new_lines = roll_north(lines)
    value = calculate_value(new_lines)
    return value


def part2(lines):
    visited = set()
    visited_arr = []
    value = None
    values = []
    start_index = 0
    for _ in range(1000):
        lines = roll_north(lines)
        lines = roll_west(lines)
        lines = roll_south(lines)
        lines = roll_east(lines)
        value = calculate_value(lines)
        one_line = ''.join(lines)
        if one_line in visited:
            start_index = visited_arr.index(one_line)
            break
        visited.add(one_line)
        visited_arr.append(one_line)
        values.append(value)

    cycle = values[start_index:]
    mod = (1000000000-1 - start_index) % len(cycle)
    result = cycle[mod]
    return result


print('Part 1:', part1(lines.copy()))
print('Part 2:', part2(lines.copy()))
