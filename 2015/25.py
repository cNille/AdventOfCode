print(chr(27)+'[2j')
print('\033c', end='')


def get_next_pos():
    x = y = 0
    i = 1
    max_row = 0
    mtx = {}
    while True:
        mtx[(x, y)] = i
        yield (x, y)
        i += 1

        y -= 1
        x += 1

        if y < 0:
            max_row += 1
            y = max_row
            x = 0


target_row = 2947
target_column = 3029
count = 0
first_code = 20151125

curr = first_code
for x, y in get_next_pos():
    if target_row == (y+1) and target_column == (x+1):
        print("Result:", curr)
        break

    curr *= 252533
    curr = curr % 33554393
