f = open('01.test', 'r')
f = open('01.input', 'r')
content = [int(x.strip()) for x in f.readlines()]

# O(n^2)
def part1slow(arr):
    for x in arr:
        for y in arr:
            if x + y == 2020:
                return x * y

# O(n)
def part1(arr):
    rests = set()

    for x in arr:
        rest = 2020 - x
        if rest in rests:
            return rest * x
        else: 
            rests.add(x)

print("Part 1 solution: %d" % part1(content))

# O(n^3)
def part2slow(arr):
    for x in arr:
        for y in arr:
            for z in arr:
                if x + y + z == 2020:
                    return x * y * z

# O(n^2 + n) => O(n^2)
def part2(arr):
    rests = {}
    for x in arr:
        for y in arr:
            rests[x + y] = x * y

    for x in arr:
        rest = 2020 - x
        if rest in rests:
            return x * rests[rest]

print("Part 2 solution: %d" % part2(content))

# def part1(arr):
#     rests = {}
#     for x in arr:
#         rest = 2020 - x
#         if x in rests:
#             return rest * x
#         else:
#             rests[rest] = True 
#     return "not found"
# 
# 
# print("Part 1: %d" % part1(content))
# 
# from itertools import permutations
# perm = permutations(content, 2)
# newList = []
# 
# for x in perm:
#     newList.append((x[0]+x[1], x))
# 
# def part2(arr1, arr2):
#     rests = {}
#     for x in arr1:
#         rests[x[0]] = x[1]
# 
#     for x in arr2:
#         rest = 2020 - x
#         if rest in rests:
#             return (x * rests[rest][0] * rests[rest][1])
#     return "not found"
# print("Part 2: %d" % part2(newList, content))
