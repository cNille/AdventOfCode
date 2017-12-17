steps = 316
rounds = 2018
state = [0]
currpos = 0
for curr in range(1, rounds):
    currpos = ((currpos + steps) % len(state)) + 1
    state.insert(currpos, curr)
print('Result:', state[state.index(2017) + 1])
