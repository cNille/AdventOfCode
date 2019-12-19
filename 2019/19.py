from intcode import *
content = [x.strip() for x in open('19.input', 'r').readlines()][0]
input_code = content

def execute(x,y):
    stream = Streams(["A","B"])
    stream.add("A", x) 
    stream.add("A", y) 
    program = Program(IntCode(input_code), name="A", stream=stream)
    view = [out for out in program.run()]
    return view[0]

view = []
values = {}
for y in range(50):
    row = ""
    for x in range(50):
        output = execute(x,y)
        if output not in values:
            values[output] = 0
        values[output] += 1
        row += "#" if output == 1 else "."
    view.append(row)
    print(row)

print("Part 1 solution: %d " % values[1])

column_streak = {}
min_x = 1120
max_x = 99999
width = 0
y_max = {}
last_first_x_in_row = None
row_length = 10
for y in range(1440, 9999):
    beam_found = False
    for x in range(min_x, max_x):
        if last_first_x_in_row != None and x > (last_first_x_in_row+2) and (y-1) in y_max and x < y_max[y-1]:
            continue

        output = execute(x,y)
        if output == 1:
            if not beam_found:
                last_first_x_in_row = x
                if (y-100) in y_max:
                    width = y_max[y-99] - x
            beam_found = True
        min_x = x if not beam_found else min_x
            
        if beam_found and output == 0:
            y_max[y] = x - 1
            max_x = x + 5
            break

    to_rm = []
    for k in column_streak:
        if k < min_x:
            to_rm.append(k)

    for k in to_rm:
        del column_streak[k]


    if width >= 99:
        a, b = last_first_x_in_row, y - 99
        print("Part 2 solution : %d" % (10000 * a + b))
        break 
