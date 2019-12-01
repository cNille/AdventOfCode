data = open('05.input').readlines()


# Part 1
count = 0
bad_chars = [ 'ab', 'cd', 'pq', 'xy' ]
vowels = 'aeiou' 

for line in data:

    # No bad chars
    bad = [1 for b in bad_chars if b in line]
    if len(bad) > 0:
        continue

    # Twice in a row
    twice = False
    for idx, c in enumerate(line):
        if idx > 0 and line[idx-1] == c:
            twice = True
    
    if not twice:
        continue

    # Vowels
    v = 0
    v = sum([1 for c in line if c in vowels])
    if v < 3:
        continue

    count += 1

print("Part 1: %d" % count)


# Part 2
count = 0
bad_chars = [ 'ab', 'cd', 'pq', 'xy' ]
vowels = 'aeiou' 

for line in data:

    # Repeat 
    repeat = False
    for idx, c in enumerate(line):
        if idx > 1 and line[idx-2] == c:
            repeat = True
    
    if not repeat:
        continue

    # Pair 
    pair = False
    for idx, c in enumerate(line):
        p = line[idx-1] + c
        if idx > 1 and (
            p in line[:idx-1]
            or
            p in line[idx+1:]
        ):
            pair = True
    if not pair:
        continue

    count += 1

print("Part 2: %d" % count)
