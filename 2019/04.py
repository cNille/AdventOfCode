f = open('04.input', 'r')
content = [x.strip() for x in f.readlines()]

data = "138241-674034"

def adj(nbr):
    x = zip(nbr[:-1], nbr[1:])
    for (a,b) in x:
        if  a == b:
            return True
    return False

def adj2(nbr):
    groups = [ [nbr[0]] ]
    
    for i in range(len(nbr)-1):
        if nbr[i] != nbr[i+1]:
            groups.append([nbr[i+1]])
        else:
            groups[-1].append(nbr[i+1])

    lengths = [len(g) for g in groups if len(g) == 2]
    return len(lengths) > 0

def dec(nbr):
    for i,x in enumerate(nbr[:-1]):
        if x > nbr[i+1]:
            return False
    return True

# Part 1
count = 0 
for x in range(138241, 674034):
    if not dec(str(x)):
        continue
    if not adj(str(x)):
        continue
    count += 1
print("Part 1: %d" % count)

# Part 2
count = 0 
for x in range(138241, 674034):
    if not dec(str(x)):
        continue
    if not adj2(str(x)):
        continue
    count += 1
print("Part 2: %d" % count)
