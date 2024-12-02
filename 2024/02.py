print(chr(27)+'[2j')
print('\033c')
f = open('02.input', 'r')
lines = [x.strip() for x in f.readlines()]

def is_report_safe(nbr):
    # Get diffs
    diffs = [a - b for (a,b) in zip(nbr, nbr[1:])]

    # Ensure diff is between 1 and 3
    within_range = [d for d in diffs if 1 <= abs(d) and abs(d) <= 3]
    if len(within_range) != len(diffs):
        return False

    # Ensure diffs are either all positive or all negative
    positive = [d for d in diffs if d > 0]
    if len(positive) == len(diffs):
        return True
    negative = [d for d in diffs if d < 0]
    if len(negative) == len(diffs):
        return True
    return False

result1 = 0
result2 = 0
for line in lines:
    nbr = [int(x) for x in line.split()]
    is_safe = is_report_safe(nbr)
    if is_safe:
        result1 += 1
        result2 += 1
        continue
    # Part 2
    for i in range(len(nbr)):
        is_safe = is_report_safe(nbr[:i] + nbr[i+1:] )
        if is_safe:
            result2 += 1
            break

print('Solution part 1:', result1)
print('Solution part 2:', result2)
