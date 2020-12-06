# Read in groups from file
f = open('06.input', 'r')
data = f.read()
groups = data.strip().split('\n\n')

def part1(groups):
    total = 0
    for group in groups:
        # 1. Concatinate rows to one-line by replacing \n
        # 2. Extract unique characters by creating a set
        # 3. Count size of set
        total += len(set(group.replace('\n', '')))
    return total

def part2(groups):
    total = 0
    for group in groups:
        # Use dictionary to count occurrences of letters
        occurrences = {}
        for letter in group:
            if letter not in occurrences:
                occurrences[letter] = 0
            occurrences[letter] +=1 

        # Amount of persons in the group will be one more than new-lines.
        person_count = occurrences['\n'] + 1 if '\n' in occurrences else 1 

        # Count all letters that occur same amount as persons in group
        all_answers = [x for x in occurrences.values() if x == person_count]
        total += len(all_answers)
    return total

print "Solution part 1: %d" % part1(groups)
print "Solution part 2: %d" % part2(groups)

# Alternative solutions

def part1set(groups):
    sets = [map(set, group.splitlines()) for group in groups]
    unions = [set.union(*s) for s in sets]
    return sum(map(len, unions))
print part1set(groups)

def part2set(groups):
    sets = [map(set, group.splitlines()) for group in groups]
    intersections = [set.intersection(*s) for s in sets]
    return sum(map(len, intersections))
print part2set(groups)

def part2(groups):
    total = 0
    for group in groups:
        # Use dictionary to count occurrences of letters
        occurrences = {}
        for letter in group:
            if letter not in occurrences:
                occurrences[letter] = 0
            occurrences[letter] +=1 

        # Amount of persons in the group will be one more than new-lines.
        person_count = occurrences['\n'] + 1 if '\n' in occurrences else 1 

        # Count all letters that occur same amount as persons in group
        all_answers = [x for x in occurrences.values() if x == person_count]
        total += len(all_answers)
    return total


from collections import Counter
def part2count(groups):
    total = 0
    for g in groups:
        letter_counter = Counter(g)
        person_count = len(g.split('\n'))
        all_answers = [x for x in letter_counter.values() if x == person_count]
        total += len(all_answers)
    return total

def part1func(groups):
    return sum([
        len(set(g.replace('\n','')))
        for g
        in groups
    ])

def part2func(groups):
    return sum([
        len([x for x in Counter(g).values() if x == len(g.split('\n'))])
        for g
        in groups
    ])
