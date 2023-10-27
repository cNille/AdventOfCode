from heapq import heappush, heappop
print(chr(27)+'[2j')
print('\033c', end='')
lines = open('./24_day/my.input', 'r').read().split('\n')
lines = lines[:-1]

test = [
    '0/2',
    '2/2',
    '2/3',
    '3/4',
    '3/5',
    '0/1',
    '10/1',
    '9/10'
]

# lines = test

ports = set(lines)
start_ports = set(["0/0"])

queue = []
for port in start_ports:
    strength = sum([int(p) for p in port.split('/')])
    heappush(queue, (-strength, port, port))

max_strength = 0
max_length = 0
max_length_strength = 0

count = 0
bridges = set()
while len(queue) > 0:

    strength, port, path = heappop(queue)
    strength = -strength
    if strength >= max_strength:
        max_strength = strength
    if len(path.split('/')) > max_length:
        max_length = len(path.split('/'))
        max_length_strength = strength

    a1, b1 = port.split('/')
    for port2 in ports:
        a2, b2 = port2.split('/')
        rev_port = "{}/{}".format(b2, a2)
        if rev_port not in path and port2 not in path:
            new_strength = strength + int(a2) + int(b2)
            if b1 == a2:
                new_port = "{}/{}".format(a2, b2)
                new_path = path + '->' + new_port
                heappush(queue, (-new_strength, new_port, new_path))
            if b1 == b2 and a2 != b2:
                new_port = "{}/{}".format(b2, a2)
                new_path = path + '->' + new_port
                heappush(queue, (-new_strength, new_port, new_path))


print()
print("Max strength:", max_strength)
print("Max length strength:", max_length_strength)
