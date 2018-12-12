
# Import data
#data = [x.strip() for x in open('day_12_test.txt','r').readlines()]
data = [x.strip() for x in open('day_12_input.txt','r').readlines()]

state = data[0].split(' ')[2]

rules = {}
for line in data[2:]:
    (condition, result) = line.split(' => ')
    rules[condition] = result

def part1(state):
    generations = 20
    state = '...' + state + '........................'
    # print('I state: %s' % state)
    gen = 0
    while gen < generations:
        new_state = '.'
        for i in range(1,len(state)-2):
            if i == 1:
                s = '.' + state[i-1:i+3]
            else:
                s = state[i-2: i+3]

            if s not in rules:
                new_s = '.'
            else:
                new_s = rules[s]
            new_state += new_s

        state = new_state + '..'


        # print('%d state: %s' % (gen,state))
        gen +=1

    result = 0
    for i in range(-3,len(state)-3):
        if state[i+3] == '#':
            result += i
    print('Part 1 result: %s' % result)
part1(state)

# =============================================================================
# Part 2
def part2(state):
    state = '...' + state + '...........................................................................................................'
    gen = 0
    curr = 0
    generations = 500
    while gen < generations:
        new_state = '..'
        last_hash = 0
        for i in range(2,len(state)-3):
            s = state[i-2: i+3]
            new_s = rules[s]
            new_state += new_s
            if new_s == '#':
                last_hash = i
        state = new_state + '...'
        if last_hash > len(state) - 5:
            curr += 1
            state = state[1:] + '.'
        gen +=1

    # Now the recipe has converged and we can calculate the rest
    # by integer calculations.

    # Nbr of hashes represent diff of result per generation
    hashes = len([x for x in state if x == '#'])

    # Calculate current result
    result = 0
    for i in range(-3,len(state)-3):
        if state[i+3] == '#':
            result += i + curr

    # Calculate how many generations are left, multiply to diff and apply to
    # the current result
    all_result = (50000000000 - (gen)) * hashes + result
    print('Part 2 result: %d' % all_result)
part2(state)
