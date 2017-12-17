steps = 316
rounds = 50000000
last_val = 0
currpos = 0
for curr in range(1, rounds):
    currpos = ((currpos + steps) % curr) + 1
    if currpos == 1:
        last_val = curr
    if curr % 100000 == 0:
        print(curr, last_val)
print('lastval:', last_val)
