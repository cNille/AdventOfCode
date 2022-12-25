print(chr(27)+'[2j')
print('\033c')
f = open('19.test', 'r')
f = open('19.input', 'r')
lines = [x.strip() for x in f.readlines()]
print("Day 19")
import copy
from itertools import permutations
#from functools import lru_cache

blueprints = []
for l in lines:
    b = l.split(': ')[1]
    r = b.split('. ')
    blueprint = {} 
    for robot in r:
        t = robot.split(' ')[1] 
        costs = robot.split(' costs ')[1].split(' and ')
        costs = tuple([cost.replace('.', '') for cost in costs])
        costs = [c.split() for c in costs] 
        blueprint[t] = [(int(c[0]), c[1]) for c in costs]
    blueprints.append(blueprint)

def inc_resources(resources, robots):
    new_resources = list(resources)
    for r, _ in enumerate(resources):
        new_resources[r] = resources[r] + 1 * robots[r]
    return tuple(new_resources)

def inc_robot(robots, robot_type):
    new_robots = list(robots) 
    new_robots[I[robot_type]] += 1
    return tuple(new_robots)

itr = 0
I = { 'ore': 0, 'clay': 1, 'obsidian': 2, 'geode': 3 }

def game(t, resources, robots):
    global blueprint, itr
    blueprint = blueprint if blueprint is not None else {}
    itr += 1

    # Can purchase
    purchase = []
    for b in ['geode', 'obsidian', 'clay', 'ore']:
        can_purchase = True
        for (cost, cost_type) in blueprint[b]:
            if cost <= resources[I[cost_type]]:
                continue
            can_purchase = False
            break
        if can_purchase:
            purchase.append(b)

    actions = []
    orig_robots = copy.deepcopy(robots)
    new_resources = inc_resources(resources, orig_robots)
    if 'geode' not in purchase:
        actions.append((t+1, new_resources, orig_robots))

    #for i in range(len(purchase)):
    #    perm = permutations(purchase, 1)
    if len(purchase) >= 2 and 'ore' in purchase:
        purchase = [purchase[0], 'ore']
    for p in purchase[:2]:
        res2 = [r for r in new_resources] 
        new_robots = copy.deepcopy(robots)
        #p = [p]
        #for r in p:
        r = p
        for cost, cost_type in blueprint[r]:
            res2[I[cost_type]] -= cost
        new_robots = inc_robot(new_robots, r)
        
        actions.append((t+1, tuple(res2), new_robots))
            
    return actions

priority = ["geode", "obsidian", "clay", "ore"]
blueprint = None
results = []
for i, b in enumerate(blueprints):
    blueprint = b

    q = []
    max_geode = 0
    max_obsid = 0
    max_clay = 0
    max_ore = 0
    max_rob = (0,0,0,0) 
    robots =  (1,0,0,0) 
    resources =  (0,0,0,0) 
    MAX_T = 24
    reach = {}
    lvl = 0

    def get_max(res, rob):
        global max_ore, max_clay, max_obsid, max_geode, lvl, max_rob
        if(res[0] >= max_ore):
            max_ore = res[0]
            if lvl == 0:
                max_rob = rob
        if(res[1] >= max_clay):
            max_clay = res[1]
            if lvl < 1:
                max_rob = rob
                lvl +=1
            if lvl == 1:
                max_rob = rob
        if(res[2] >= max_obsid):
            max_obsid = res[2]
            if lvl < 2:
                lvl +=2
                max_rob = rob
            if lvl == 2:
                max_rob = rob
        if(res[3] >= max_geode):
            max_geode = res[3]
            if lvl < 3:
                lvl +=3
            if lvl == 3:
                max_rob = rob

    for t in range(MAX_T+1):
        reach[t] = set() 
    reach[0].add((0, resources, robots))

    print("-"*20)
    print('Blueprint', i+1)
    for t in range(0, MAX_T):

        count_obsid = 0
        prev_max = max_geode
        for (t1, res1, rob1) in reach[t]:
            new_actions = game(t1, res1, rob1)
            for (t2, res2, rob2) in new_actions:
                reach[t2].add((t2, res2, rob2))
                get_max(res2, rob2)
                if res2[2] == 0:
                    count_obsid += 1
        print("%d reaches %d. Maxes at geode:%d, obsidian:%d, clay:%d, ore:%d. Count obsidian:%d" 
              % (t, len(reach[t]), max_geode, max_obsid, max_clay, max_ore, count_obsid)
              + ". Robots:", max_rob 
        )
        #if prev_max == 0 and max_geode != 0:
        #    reach[t] = [x for x in reach[t] if x[1][3] != 0]
        

    geodes = [res[3] for (_, res, _) in reach[len(reach)-1]]
    geodes.sort()
    print("Finished with blueprint", i, ", score: ", geodes[-1])
    res = (i+1) * geodes[-1]
    results.append(res)


print('-'*80)
print('FINISHED')
for i,v in enumerate(results):
    print("Blueprint %d: %d" % (i+1, v))

print("Total result:", sum(results))
