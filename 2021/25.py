print(chr(27)+'[2j')
print('\033c')
f = open('25.test', 'r')
f = open('25.input', 'r')
#f = open('25.test2', 'r')
data = [x.strip() for x in f.readlines()]

mtx = []

for line in data: mtx.append([x for x in line])

def p(mtx):
    for row in mtx:
        print(''.join(row))

def run_mtx(mtx):
    
    did_switch = False
    switches = []
    for y, row in enumerate(mtx):
        for x, col in enumerate(row):
            if col == '.':
                left = (x-1) % len(row)
                if mtx[y][left] == '>':
                    a = (x,y)
                    b = (left,y)
                    switches.append((a,b))
                    continue
    for a, b in switches:
        did_switch = True
        mtx[a[1]][a[0]], mtx[b[1]][b[0]] = mtx[b[1]][b[0]], mtx[a[1]][a[0]]

    switches = []
    for y, row in enumerate(mtx):
        for x, col in enumerate(row):
            if col == '.':
                above = (y-1) % len(mtx)
                if mtx[above][x] == 'v':
                    a = (x, y)
                    b = (x, above)
                    switches.append((a,b))
                    continue
    for a, b in switches:
        did_switch = True
        mtx[a[1]][a[0]], mtx[b[1]][b[0]] = mtx[b[1]][b[0]], mtx[a[1]][a[0]]

    return mtx, did_switch 

count =0 

print("Initial state:")
p(mtx)

while True:
    mtx, did_switch = run_mtx(mtx)
    count += 1 
    print("After", count, "step:")
    #p(mtx)
    print()
    if not did_switch:
        break
