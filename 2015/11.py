# 1. Passwords must include one increasing straight of at least three letters, 
#like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
def req1(x):
    if len(x) < 3:
        return False
    if ord(x[0]) - ord(x[1]) == -1 and ord(x[1]) - ord(x[2]) == -1:
        return True
    else:
        return req1(x[1:])

# 2. Passwords may not contain the letters i, o, or l, as these letters can be 
#mistaken for other characters and are therefore confusing.
def req2(x):
    return (
        'i' not in x  and
        'o' not in x  and
        'l' not in x
    )

# 3. Passwords must contain at least two different, non-overlapping pairs of 
#letters, like aa, bb, or zz.
def req3(x):
    count = 0
    overlap = False
    for i in range(0,len(x)-1):
        if overlap:
            overlap = False
            continue
        if x[i] == x[i+1]:
            count += 1
            overlap = True
    return count >= 2

def incr(x):
    if len(x) == 0:
        return ''
    elif x[-1] == 'z':
        return incr(x[:-1]) + 'a'
    else:
        return x[:-1] + chr(1 + ord(x[-1])) 

data = 'cqjxjnds'
while(True):
    data = incr(data)
    if (
        req2(data) and
        req1(data) and
        req3(data)
    ):
        break

print('Part 1: %s' % data)

def smart_incr(x):
    if len(x) == 0:
        return ''
    elif x[-1] == 'z':
        return incr(x[:-1]) + 'a'
    else:
        new_char = chr(1 + ord(x[-1]))
        if new_char in ['o', 'i', 'l']:
            new_char = chr(1 + ord(x[-1]))
        return x[:-1] + new_char

while(True):
    data = smart_incr(data)
    if (
        req2(data) and
        req1(data) and
        req3(data)
    ):
        break

print('Part 2: %s' % data)
