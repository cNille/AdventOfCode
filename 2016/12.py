print(chr(27)+'[2j')
print('\033c', end='')

f = open('12.test', 'r')
#f = open('12.input', 'r')
lines = [x.strip() for x in f.readlines()]

def solve(registers):
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        parts = line.split()
        if parts[0] == 'cpy':
            if parts[1].isalpha():
                registers[parts[2]] = registers[parts[1]]
            else:
                registers[parts[2]] = int(parts[1])
        elif parts[0] == 'inc':
            registers[parts[1]] = registers[parts[1]] + 1
        elif parts[0] == 'dec':
            registers[parts[1]] = registers[parts[1]] - 1
        elif parts[0] == 'jnz':
            if parts[1].isalpha():
                if registers[parts[1]] != 0:
                    idx += int(parts[2])
                    continue
            else:
                if parts[1] != 0:
                    idx += int(parts[2])
                    continue
        idx += 1
    return registers['a']

part1 = solve({'a': 0, 'b': 0, 'c': 0, 'd': 0})
print("Solution part 1:", part1)
part2 = solve({'a': 0, 'b': 0, 'c': 1, 'd': 0})
print("Solution part 2:", part2)
