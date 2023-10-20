print(chr(27)+'[2j')
print('\033c', end='')

f = open('23.test', 'r')
f = open('23.input', 'r')
lines = [x.strip() for x in f.readlines()]


def solve(registers):
    idx = 0
    count = 0
    while idx < len(lines):
        count += 1
        if count % 1000000 == 0:
            print(count, registers)
        line = lines[idx]
        print(line)
        print(idx, registers)
        parts = line.split()
        if parts[0] == 'cpy':
            if parts[1].isalpha():
                registers[parts[2]] = registers[parts[1]]
            else:
                registers[parts[2]] = int(parts[1])
        elif parts[0] == 'mul':
            registers[parts[3]] = registers[parts[1]] * registers[parts[2]]
        elif parts[0] == 'inc':
            registers[parts[1]] = registers[parts[1]] + 1
        elif parts[0] == 'dec':
            registers[parts[1]] = registers[parts[1]] - 1
        elif parts[0] == 'tgl':
            tgl_idx = idx + registers[parts[1]]
            if tgl_idx < len(lines):
                tgl_line = lines[tgl_idx]
                tgl_parts = tgl_line.split()
                if len(tgl_parts) == 2:
                    if tgl_parts[0] == 'inc':
                        tgl_parts[0] = 'dec'
                    else:
                        tgl_parts[0] = 'inc'
                else:
                    if tgl_parts[0] == 'jnz':
                        tgl_parts[0] = 'cpy'
                    else:
                        tgl_parts[0] = 'jnz'
                lines[tgl_idx] = ' '.join(tgl_parts)
        elif parts[0] == 'jnz':
            if parts[1].isalpha():
                if registers[parts[1]] != 0:
                    idx += int(parts[2])
                    continue
            else:
                if parts[1] != 0:
                    if parts[2].isalpha():
                        idx += registers[parts[2]]
                    else:
                        idx += int(parts[2])
                    continue
        idx += 1
    return registers['a']


result = solve({'a': 12, 'b': 0, 'c': 0, 'd': 0})
print("Solution part 1:", result)

# Part 2 - Updated and optimized code

# cpy a b
# dec b
# cpy a d
# cpy 0 a
# cpy b c
# mul d c a
# cpy 0 c
# cpy 0 c
# cpy 0 d
# cpy 0 d
# dec b
# cpy b c
# cpy c d
# dec d
# inc c
# jnz d -2
# tgl c
# cpy -16 c
# jnz 1 c
# cpy 87 c
# jnz 97 d
# inc a
# inc d
# jnz d -2
# inc c
# jnz c -5
