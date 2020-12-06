import re
f = open('05.input', 'r')
data = [x.strip() for x in f.readlines()]

def calc_id(seat):
    transformation= { 'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    binary = "".join([transformation[x] for x in seat])
    return int(binary,2)

def part1binary(data):
    ids = [calc_id(x) for x in data]
    return max(ids)

def part2binary(data):
    ids = [calc_id(x) for x in data]

    for i in range(max(ids)):
        low = i - 1
        high = i + 1
        if  low in ids and high in ids and i not in ids:
            return i

print "Part 1 binary solution: %d " % part1binary(data)
print "Part 2 binary solution: %d " % part2binary(data)

def part1(data):
    ids = []
    for line in data:
        current = 0
        row = 64
        for letter in line[:7]:
            if letter == 'B':
                current += row
            row = row >> 1 # Shift right 1 bit

        current = current << 3 # Shift left 3 bits

        row = 4 
        for c in line[7:]:
            if c == 'R':
                current += row
            row = row >> 1 # Shift right 1 bit
        ids.append(current)

    return max(ids)


def part2(data):

    id_list = []
    max_id = 0
    for line in data:
        current = 0
        row = 64
        for c in line[:7]:
            if c == 'B':
                current += row
            row = row >> 1 # Shift right 1 bit

        current = current << 3 # Shift left 3 bits
        row = 4 
        for c in line[7:]:
            if c == 'R':
                current += row
            row = row >> 1 # Shift right 1 bit

        id_list.append(current)
    id_list = sorted(id_list)
    for i in range(940):
        low = i - 1
        high = i + 1
        if  low in id_list and high in id_list and i not in id_list:
            return i

print "Part 1 solution: %d " % part1(data)
print "Part 2 solution: %d " % part2(data)

def part1sorting(data):
    normalized = []
    for line in data:
        new_line = line.replace('R','B').replace('L','F')
        normalized.append(new_line)
    d = sorted(normalized)
    return d[0]

print "Part 1 sorted solution: %s " % part1sorting(data)

def part1str(data):
    d = sorted(data)
    highest_row_value = d[0][:7]
    i = 1
    while d[i][:7] == highest_row_value:
        i+=1

    highest_value = d[i-1]
    return calc_id(highest_value)

print "Part 1 string solution: %d " % part1str(data)
