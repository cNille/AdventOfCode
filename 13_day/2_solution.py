import re

data = open('my.input').read()
layers = re.findall(r'(\d+):\s(\d+)\n', data) # find all digits
layers = [(int(l[0]), int(l[1])) for l in layers] # Convert str to int in tuple
def got_caught(index, depth, delay):
    return (index + delay) % ((depth-1) * 2) == 0

delay = 0
while True:
    severity = [l[0] * l[1]  for l in layers if got_caught(l[0],l[1], delay)]
    if delay % 100000 == 0:
        print('Delay:', delay )
    if len(severity) == 0:
        print('Success!! Delay:', delay)
        exit()
    delay += 2     
