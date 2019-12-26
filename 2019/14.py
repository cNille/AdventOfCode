from fractions import gcd
from collections import deque
from collections import defaultdict
from math import ceil
data = [x.strip() for x in open('14.input', 'r').readlines()]

recipes = {}
for d in data:
    ing, res = d.split(' => ')
    amount, name = res.split(' ')
    required_ingredients = [a.split(' ') for a in ing.split(', ')]
    required_ingredients = [(int(a),b) for a,b in required_ingredients]
    req = {}
    for a,b in required_ingredients:
        req[b] = int(a)
    recipes[name] = (int(amount), req)

def calculate(amount, recipes):
    orders = deque()
    leftovers = defaultdict(int)
    required = 0
    orders.append(("FUEL", amount))

    while len(orders) > 0:
        order = orders.popleft()
        name, amount = order

        if name == "ORE":
            required += amount
        elif amount <= leftovers[name]:
            leftovers[name] -= amount
        else:
            needed = amount - leftovers[name]

            recipe = recipes[name]
            produced, ingredients = recipe

            factor = ceil( needed / produced )
            for i_name in ingredients:
                orders.append((i_name, ingredients[i_name] * factor))
            leftover = (factor * produced) - needed
            leftovers[name] = leftover
    return required
        
part1 = calculate(1, recipes)
print "Part 1: %d " % part1

max_ore = 1000000000000
max_succeeded = 0
curr = max_ore / part1
alpha = part1
max_found = False
for _ in range(100):
    #print "Trying: %d, alpha: %d, current max: %d " % (curr, alpha, max_succeeded)
    required = calculate(curr, recipes)
    if required > max_ore:
        curr -= alpha
        alpha = max(alpha / 2, 1)
        continue
    max_succeeded = round(max(max_succeeded, curr))
    curr += alpha

print "Part 2: %d" % max_succeeded
