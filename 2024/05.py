print(chr(27)+'[2j')
print('\033c')
#f = open('05.input', 'r')
f = open('05.test', 'r')
lines = [x.strip() for x in f.readlines()]

rules = {}

i = 0
while True:
    line = lines[i]
    i += 1
    if line.strip() == '':
        break
    before, after = line.split('|')
    if before not in rules:
        rules[before] = []
    rules[before].append(after)

tot = 0
invalid_lines = []
for line in lines[i:]:
    seen = set()
    valid = True
    arr = line.split(",")
    for x in arr:
        seen.add(x)
        if x not in rules:
            continue
        for after in rules[x]:
            if after in seen:
                valid = False

    if not valid:
        invalid_lines.append(arr)
        continue
    middle = arr[len(arr)//2]
    tot += int(middle)
print("Solution part 1:",tot)

# ----
# Part 2
def swap(rules, arr):
    seen = set()
    for i, x in enumerate(arr):
        seen.add(x)
        if x not in rules:
            continue

        for after in rules[x]:
            if after in seen:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                return False
    return True

def sort_line(rules, arr):
    while True:
        is_sorted = swap(rules, arr)
        if is_sorted:
            break
        continue
    return arr
        
valid_lines = []
tot = 0
for line in invalid_lines:
    sorted_line = sort_line(rules,line)
    middle = sorted_line[len(sorted_line)//2]
    tot += int(middle)
print("Solution part 2:",tot)
