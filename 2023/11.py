from itertools import combinations 
import sys
sys.setrecursionlimit(50000)
print(chr(27)+'[2j')
print('\033c')
f = open('11.input', 'r')
#f = open('11.test', 'r')
lines = [x.strip() for x in f.readlines()]

print('Day 11')

def solve(lines, expansion):
    cols = len(lines[0])
    cols = {x: 0 for x in range(cols)}
    rows = {x: 0 for x in range(len(lines))}
    galaxies = []
    for y, line in enumerate(lines):
        galaxy_free_line = True
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append((x, y))
            if c != '.':
                galaxy_free_line = False 
                cols[x] += 1
        if galaxy_free_line:
            rows[y] += 1

    cols_to_expand = [k for k in cols.keys() if cols[k] == 0]
    cols_to_expand.sort(reverse=True)
    rows_to_expand = [k for k in rows.keys() if rows[k] != 0]
    rows_to_expand.sort(reverse=True)

    distances = 0
    for g1, g2 in combinations(galaxies, 2):
        distances += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

        min_col = min(g1[0], g2[0])
        max_col = max(g1[0], g2[0])
        for col in cols_to_expand:
            if min_col < col < max_col:
                distances += expansion - 1
        
        min_row = min(g1[1], g2[1])
        max_row = max(g1[1], g2[1])
        for row in rows_to_expand:
            if min_row < row < max_row:
                distances += expansion - 1
    return distances

print("Part 1:", solve(lines, 2))
print("Part 2:", solve(lines, 1000000))
