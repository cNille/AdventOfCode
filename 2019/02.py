f = open('02.input', 'r')
content = [x.strip() for x in f.readlines()]
data = [int(x) for x in content[0].split(',')]

def program(verb, noun, data):
    curr = 0
    data[1] = verb 
    data[2] = noun 

    while data[curr] != 99:
        if data[curr] == 1:
            data[data[curr+3]] = data[data[curr+1]] + data[data[curr+2]]
        elif data[curr] == 2:
            data[data[curr+3]] = data[data[curr+1]] * data[data[curr+2]]
        else: 
            print('fatal error')
            exit()
        curr += 4
    return data[0]


# Part 1:
solution = program(12,2, list(data))
print("Part 1 solution: %d" % solution)

# Part 2
correct_output = 19690720
for x in range(100):
    for y in range(100):
        r = program(x,y, list(data))
        # print("Testing %d %d -> Result %d" % (x,y, r))
        if r == correct_output:
            result = 100 * x + y
            print("Part 2 solution: %d" % result)
            exit()

print("No solution found in part 2...")
