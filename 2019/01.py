f = open('01.input', 'r')
content = [int(x.strip()) for x in f.readlines()]

# Part 1
res = 0
for c in content:
    fuel = (c / 3) - 2
    res += fuel
print('Result part 1: %d' % res)

# Part 2
res = 0
for c in content:
    fuel = c
        
    while(fuel > 0):
        fuel = (fuel / 3) - 2

        if fuel > 0:
            res += fuel
print('Result part 2: %d' % res)
