f = open('04.test', 'r')
f = open('04.input', 'r')
content = [x.strip() for x in f.readlines()]

def part1():
    count = 0
    for line in content:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))

        if a1 <= b1 and a2 >= b2:
            count += 1
        elif b1 <= a1 and b2 >= a2:
            count += 1
    return count
print("Solution part 1:", part1())

def part2():
    count = 0
    for line in content:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))

        aset = set(list(range(a1,a2+1)))
        bset = set(list(range(b1,b2+1)))
        common = aset.intersection(bset)
        if(len(common) > 0):
            count+=1
        
    return count
print("Solution part 2:", part2())
