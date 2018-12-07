import operator

# Sorting
def sort_dic_by_keys(d):
    return sorted(d.items(), key=operator.itemgetter(0))
def sort_dic_by_values(d):
    return sorted(d.items(), key=operator.itemgetter(1))

# -----------------------------------------------------------------------------

# Import data
data = [x.strip() for x in open('day_07_input.txt','r').readlines()]

conditions = {}
for d in data:
    words = d.split()
    c = words[7]
    letter = words[1]
    if c not in conditions:
        conditions[c] = []
    conditions[c].append(letter)

print('Condition relations')
for c in conditions:
    print('\t %s: %s' % (c, ', '.join(conditions[c])))
print('-'*80)

# Find letter not dependent
all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
starting = [l for l in all_letters if l not in conditions]

print('Letters without conditions: %s' % ', '.join(starting))


 # Part 1
 # -------------------------------------------------------------------------
def part1():
    steps = []
    wip = sorted(starting, reverse=True)
    curr = wip.pop()
    while True:
        for c in conditions:
            if curr in conditions[c]:
                conditions[c].remove(curr)
            if len(conditions[c]) == 0:
                wip.append(c)
                conditions[c] = [-1] # nullify its conditions.

        # Breaking condition
        if len(wip) == 0:
            steps.append(curr)
            break

        # Add current to steps
        if curr not in steps:
            steps.append(curr)

        # Re-sort WIP and take the last element as current
        wip = sorted(wip, reverse=True)
        curr = wip.pop()

    print('Part 1: Result is %s' % ''.join(steps))

 # Part 2
 # -------------------------------------------------------------------------

def part2():
    steps = []
    steps_left = all_letters
    wip = sorted(starting, reverse=True)
    wip = starting
    time = {}
    for s in starting:
        time[s] = all_letters.index(s) + 61
    i = 0

    while i < 1000:
        rm_w = []
        for w in wip:
            if w in time and time[w] <= i:
                if w not in steps:
                    steps.append(w)
                rm_w.append(w)
                steps_left = steps_left.replace(w,'')
        for r in rm_w:
            wip.remove(r)
            if r in conditions:
                del conditions[r]

        for c in conditions:
            conditions_left = [cond for cond in conditions[c] if cond in steps_left]
            if len(conditions_left) == 0 and c not in time:
                time[c] = i + all_letters.index(c) + 61

            if c in time and time[c] >= i and len(conditions_left) == 0 and len(wip) < 6 and c not in wip:
                wip.append(c)


        wip = sorted(wip, reverse=True)

        # Breaking condition
        if len(steps) >= 26 or i > 2000:
            print('Part 2: Result in %d iterations' % i)
            break
        i += 1

part1()
# part2()
