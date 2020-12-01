from itertools import permutations
f = open('test2', 'r')
f = open('01.input', 'r')

content = [int(x.strip()) for x in f.readlines()]


def part1(arr):
    rests = {}

    for x in arr:
        rest = 2020 - x
        if x in rests:
            return rest * x
        else:
            rests[rest] = True 
    return "not found"


#print(part1(content))

perm = permutations(content, 2)
newList = []

for x in perm:
    newList.append((x[0]+x[1], x))

def part2(arr1, arr2):
    rests = {}
    for x in arr1:
        rests[x[0]] = x[1]

    for x in arr2:
        rest = 2020 - x
        if rest in rests:
            print(x, rests[rest][0] , rests[rest][1])
            print(x * rests[rest][0] * rests[rest][1])
            return rest * x
    return "not found"
print(part2(newList, content))
