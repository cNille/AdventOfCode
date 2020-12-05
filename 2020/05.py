import re
f = open('05.input', 'r')
data = [x.strip() for x in f.readlines()]

def part1(data):
    max_id = 0
    for line in data:
        current = 0
        row = 64
        for c in line[:7]:
            if c == 'B':
                current += row
            row = row / 2

        current = current * 8
        row = 4 
        for c in line[7:]:
            if c == 'R':
                current += row
            row = row / 2
        max_id = current if current > max_id else max_id
        if current > 937:
            print line
    return max_id


def part2(data):

    id_list = []
    max_id = 0
    for line in data:
        current = 0
        row = 64
        for c in line[:7]:
            if c == 'B':
                current += row
            row = row / 2

        current = current * 8
        row = 4 
        for c in line[7:]:
            if c == 'R':
                current += row
            row = row / 2

        id_list.append(current)
    id_list = sorted(id_list)
    for i in range(940):
        low = i - 1
        high = i + 1
        if  low in id_list and high in id_list and i not in id_list:
            return i

d = sorted(data)
for l in d[:5]:
    print l
print "Part 1 solution: %d " % part1(data)
exit()
print "Part 2 solution: %d " % part2(data)
