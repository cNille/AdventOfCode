print(chr(27)+'[2j')
print('\033c')
f = open('05.input', 'r')
f = open('05.test', 'r')
rows = [x for x in f.readlines()]

crate_rows = []
mtx = []
instr = []
is_columns = True
for line in rows:
    if line.strip() == "":
        is_columns = False
        continue
    if is_columns:
        crate_rows.append(line)
    else:
        instr.append(line)

for row in crate_rows[:-1]:
    # Get each 4th char, with offset 1.
    every = 4
    offset = 1
    start = offset
    end = len(row) + offset
    for i in range(start, end, every):
        column_idx = int(i/4)
        # Add a new column if needed.
        if column_idx >= len(mtx):
            mtx.append([])

        # Get crate
        crate = row[i]

        # If crate not empty, add it to the stack.
        if crate != ' ':
            mtx[column_idx].insert(0, crate)

print(mtx)


def do_instr(instr, mtx, reverse=False):
    for i in instr:
        _, nbr, _, src, _, dest = i.split(' ')
        nbr = int(nbr)
        src = int(src) - 1
        dest = int(dest) - 1

        poped = []
        for _ in range(nbr):
            poped.append(mtx[src].pop())

        if reverse:
            poped.reverse()

        for p in poped:
            mtx[dest].append(p)

    res = ""
    for m in mtx:
        res += m[-1]
    return res


part1 = do_instr(instr, [x.copy() for x in mtx])
print("Solution part 1:", part1)

part2 = do_instr(instr, [x.copy() for x in mtx], True)
print("Solution part 2:", part2)
