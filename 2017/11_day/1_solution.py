from collections import Counter

path = open('my.input').read().split()[0].split(',')

counter = Counter(path)

print(counter)

deltaN = abs(counter['n'] - counter['s'])
deltaNe = abs(counter['ne'] - counter['sw'])
deltaNw = abs(counter['nw'] - counter['se'])

print('DeltaN',deltaN)
print('DeltaNe',deltaNe)
print('DeltaNw',deltaNw)

print('Result', deltaN + max(deltaNw, deltaNe))
