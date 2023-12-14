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


def rotate_lines(lines):
    return list(map("".join, zip(*lines[::-1])))


def calculate_value(lines):
    total = 0
    for i, line in enumerate(lines[::-1]):
        total += line.count('O') * (i+1)
    return total


def part1(lines):
    new_lines = roll_north(lines)
    value = calculate_value(new_lines)
    return value


def part2(lines):
    visited = {}
    values = []
    start_index = 0
    for i in range(1000):
        for _ in range(4):
            lines = roll_north(lines)
            lines = rotate_lines(lines)
        value = calculate_value(lines)
        one_line = ''.join(lines)
        if one_line in visited:
            start_index = visited[one_line]
            break
        visited[one_line] = i
        values.append(value)

    cycle = values[start_index:]
    mod = (1000000000-1 - start_index) % len(cycle)
    result = cycle[mod]
    return result


print('Part 1:', part1(lines.copy()))
print('Part 2:', part2(lines.copy()))
