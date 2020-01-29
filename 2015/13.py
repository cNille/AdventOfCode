from itertools import permutations
data = [x.strip() for x in open('13.input','r').readlines()]

pref = {}
names = set() 
for d in data:
    x = d[:-1].split(' ')
    a = x[0]
    b = x[-1]
    happiness = int(x[3]) if x[2] == 'gain' else -int(x[3])
    names.add(a)
    names.add(b)
    if a not in pref:
        pref[a] = {}
    pref[a][b] = happiness

def get_happy(names, pref):
    neighbours = zip(names, names[1:] + names[:1])
    return sum([pref[a][b] + pref[b][a] for a,b in neighbours])

def get_max_happ(names,pref):
    max_happ = 0
    for p in list(permutations(list(names))):
        max_happ = max(max_happ, get_happy(p, pref))
    return max_happ

res = get_max_happ(names,pref)
print("Part 1: %d" % res)

pref['you'] = {}
for name in list(names):
    pref['you'][name] = 0
    pref[name]['you'] = 0
names.add('you') 

res = get_max_happ(names,pref)
print("Part 2: %d" % res)
