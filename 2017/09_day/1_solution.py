import re

data = open('my.input').read().split()[0]

data = re.sub(r'(!.)', '', data)
data = re.sub(r'(<.*?>)', '', data)
data = re.sub(r',', '', data)

points = 1
total = 0
for c in data:
    if c == '{':
        total += points
        points += 1
    if c == '}':
        points -= 1
print(total)
