print(chr(27)+'[2j')
print('\033c', end='')

f = open('15.test', 'r')
f = open('15.input', 'r')
lines = [x.strip() for x in f.readlines()]

discs = []
for line in lines:
    parts = line.split()
    id = int(parts[1][1:])
    positions = int(parts[3])
    start = int(parts[11][:-1])
    discs.append((id, positions, start))

def check(discs, time):
    level = 0
    while True:
        time += 1
        level += 1
        if level > len(discs):
            return True

        disc = discs[level-1]
        pos = (disc[2] + time) % disc[1]
        if pos != 0:
            return False
    
# part 1 
i = 0
while True:
    success = check(discs, i)
    if success:
        print('Solution part 1: %d' % i)
        break
    i += 1

# part 2 
discs.append((len(discs)+1, 11, 0))
i = 0
while True:
    success = check(discs, i)
    if success:
        print('Solution part 2: %d' % i)
        exit()
    i += 1
