f = open('03.test', 'r')
f = open('03.input', 'r')
lines = [x.strip() for x in f.readlines()]

# --------------
# Utils 

def nth_most_common(lines, n):
    half = float(len(lines)) / 2.0
    nth_bit = [x[n] for x in lines]
    return '1' if nth_bit.count('1') >= half else '0' 

def nth_least_common(lines, n):
    half = float(len(lines)) / 2.0
    nth_bit = [x[n] for x in lines]
    return '0' if nth_bit.count('1') >= half else '1' 

# --------------
# Part 1

def part1():
    bits_count = len(lines[0])
    gamma = ''.join([
        nth_most_common(lines, i) 
        for i in range(bits_count)
    ])

    epsilon = ''.join([
        nth_least_common(lines, i) 
        for i in range(bits_count)
    ])

    return int(gamma, 2) * int(epsilon, 2)
print("Solution part1: %d" % part1())

# --------------
# Part 2

def find_by(lines, filter_function):
    bits_count = len(lines[0])
    filtered = lines
    for i in range(bits_count):
        filtered = [
            x for x in filtered 
            if x[i] == filter_function(filtered,i)
        ] 
        if len(filtered) == 1:
            break
    return int(filtered[0], 2)

def part2():
    ogr = find_by(lines, nth_most_common)
    csr = find_by(lines, nth_least_common)
    return ogr * csr
print("Solution part2: %d" % part2())
