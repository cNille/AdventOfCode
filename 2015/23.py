print(chr(27)+'[2j')
print('\033c', end='')
f = open('23.input', 'r')
# f = open('23.test', 'r')
lines = [x.strip() for x in f.readlines()]


a = b = 0
i = 0
a = 1
while i < len(lines):
    line = lines[i]
    print(line)

    if line.startswith('hlf'):
        _, r = line.split()
        if r == 'a':
            a //= 2
        else:
            b //= 2
    elif line.startswith('tpl'):
        _, r = line.split()
        if r == 'a':
            a *= 3
        else:
            b *= 3
    elif line.startswith('inc'):
        _, r = line.split()
        if r == 'a':
            a += 1
        else:
            b += 1
    elif line.startswith('jmp'):
        _, r = line.split()
        r = int(r)
        i += r
        continue
    elif line.startswith('jie'):
        _, r, o = line.split()
        o = int(o)
        if r == 'a,' and a % 2 == 0:
            i += o
            continue
        elif r == 'b,' and b % 2 == 0:
            i += o
            continue
    elif line.startswith('jio'):
        _, r, o = line.split()
        o = int(o)
        if r == 'a,' and a == 1:
            i += o
            continue
        elif r == 'b,' and b == 1:
            i += o
            continue
    i += 1
    print('Register:', a, b)

print('Result:', a, b)
