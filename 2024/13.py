print(chr(27)+'[2j')
print('\033c')
f = open('13.test', 'r')
#f = open('13.input', 'r')
machines = [x.strip() for x in f.read().split('\n\n')]

def parse_machine(machine):
    a,b,p = machine.split('\n') 
    _, _, x, y = a.replace(',', '').split()
    xa = int(x.split('+')[1])
    ya = int(y.split('+')[1])
    _, _, x, y = b.replace(',', '').split()
    xb = int(x.split('+')[1])
    yb = int(y.split('+')[1])
    _, x, y = p.replace(',', '').split()
    x0 = int(x.split('=')[1])
    y0 = int(y.split('=')[1])
    return (xa,ya, xb,yb, x0,y0)

# A costs 3 tokens
# B costs 1 tokens

def get_win1(machine):
    (xa,ya, xb,yb, x0,y0) = machine
    max_rounds = 100
    cheapest = 3000
    has_win = False
    for i in range(max_rounds):
        for j in range(max_rounds):
            x = xa * i + xb * j
            y = ya * i + yb * j
            if x > x0 or y > y0:
                break
            if x == x0 and y == y0:
                cost = i * 3 + j
                print(i,j)
                print(f'Win at ({i} {j}), cost {cost}')
                cheapest = min(cheapest, cost)
                has_win = True
        
    return has_win, cheapest

def get_win2(machine):
    (xa,ya, xb,yb, x0,y0) = machine
    x0 += 10000000000000
    y0 += 10000000000000
    cheapest = 10000000000000
    has_win = False
    D = xa * yb - xb * ya
    assert(D != 0)
    # Inverse the Matrix
    i = (yb*x0 - xb*y0) / D
    j = (-1*ya*x0 + xa*y0) / D
    if int(i) == i and int(j) == j:
        i, j = int(i), int(j)
        cost = i * 3 + j
        print(f'Win at ({i} {j}), cost {cost}')
        cheapest = min(cheapest, cost)
        has_win = True
        
    return has_win, cheapest

tokens1 = 0
tokens2 = 0
for i, machine in enumerate(machines):
    print('---')
    machine = parse_machine(machine)
    print(f'Machine {i} = ', machine)
    win1, t1 = get_win1(machine)
    win2, t2 = get_win2(machine)
    if win1:
        tokens1 += t1
        print(f'Won. part1: {tokens1}')
    if win2:
        tokens2 += t2
        print(f'Won. part2: {tokens2}')

print('---')
print(f'Solution part1: {tokens1}')
print(f'Solution part2: {tokens2}')

