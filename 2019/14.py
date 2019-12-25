from fractions import gcd

data = [x.strip() for x in open('14.input2', 'r').readlines()]

for d in data:
    print d
print '-'*50

recipe = {}
for d in data:
    ing, res = d.split(' => ')

    amount, name = res.split(' ')
    required_ingredients = [a.split(' ') for a in ing.split(', ')]
    required_ingredients = [(int(a),b) for a,b in required_ingredients]
    req = {}
    for a,b in required_ingredients:
        req[b] = int(a)
        
    if name in recipe:
        print "ALREADY IN GAME", name, recipe
    recipe[name] = (int(amount), req)

print(recipe)

def requires(recipe, ingredient_name, requested_amount, level, unused_ingredients):
    print('-'*40)
    print "CHECKING (%d) %s %d" % (level, ingredient_name, requested_amount)
    amount, ingredients = recipe[ingredient_name]
    print "Ingredients: ", amount, ingredients
    
    produced = {}
    used = {}
    if ingredient_name not in produced:
        produced[ingredient_name] = 0
    for name in ingredients:
        #print name
        if name in recipe:
            #print "in recipe", name
            produced_amount, _ = recipe[name]
            p, u = requires(recipe, name, ingredients[name], level+1, unused_ingredients)

            for x in p:
                if x not in produced:
                    produced[x] = 0
                produced[x] += p[x]
            for x in u:
                if x not in unused_ingredients:
                    unused_ingredients[x] = {}
                for y in x:
                    if y not in unused_ingredients[x]:
                        unused_ingredients[x][y] = 0
                    unused_ingredients[x][y] += u[x][y]
        else:
            print "not in recipe", name, requested_amount, unused_ingredients

            if ingredient_name not in unused_ingredients:
                unused_ingredients[ingredient_name] = {}
            if  name not in unused_ingredients[ingredient_name]:
                unused_ingredients[ingredient_name][name] = 0

            unused = unused_ingredients[ingredient_name][name]

            produce_amount, required =  recipe[ingredient_name]
            required = required[name]
            #print produce_amount, required
            
            p = unused if unused > produce_amount else produce_amount - unused
            produced_ing = ((p) / requested_amount) * required
            print 123, produced_ing
            # TODO:
            # Figure out how to handle big requested amounts when there is a lot of unused
            unused = produced_ing - requested_amount

            unused_ingredients[ingredient_name][name] += unused 

            if name not in produced:
                produced[name] = 0
            produced[name] += produced_ing

    #print "Returning", produced, unused_ingredients
    return produced, unused_ingredients
    

produced, _ = requires(recipe, "FUEL", 1, 1, {})

#print '@' * 20
#print produced
#print '@' * 20

print "Requires:"
for p in produced:
    if produced[p] >0:
        print "\t%s: %d " % (p, produced[p])

