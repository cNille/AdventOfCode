print(chr(27)+'[2j')
print('\033c')
f = open('02.input', 'r')
#f = open('02.test', 'r')
content = [x.strip() for x in f.readlines()]
lines = content


maxes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

result = 0
result2 = 0
for line in lines:
    #print(line)
    line = line.split(':')
    sets = line[1].split(';')
    game_id = int(line[0].split(' ')[1])
    minimum = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    possible = True
    for s in sets:
        cubes = s.split(',')
        for c in cubes:
            # For each value of maxes 
            # check if it is in the range
            cube_count = int(c.strip().split(' ')[0])
            color = c.strip().split(' ')[1]
            minimum[color] = minimum[color] if minimum[color] > cube_count else cube_count
            for k, v in maxes.items():
                if k in c:
                    
                    if cube_count > v:
                        possible = False
                        break
    if possible:
        result += game_id
    
    power = 1   
    print(minimum)
    for k, v in minimum.items():
        power *= v
    result2 += power

    print("Game id: {}, possible: {}, with power: {}".format(game_id, possible, power))

print("Result: {}".format(result))
print("Result2: {}".format(result2))


