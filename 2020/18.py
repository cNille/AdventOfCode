import re

lines = [
    '1 + 2 * 3 + 4 * 5 + 6',
    '1 + (2 * 3) + (4 * (5 + 6))',
    '2 * 3 + (4 * 5)',
    '5 + (8 * 3 + 9 + 3 * 4 * 3)',
    '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
    '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',
]
lines = [x.strip() for x in open('18.input', 'r').readlines() if x != '']

def end_paranthesis(expression):
    count = 0
    for i, ch in enumerate(expression):
        if ch == '(':
            count += 1
        if ch == ')':
            count -= 1
        if count == 0:
            break
    return i

def math(expression, verbose=False):
    if verbose:
        print "Math Expression:", expression
    # First calculate all paranthesis in a recursive call
    i = 0
    new_expression = ''
    while i < len(expression):
        ch = expression[i]
        if ch == '(':
            end = end_paranthesis(expression[i:])  
            new_expression += str(math(expression[i+1: end+i]))
            i += end 
        else:
            new_expression += ch
        i += 1 
    expression = new_expression

    # Evaluate all additions 
    i = 0
    if verbose:
        print 'after paranthesis', expression
    match_found = True
    while match_found:
        match_found = False
        for a,b in re.findall(r'(\d+)\+(\d+)', expression):
            match_found = True
            addition = int(a) + int(b)
            expression = expression.replace('%s+%s'%(a,b), str(addition), 1)
            break

    if verbose:
        print 'after sum', expression
    # Evaluate all multiplications 
    match_found = True
    while match_found:
        match_found = False
        for a,b in re.findall(r'(\d+)\*(\d+)', expression):
            match_found = True
            product = int(a) * int(b)
            expression = expression.replace('%s*%s'%(a,b), str(product), 1)
            break

    if verbose:
        print 'after mul', expression
    return int(expression)

values = []
for line in lines:
    expression = line.replace(' ', '')
    value = math(expression)
    values.append(value)
print "Solution part 2: %d" %sum(values)

def part1(lines):
    def operate(a,b, op):
        return a * b if op == '*' else a + b 

    def math(expression):
        val = 0
        i = 0
        operator = '+'
        while i < len(expression):
            ch = expression[i]

            if ch == '(':
                end = end_paranthesis(expression[i:])  
                submath = expression[i+1: end+i]
                subvalue = math(submath)
                val = operate(val, subvalue, operator)
                i += end 
            elif ch in ['+', '*']:
                operator = ch
            else:
                digit = int(ch)
                val = operate(val,digit, operator)
            i += 1

        return val

    values = []
    for line in lines:
        values.append(math(line.replace(' ', '')))
    print "Solution part 1: %d " % sum(values)
part1(lines)
