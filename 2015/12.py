import re
data =  open('12.input', 'r').readline().strip()

res = 0
pattern = re.compile(r'([0-9\-]+)')
for x in re.findall(pattern,data):
    res += int(x)
print("Part 1: %d" % res)


def clear(txt, pos):
    count = 0
    left = pos 
    while left > 0 and count >= 0:
        left -= 1
        if txt[left] == '{':
            count -= 1
        elif txt[left] == '}':
            count += 1
    count = 0
    right = pos 
    while right < len(txt) and count >= 0:
        right += 1
        if txt[right] == '}':
            count -= 1
        elif txt[right] == '{':
            count += 1
    return txt[:left+1] + txt[right:]
        

done = False
while not done:
    done = True 
    for i in range(len(data)):
        if data[i:i+5] == ':"red':
            data = clear(data, i)
            done = False
            break
    if done:
        break

res = 0
pattern = re.compile(r'([0-9\-]+)')
for x in re.findall(pattern,data):
    res += int(x)
print("Part 2: %d" % res)
