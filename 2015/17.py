print(chr(27)+'[2j')
print('\033c', end='')
f = open('17.input', 'r')
lines = [x.strip() for x in f.readlines()] 

containers = [int(x) for x in lines]
containers.sort(reverse=True)

# Part 1
# find all combinations of containers that sum to 150
def find_combinations(containers, target, used):
    if target == 0:
        return [used]
    if target < 0:
        return []
    if len(containers) == 0:
        return []
    return find_combinations(containers[1:], target, used) + find_combinations(containers[1:], target - containers[0], used + [containers[0]])

combinations = find_combinations(containers, 150, [])
print("Solution part 1:", len(combinations))


# Part 2
# find the minimum number of containers that sum to 150
sizes = [len(x) for x in combinations]
min_size = min(sizes)
print("Solution part 2:", sizes.count(min_size))
