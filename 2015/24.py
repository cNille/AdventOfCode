from itertools import combinations
print(chr(27)+'[2j')
print('\033c', end='')
f = open('24.input', 'r')
# f = open('24.test', 'r')
lines = [x.strip() for x in f.readlines()]
packages = [int(x) for x in lines]
packages.sort(reverse=True)

print(packages)
print(len(packages))
total = sum(packages)
third = total // 3
fourth = total // 4
print(total)
print(third)
print(fourth)
fourth_packages = len(packages) // 4


# Part 1
fewest_packages = 2
while True:
    print('Fewest', fewest_packages)

    combs = combinations(packages, fewest_packages)
    group1 = []
    for comb in combs:
        tot = sum(comb)
        if tot == third:
            group1.append(comb)

    min_qe = 999999999999
    for g in group1:
        qe = 1
        for x in g:
            qe *= x
        if qe < min_qe:
            min_qe = qe
    if min_qe != 999999999999:
        print('Part 1:', min_qe)
        break
    fewest_packages += 1

# Part 2
fewest_packages = 2
while True:
    print('Fewest', fewest_packages)

    combs = combinations(packages, fewest_packages)
    group1 = []
    for comb in combs:
        tot = sum(comb)
        if tot == fourth:
            group1.append(comb)

    min_qe = 999999999999
    for g in group1:
        qe = 1
        for x in g:
            qe *= x
        if qe < min_qe:
            min_qe = qe
    if min_qe != 999999999999:
        print('Part 2:', min_qe)
        break
    fewest_packages += 1
