print(chr(27)+'[2j')
print('\033c', end='')
#f = open('15.input', 'r')
f = open('15.test', 'r')
lines = [x.strip() for x in f.readlines()] 

ingredients = {}
for line in lines:
    line = line.replace(',', '')
    line = line.replace(':', '')
    line = line.split()
    ingredients[line[0]] = {}
    ingredients[line[0]]['capacity'] = int(line[2])
    ingredients[line[0]]['durability'] = int(line[4])
    ingredients[line[0]]['flavor'] = int(line[6])
    ingredients[line[0]]['texture'] = int(line[8])
    ingredients[line[0]]['calories'] = int(line[10])

def fn1(ingredients, spoons):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for key in ingredients:
        capacity += ingredients[key]['capacity'] * spoons[key]
        durability += ingredients[key]['durability'] * spoons[key]
        flavor += ingredients[key]['flavor'] * spoons[key]
        texture += ingredients[key]['texture'] * spoons[key]
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    return capacity * durability * flavor * texture

def fn2(ingredients, spoons):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for key in ingredients:
        capacity += ingredients[key]['capacity'] * spoons[key]
        durability += ingredients[key]['durability'] * spoons[key]
        flavor += ingredients[key]['flavor'] * spoons[key]
        texture += ingredients[key]['texture'] * spoons[key]
        calories += ingredients[key]['calories'] * spoons[key]
    if calories != 500:
        return 0
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    return capacity * durability * flavor * texture

def fn3(ingredients, spoons, fn):
    nextKey = None
    for key in ingredients:
        if key not in spoons:
            nextKey = key
            break
    if nextKey is None:
        return fn(ingredients, spoons)

    usedSpoons = 0
    for s in spoons:
        usedSpoons += spoons[s]

    maxScore = 0
    for i in range(0, 100 - usedSpoons + 1):
        newSpoons = {}
        for s in spoons:
            newSpoons[s] = spoons[s]
        newSpoons[nextKey] = i
        score = fn3(ingredients, newSpoons, fn)
        if score > maxScore:
            maxScore = score    

    return maxScore

spoons = {}
print("Solution part 1:", fn3(ingredients, spoons, fn1))
print("Solution part 2:", fn3(ingredients, spoons, fn2))
