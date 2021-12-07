# f = open('07.input', 'r')
# lines = [x.strip() for x in f.readlines()]
# positions = list(map(int, lines[0].split(',')))
positions = list(map(int, '16,1,2,0,4,2,7,1,2,14'.split(',')))

min_pos = min(positions)
max_pos = max(positions)

def part1():
    least_fuel = 99999999
    for i in range(min_pos, max_pos):
        fuel = sum([abs(p - i) for p in positions])
        least_fuel = min(fuel, least_fuel)
    print(least_fuel)
part1()

def calc(a,b):
    steps = abs(a - b)
    # Arithmetic series formula: n ((a1*an) / 2)
    # n = number of elements
    # a1 = first elements
    # an = last elements
    return steps * (1 + steps) // 2 
def part2():
    least_fuel = 99999999
    for i in range(min_pos, max_pos):
        fuel = sum([calc(p,i) for p in positions])
        least_fuel = min(fuel, least_fuel)
    print(least_fuel)
part2()

