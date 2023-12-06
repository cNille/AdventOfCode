print(chr(27)+'[2j')
print('\033c')
f = open('01.input', 'r')
#f = open('01.test', 'r')
content = [x.strip() for x in f.readlines()]
#calories = [int(x) if x != '' else 0 for x in content]
lines = content
import re
print("== part1 ==")


def parse_line(x, idx, part2=False):
    if x[idx].isdigit():
        return x[idx]
    elif part2 and x[idx:].startswith('one'):
        return '1'
    elif part2 and x[idx:].startswith('two'):
        return '2' 
    elif part2 and x[idx:].startswith('three'):
        return '3' 
    elif part2 and x[idx:].startswith('four'):
        return '4' 
    elif part2 and x[idx:].startswith('five'):
        return '5' 
    elif part2 and x[idx:].startswith('six'):
        return '6' 
    elif part2 and x[idx:].startswith('seven'):
        return '7' 
    elif part2 and x[idx:].startswith('eight'):
        return '8' 
    elif part2 and x[idx:].startswith('nine'):
        return '9' 
    return None

def last_digit(x:str, part2=False):
    idx = len(x) - 1
    while idx >= 0:
        digit = parse_line(x, idx, part2)
        if digit is not None:
            return digit    
        idx -= 1
    return None 

def first_digit(x:str, part2=False):
    idx = 0
    while idx < len(x):
        digit = parse_line(x, idx, part2)
        if digit is not None:
            return digit    
        idx += 1
    return None 

def solve(part2=False):
    result = 0
    for x in lines:

        a = first_digit(x, part2)
        b = last_digit(x, part2)
        if a is None or b is None:
            print('error', a, b)
            exit()
        digit = int(a + b)
        result += digit
    return result


result1 = solve()
print("Part 1 solution: %d" % result1)
result1 = solve(True)
print("Part 2 solution: %d" % result1)
