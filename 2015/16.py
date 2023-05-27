print(chr(27)+'[2j')
print('\033c', end='')
f = open('16.input', 'r')
lines = [x.strip() for x in f.readlines()] 

ticker_tape = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".strip().split('\n')
message = {}
for t in ticker_tape:
    message[t.split(':')[0]] = int(t.split(':')[1])


# Part 1
for line in lines:
    head, tail = line.split(': ', 1)
    sue_id = int(head.split(' ')[1])
    parts = tail.split(', ')
    is_match = True
    for part in parts:
        key, value = part.split(': ')
        if message[key] != int(value):
            is_match = False
            break
    if is_match:
        print('Solution part 1:', sue_id)
        break


# Part 2
for line in lines:
    head, tail = line.split(': ', 1)
    sue_id = int(head.split(' ')[1])
    parts = tail.split(', ')
    is_match = True
    for part in parts:
        key, value = part.split(': ')

        if key in ['cats', 'trees']: 
            if message[key] >= int(value):
                is_match = False
                break
        elif key in ['pomeranians', 'goldfish']: 
            if message[key] <= int(value):
                is_match = False
                break
        else: 
            if message[key] != int(value):
                is_match = False
                break
    if is_match:
        print('Solution part 2:', sue_id)
        break



