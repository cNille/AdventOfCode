f = open('03.test', 'r')
f = open('03.input', 'r')
lines = [x.strip() for x in f.readlines()]

# --------------
# Utils 

def get_common(lines):
    s = set(lines[0])
    for line in lines[1:]:
        s = s.intersection(set(line))
    return list(s)

def get_points(ch):
    p = 0 
    if ch.isupper():
        p += 26
        p += ord(ch) - 64
    else:
        p += ord(ch) - 96
    return p

# --------------
# Part 1

def part1():
    v = 0
    for l in lines:
        length = int(len(l) / 2)
        l1, l2 = l[:length], l[length:]
        common = get_common([l1,l2])
        common = common[0]

        v += get_points(common)
    return v 
print("Solution part1: %d" % part1())

# --------------
# Part 2
def part2():
    v = 0
    for i in range(0,len(lines), 3):
        l1, l2, l3 = lines[i], lines[i +1], lines[i+2]
        common = get_common([l1,l2,l3])
        common = common[0]

        v += get_points(common)
    return v 
print("Solution part2: %d" % part2())
