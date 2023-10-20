print(chr(27)+'[2j')
print('\033c', end='')

# f = open('25.test', 'r')
f = open('25.input', 'r')
lines = [x.strip() for x in f.readlines()]


def solve(registers):
    idx = 0
    tick = 0
    while idx < len(lines):
        tick += 1
        if tick % 1000000 == 0:
            return None
        line = lines[idx]
        parts = line.split()
        # print(tick, idx, parts, registers)
        if parts[0] == 'cpy':
            if parts[1].isalpha():
                registers[parts[2]] = registers[parts[1]]
            else:
                registers[parts[2]] = int(parts[1])
        elif parts[0] == 'mul':
            registers[parts[3]] += registers[parts[1]] * registers[parts[2]]
        elif parts[0] == 'inc':
            registers[parts[1]] = registers[parts[1]] + 1
        elif parts[0] == 'out':
            # print("OUT", registers[parts[1]])
            yield registers[parts[1]]
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
                if int(parts[1]) != 0:
                    if parts[2].isalpha():
                        idx += registers[parts[2]]
                    else:
                        idx += int(parts[2])
                    continue
        idx += 1
    return registers['a']


test = 0
while True:
    count = 0
    curr = 1
    for x in solve({'a': test, 'b': 0, 'c': 0, 'd': 0}):
        # print("OUT", x)
        count += 1
        if x == curr:
            # print("Break")
            break
        else:
            curr = x
            if count == 100:
                print('Solution:', test)
                exit()
    test += 1
