lines = [x.strip() for x in open('21.test', 'r').readlines()]
lines = [x.strip() for x in open('21.input', 'r').readlines()]

allergenes = {} 
all_ingredients = set()

for line in lines:
    allergene_list = "".join(line.split('(contains ')[1])[:-1].split(', ')
    ingredient_list = set("".join(line.split('(')[0])[:-1].split(' '))
    all_ingredients = all_ingredients.union(ingredient_list) 
    for a in allergene_list:
        if a not in allergenes:
            allergenes[a] = set(ingredient_list)
        else:
            allergenes[a] = allergenes[a].intersection(set(ingredient_list))


for a in allergenes:
    print a, allergenes[a]


count = 0
for line in lines:
    ingredient_list = set("".join(line.split('(')[0])[:-1].split(' '))

    for i in ingredient_list:
        no_allergene = True
        for a in allergenes:
            if i in allergenes[a]:
                no_allergene = False
                break
        if no_allergene:
            count += 1

print "Solution part 1: %d" % count

while True:
    unique = []
    for a in allergenes:
        if len(allergenes[a]) == 1:
            unique.append(list(allergenes[a])[0])
    if len(unique) == len(allergenes):
        break

    for a in allergenes:
        if len(allergenes[a]) > 1:
            allergenes[a] = allergenes[a].difference(unique)
    
allergenes = [(a, list(allergenes[a])[0]) for a in allergenes]
allergenes.sort()
allergenes = [a[1] for a in allergenes]
result = ",".join(allergenes)

print "Solution part 2: %s" % result
