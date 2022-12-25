print(chr(27)+'[2j')
print('\033c')
f = open('21.test', 'r')
#f = open('21.input', 'r')
lines = [x.strip() for x in f.readlines()]
print("Day 21")

def game(default=0):
    registers = {}
    values = {}
    root_deps = ('none', 'none')
    for l in lines:
        r, op = l.split(': ')
        registers[r] = op
        ops = op.split(' ')
        if len(ops) == 1:
            if r == 'humn' and default is not 0:
                values[r] = int(default)
            else:
                values[r] = int(op)
        else:
            left, operator, right = ops
            if r == 'root':
                root_deps = (left,right)

    while len(values) < len(registers):
        for r in registers:
            if r in values:
                continue
            op = registers[r]
            ops = op.split(' ')
            left, operator, right = ops
            if left not in values or right not in values:
                continue
            if operator == '*':
                values[r] = values[left] * values[right]
            elif operator == '/':
                values[r] = values[left] / values[right]
            elif operator == '+':
                values[r] = values[left] + values[right]
            elif operator == '-':
                values[r] = values[left] - values[right]
            else:
                print("Unrecog:", operator)
                exit()
    print(values)
    return values, root_deps

values, (l,r) = game()
print("Part 1 solution:", int(values['root']))

prev = 0
i = 0
while True:
    i += 1
    values, (l,r) = game(i)
    l_val = int(values[l])
    r_val = int(values[r])
    is_correct = l_val == r_val
    if is_correct: 
        print("Part 2 solution:", i)
        break
    else:
        if prev != 0 and prev != l_val:
            diff = (r_val - l_val)
            rate = (l_val - prev)
            i +=  diff // rate 
        prev = l_val
