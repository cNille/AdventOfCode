f = open('03.test', 'r')
f = open('03.input', 'r')
lines = [x.strip() for x in f.readlines()]

# --------------
# Utils 

def nth_most_common(lines, n):
    half = float(len(lines)) / 2.0
    nth_bit = [x[n] for x in lines]
    ones = sum(map(int, nth_bit))
    return '1' if ones >= half else '0' 

def nth_least_common(lines, n):
    half = float(len(lines)) / 2.0
    nth_bit = [x[n] for x in lines]
    ones = sum(map(int, nth_bit))
    return '0' if ones >= half else '1' 

# --------------
# Part 1

def part1():
    bits_count=len(lines[0])
    gamma = ''.join([
        nth_most_common(lines, i) 
        for i in range(bits_count)
    ])

    epsilon = ''.join([
        nth_least_common(lines, i) 
        for i in range(bits_count)
    ])

    gamma = int(gamma, 2) 
    epsilon = int(epsilon, 2) 
    return epsilon * gamma
print("Solution part1: %d" % part1())

# --------------
# Part 2

def find_by(lines, filter_function):
    bits_count= len(lines[0])
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
    bits_count=len(lines[0])
    ogr = csr = lines
    ogr = find_by(lines, nth_most_common)
    csr = find_by(lines, nth_least_common)
    return ogr * csr
print("Solution part2: %d" % part2())
