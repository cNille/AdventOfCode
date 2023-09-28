print(chr(27)+'[2j')
print('\033c', end='')


print("Day 18")


puzzle_input = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."


def next_row(prev_row: str):
    t = "^"
    row = ""
    prev = "." + prev_row + "."
    for idx in range(len(prev_row)):
        i = idx + 1
        is_trap = False
        l, c, r = prev[i-1], prev[i], prev[i+1]
        #print(i, "Previous",l,c,r)

        is_trap = is_trap or (l == t and c == t and r != t)
        is_trap = is_trap or (l != t and c == t and r == t)
        is_trap = is_trap or (l == t and c != t and r != t)
        is_trap = is_trap or (l != t and c != t and r == t)

        if is_trap:
            row += "^"
            #print("is-trap", row)
        else:
            row += "."
            #print("no-trap", row)
    return row



def count_tiles(row_count: int):
    rows = [puzzle_input] 
    for i in range(row_count - 1):
        #if i % 1000 == 0:
        #    print("Row %d done" % i)
        rows.append(next_row(rows[-1]))

    safe_tiles = 0
    for i, r in enumerate(rows):
        for l in r:
            if l == ".":
                safe_tiles += 1
        #print(r)
    print("Rows", len(rows))
    print("Safe tiles", safe_tiles)
    return safe_tiles

print("Part 1:", count_tiles(40))
print("Part 2:", count_tiles(400000))
