import re

data = open('my.input').read().split()[0]
data = re.sub(r'(!.)', '', data)
data = re.findall(r'(<.*?>)', data)

count = 0
for d in data:
    count += len(d) - 2
    print(count, d)
