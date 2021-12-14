print(chr(27)+'[2j')
print('\033c')
from collections import Counter
from itertools import permutations
from math import ceil
f = open('14.test', 'r')
# f = open('14.input', 'r')
lines = [x.strip() for x in f.readlines()]
#print(lines[:10])

rules = {}
for line in lines[2:]:
    a,b = line.split(' -> ')
    rules[a] = b

polymer_template = lines[0]
polymer = polymer_template

def part1(polymer):
    STEPS = 10
    #print("Template: %s" % polymer)
    for step in range(1, STEPS + 1):
        #print('Step %d' % step)

        next_polymer = ''
        for i, char in enumerate(polymer[:-1]):
            pair = "%s%s" % (char, polymer[i+1])
            if pair in rules:
                next_polymer += "%s%s" % (char, rules[pair])
            else:
                next_polymer += char
        polymer = next_polymer + polymer[-1]
        # print('----------')
        # print("After step %d: %d %s" % (step, len(polymer), ''))

    counter = Counter(polymer)
    commons = counter.most_common()
    common_char, common_count = commons[0]
    least_char, least_count = commons[-1]
    print("Solution part 1: %d" % (common_count - least_count))
part1(polymer)
        
cache = {}
def count_commons(pair, steps, full):
    #print("-" * (full-steps) + "Fetching", pair, steps)
    if (pair,steps) in cache:
        return cache[(pair,steps)]
    if(steps == 1):
        return Counter(pair[0] + rules[pair]  + pair[1])

    counter = Counter() 
    counter += count_commons(pair[0] + rules[pair], steps - 1, full)
    counter += count_commons(rules[pair] + pair[1], steps - 1, full)
    counter -= Counter(rules[pair])

    cache[(pair,steps)] = counter
    return counter

def part2(polymer):
    STEPS = 40 
    #print("Template: %s" % polymer)

    pairs = zip(polymer, polymer[1:])
    counter = Counter(polymer[-1])
    for (a,b) in pairs:
        pair = a + b 
        counter += count_commons(pair, STEPS, STEPS)
        counter -= Counter(b)
    commons = counter.most_common()
    common_char, common_count = commons[0]
    least_char, least_count = commons[-1]
    print("Solution part 2: %d" % (common_count - least_count))
part2(polymer)


