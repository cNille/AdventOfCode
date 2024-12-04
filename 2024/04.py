print(chr(27)+'[2j')
print('\033c')
f = open('04.input', 'r')
f = open('04.test', 'r')
lines = [x.strip() for x in f.readlines()]

for line in lines:
    print(line)

#def pprint():
#    print('Found', len(found))
#    for y in range(len(lines)):
#        line = ''
#        for x in range(len(lines[0])):
#            if (x,y) in found:
#                line += "X"
#            else:
#                line += "."
#        print(line)

# Part 1
count = 0
found = []
for y in range(len(lines)):
    for x in range(len(lines[0])-3):
        if (
            lines[y][x] == 'X' and
            lines[y][x+1] == 'M' and
            lines[y][x+2] == 'A' and
            lines[y][x+3] == 'S'
            ):
            count += 1
            found.append((x,y))

for y in range(len(lines)):
    for x in range(3,len(lines[0])):
        if (
            lines[y][x] == 'X' and
            lines[y][x-1] == 'M' and
            lines[y][x-2] == 'A' and
            lines[y][x-3] == 'S'
            ):
            count += 1
            found.append((x,y))

for y in range(len(lines)-3):
    for x in range(len(lines[0])):
        if (
            lines[y][x] == 'X' and
            lines[y+1][x] == 'M' and
            lines[y+2][x] == 'A' and
            lines[y+3][x] == 'S'
            ):
            count += 1
            found.append((x,y))

for y in range(3,len(lines)):
    for x in range(len(lines[0])):
        if (
            lines[y][x] == 'X' and
            lines[y-1][x] == 'M' and
            lines[y-2][x] == 'A' and
            lines[y-3][x] == 'S'
            ):
            count += 1
            found.append((x,y))

for y in range(0,len(lines)-3):
    for x in range(0,len(lines[0])-3):
        # Diagonal down right
        if (
            lines[y][x] == 'X' and
            lines[y+1][x+1] == 'M' and
            lines[y+2][x+2] == 'A' and
            lines[y+3][x+3] == 'S'
            ):
            count += 1
            found.append((x,y))

for y in range(len(lines)-3):
    for x in range(3,len(lines[0])):
        # Diagonal down left
        if (
            lines[y][x] == 'X' and
            lines[y+1][x-1] == 'M' and
            lines[y+2][x-2] == 'A' and
            lines[y+3][x-3] == 'S'
            ):
            count += 1
            found.append((x,y))

for y in range(3,len(lines)):
    for x in range(len(lines[0])-3):
        # Diagonal up right
        if (
            lines[y][x] == 'X' and
            lines[y-1][x+1] == 'M' and
            lines[y-2][x+2] == 'A' and
            lines[y-3][x+3] == 'S'
            ):
            count += 1
            found.append((x,y))

for y in range(3,len(lines)):
    for x in range(3,len(lines[0])):
        # Diagonal up left
        if (
            lines[y][x] == 'X' and
            lines[y-1][x-1] == 'M' and
            lines[y-2][x-2] == 'A' and
            lines[y-3][x-3] == 'S'
            ):
            count += 1
            found.append((x,y))


print('Solution part 1:', count)
# Part 2
count = 0
found = []
for y in range(0,len(lines)-2):
    for x in range(0,len(lines[0])-2):
        if (
            lines[y][x] == 'M' and
            lines[y+2][x] == 'M' and
            lines[y+1][x+1] == 'A' and
            lines[y+2][x+2] == 'S' and
            lines[y][x+2] == 'S'
            ):
            count += 1
            found.append((x,y))
            found.append((x+1,y+1))
            found.append((x+2,y+2))
            found.append((x,y+2))
            found.append((x+2,y))
        if (
            lines[y][x] == 'S' and
            lines[y+2][x] == 'S' and
            lines[y+1][x+1] == 'A' and
            lines[y+2][x+2] == 'M' and
            lines[y][x+2] == 'M'
            ):
            count += 1
            found.append((x,y))
            found.append((x+1,y+1))
            found.append((x+2,y+2))
            found.append((x,y+2))
            found.append((x+2,y))
        if (
            lines[y][x] == 'M' and
            lines[y+2][x] == 'S' and
            lines[y+1][x+1] == 'A' and
            lines[y+2][x+2] == 'S' and
            lines[y][x+2] == 'M'
            ):
            count += 1
            found.append((x,y))
            found.append((x+1,y+1))
            found.append((x+2,y+2))
            found.append((x,y+2))
            found.append((x+2,y))
        if (
            lines[y][x] == 'S' and
            lines[y+2][x] == 'M' and
            lines[y+1][x+1] == 'A' and
            lines[y+2][x+2] == 'M' and
            lines[y][x+2] == 'S'
            ):
            count += 1
            found.append((x,y))
            found.append((x+1,y+1))
            found.append((x+2,y+2))
            found.append((x,y+2))
            found.append((x+2,y))
print('Solution part 2:', count)
