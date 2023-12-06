print(chr(27)+'[2j')
print('\033c')
f = open('05.input', 'r')
#f = open('05.test', 'r')
content = [x.strip() for x in f.readlines()]
lines = content

print('Day 05:')
RED = '\033[31m'
RESET = '\033[0m'

seeds = lines[0].split(': ')[1].split()
seeds = [int(x) for x in seeds]

# Iterate lines from third line, and group them by empty lines
categories = []
category = []
for line in lines[2:]:
    if line == '':
        categories.append(category)
        category = []
    else:
        category.append(line)
categories.append(category)

def solve(seeds):
    result_seeds = []
    max_seed = max(seeds)
    lowest_seed = max_seed 
    low_start_seed = max_seed 
    for i, seed in enumerate(seeds):

        start_seed = seed

        for category in categories:
            ranges = category[1:]
            for r in ranges:
                destination, source, length = [int(x) for x in r.split()]
                if source <= seed < source + length:
                    seed = destination + seed - source
                    break
        if seed < lowest_seed:
            low_start_seed = start_seed
            lowest_seed = seed
    return low_start_seed, lowest_seed

# Part 1
_, part1 = solve(seeds)
print("Part1:", part1)

seed_ranges = []
for i in range(0, len(seeds), 2):
    new_range = (seeds[i], seeds[i] +seeds[i+1]-1)
    seed_ranges.append(new_range)

min_s = 99999999999
seed1 = None
for seed_range in seed_ranges:
    print(len(seeds), seed_range)
    seed_list = range(seed_range[0], seed_range[1]+1)
    # Only use every 50000th seed
    seed_list = seed_list[::50000]
    seed, result1 = solve(seed_list)
    if result1 < min_s:
        seed1 = seed
        min_s = result1
print("Rough iteration:", seed1)


min_s = 99999999999

# Use seed1 as starting point
seed_list = range(seed1-100000, seed1)
seed, result1 = solve(seed_list)
if result1 < min_s:
    print('New lowest:', result1, seed)
    seed1 = seed
    min_s = result1
print("Part 2:", min_s)
