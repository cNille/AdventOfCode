f = open('day_02_input.txt','r')
content = [x.strip() for x in f.readlines()]


two = 0
three = 0
for row in content:

    d = {}
    twol = False
    threel = False
    for l in row:
        c = row.count(l)
        if c == 2:
            twol = True
        if c == 3:
            threel = True
    if twol:
        two +=1
    if threel:
        three +=1

print('Result', two * three)

# Part 2

for row in content:
    for row2 in content:
        diff = 0
        diff_index = 0

        for i in range(len(row)):
            if row[i] != row2[i]:
                diff +=1
                diff_index = i

        if diff == 1:
            print('Diff', row, row2)
            print('Diff-index', diff_index)
            print('common', row[:diff_index] + row[1+diff_index:])



        # Prettier solution
        z = zip(row, row2)
        common = [x[0] for x in z if x[0] == x[1]]
        if len(z) - len(common) == 1:
            print('Solution', ''.join(common))
            print('Diff found')
