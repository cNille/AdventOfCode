import re

data = open('my.input').read()
layers = re.findall(r'(\d+):\s(\d+)\n', data) # find all digits
layers = [(int(l[0]), int(l[1])) for l in layers] # Convert str to int in tuple
def got_caught(index, depth):
    return (index) % ((depth - 1) * 2) == 0

severity = [int(l[0]) * int(l[1]) for l in layers if got_caught(l[0],l[1])]
print('Result:', sum(severity))
