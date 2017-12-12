from collections import Counter

data = open('my.input').read().split('\n')

groups = []

for d in data:
    numbers = [int(s.strip(',')) for s in d.split() if s.strip(',').isdigit()] 
    numbers = list(set(numbers))
    groups.append(numbers)

def mergeGroup(groups):    
    l = len(groups)
    for i in range(l):
        for j in range(i+1, l):
            union = set(groups[i] + groups[j])
            if len(union) != len(groups[i]) + len(groups[j]):
                groups[i] = list(union)
                del(groups[j])
                return True
    return False

noMerge = True    
while noMerge:
    print('Group length', len(groups))
    noMerge = mergeGroup(groups)
                
print(groups)
print('Programs in same group as 0:', len(groups[0]))
print('Total number of groups:', len(groups) - 1)
