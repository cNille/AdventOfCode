# Read in groups from file
lines = [x.strip() for x in open('08.input', 'r').readlines() if x != '']
# Create tuples (x,y) where x is instruction and y is value
lines = [tuple(x.split()) for x in lines]

def part1(lines):
    lines_executed = set()
    cursor = 0
    accumulator = 0

    def acc(lines, cursor, accumulator):
        return (cursor + 1, accumulator + int(lines[cursor][1]))

    def jmp(lines, cursor, accumulator):
        return (cursor + int(lines[cursor][1]), accumulator )

    def nop(lines, cursor, accumulator):
        return (cursor + 1, accumulator)

    while cursor not in lines_executed:
        instruction = lines[cursor][0]
        lines_executed.add(cursor)
        operations = {
            'jmp': jmp,
            'acc': acc,
            'nop': nop,
        }
        operation = operations[instruction]
        cursor, accumulator = operation(lines, cursor, accumulator)
    return accumulator
print "Solution part 1: %d" % part1(lines)




def execute_program(lines):
    lines_executed = set()
    cursor = 0
    accumulator = 0

    def acc(lines, cursor, accumulator):
        return (cursor + 1, accumulator + int(lines[cursor][1]))

    def jmp(lines, cursor, accumulator):
        return (cursor + int(lines[cursor][1]), accumulator )

    def nop(lines, cursor, accumulator):
        return (cursor + 1, accumulator)

    terminated = False
    while not terminated and cursor not in lines_executed:
        instruction = lines[cursor][0]
        lines_executed.add(cursor)

        operations = {
            'jmp': jmp,
            'acc': acc,
            'nop': nop,
        }
        operation = operations[instruction]
        cursor, accumulator = operation(lines, cursor, accumulator)

        # Terminate if end at program
        terminated = cursor == len(lines)

    return terminated, accumulator

def part1quick(lines):
    _, result = execute_program(lines)
    return result
print part1quick(lines)
exit()

def part2(lines):
    for i in range(len(lines)):
        # Copy lines so that changes don't persist.  
        local_lines = [x for x in lines]

        # Switch statement jmp/nop
        if 'jmp' in local_lines[i][0]:
            local_lines[i] = ('nop', local_lines[i][1])
        elif 'nop' in local_lines[i][0]:
            local_lines[i] = ('jmp', local_lines[i][1])

        terminated, result = execute_program(local_lines)

        if terminated:
            break
    return result
print "Solution part 2: %d" % part2(lines)

def part1quick(lines):
    lines_executed = set()
    cursor, accumulator = 0, 0

    while cursor not in lines_executed:
        instruction = lines[cursor][0]
        lines_executed.add(cursor)
        if instruction == 'jmp':
            cursor += int(lines[cursor][1])
        elif instruction == 'nop':
            cursor += 1
        elif instruction == 'acc':
            accumulator += int(lines[cursor][1])
            cursor += 1
        else:
            raise Exception('Unexpected instruction', instruction)
    return accumulator
print part1quick(lines)
