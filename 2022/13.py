print(chr(27)+'[2j')
print('\033c')
f = open('13.test', 'r')
f = open('13.input', 'r')
data = f.read() 
import copy 

pairs = [x.split('\n') for x in data.strip().split('\n\n')]

print("Day 13")



def compare_pair(p, level):
    #print("\t"*level, "- Compare:", p[0], p[1])
    l , r = p
    
    done = False
    right_order = False
    while len(l) > 0 and len(r) > 0:
        l1 = l.pop(0)
        r1 = r.pop(0)

        if isinstance(l1, int) and isinstance(r1, int):
            right_order = l1 < r1
            #print("\t"*level, "- Compare %d vs %d:" % (l1, r1), right_order)
            if l1 != r1:
                done = True
                break
        if isinstance(l1, list) and isinstance(r1, list):
            p = (l1,r1)
            d, rig = compare_pair(p , level + 1)
            if d:
                return (d,rig)
            continue
        if isinstance(l1, list):
            l.insert(0, l1)
            r.insert(0, [r1])
            continue
        if isinstance(r1, list):
            l.insert(0, [l1])
            r.insert(0, r1)
            continue


    if not done and (len(r) > 0 or len(l) > 0):
        done = True
        right_order = len(r) > len(l) 
        #if len(r) > len(l):
        #    print(p, "Left side is smaller. RIGHT order")
        #else:
        #    print(p, "Right side is smaller. NOT right order")

    return (done, right_order)

def part1(pairs):
    res = 0
    for i, pair in enumerate(pairs):
        index = i + 1
        right_order = compare_pair(pair, 0)    
        if right_order:
            res += index
    return res

pairs = [(eval(l), eval(r)) for (l, r) in pairs]
print("Solution part 1:", part1(copy.deepcopy(pairs)))


signals = []
for (l,r) in pairs:
    signals.append(l)
    signals.append(r)
signals.insert(0, [[2]])
signals.insert(0, [[6]])

def print_signals(signals):
    for s in signals:
        print(s)

is_sorted = False
itr = 0
max_sorted = 0
offset = 0
while not is_sorted:
    itr += 1
    print("Iteration" , itr, max_sorted, len(signals))

    has_changed = False
    for i in range(0 , len(signals)):

        pair = (
            copy.deepcopy(signals[i]),
            copy.deepcopy(signals[i+1])
        )

        done, right_order = compare_pair(pair, 0)    
        if done and not right_order:
            #print("COMPARE", signals[i], signals[i+1])
            #print("Result", done, right_order) 
            signals[i], signals[i+1] = signals[i+1], signals[i]
            has_changed = True
            max_sorted = i if i > max_sorted else max_sorted
            break

    if not has_changed:
        is_sorted = True

    #print_signals(signals)

print('-'*80)
print('Sorted')
print_signals(signals)

total = 1
for i, s in enumerate(signals):
    if s == [[2]]:
        print("2 in ", i)
        total *= i+1
    if s == [[6]]:
        print("6 in ", i)
        total *= i+1

print("TOtal", total)
# 90902 too high
# 96 not correct
