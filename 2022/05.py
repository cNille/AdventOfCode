print(chr(27)+'[2j')
print('\033c')
#f = open('05.input', 'r')
f = open('05.test', 'r')
rows = [x for x in f.readlines()]

is_columns = True

columns = []
mtx1 = []
mtx2 = []
instr = []
max_width = 0
for line in rows:
    if line.strip() == "":
        is_columns = False
        continue
    if is_columns:
        columns.append(line)
        try:
            width = int(line.strip()[-1])
            if width > 0:
                max_width = width
        except:
            continue
    else:
        instr.append(line)

for i in range(max_width):
    mtx1.append([])
    mtx2.append([])

for column in columns[:-1]:
    length = len(column)
    column_width = int((length - 3) / 4) + 1
    for i in range(0, column_width):
        col = column[i*4:i*4+3]
        col = col[1:-1]
        if col != ' ':
            mtx1[i].insert(0, col)
            mtx2[i].insert(0, col)

def do_instr(instr, mtx, reverse=False):
    for i in instr:
        _, nbr, _, src, _, dest = i.split(' ')
        nbr = int(nbr)
        src = int(src) -1 
        dest = int(dest) -1

        poped = []
        for _ in range(nbr):
            poped.append(mtx[src].pop())

        if reverse:
            poped.reverse()

        for p in poped:
            mtx[dest].append(p)

    res = ""
    for m in mtx:
        res +=m[-1]
    return res

part1 = do_instr(instr, mtx1)
print("Solution part 1:", part1)

part2 = do_instr(instr, mtx2, True)
print("Solution part 2:", part2)
