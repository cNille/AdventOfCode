my_input = "2   8   8   5   4   2   3   1   5   5   1   2   15  13  5   14"

banks = [int(x) for x in my_input.split(' ') if len(x) > 0]
states = []

while True:
    if str(banks) in states:
        print('Duplicate found at count:', len(states))
        start = states.index(str(banks))
        end = len(states)
        print('Loop length:', end - start)
        exit()
        
    states.append(str(banks))
    #print(str(banks))

    idx = banks.index(max(banks))
    value = banks[idx]
    banks[idx] = 0

    for i in range(1, value+1):
        banks[ (idx + i) % len(banks) ] += 1
