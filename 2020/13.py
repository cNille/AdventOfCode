lines = [x.strip() for x in open('13.test', 'r').readlines() if x != '']
lines = [x.strip() for x in open('13.input', 'r').readlines() if x != '']

def part1(lines):
    start = int(lines[0])
    ids = lines[1].split(",")
    ids = [x for x in ids if x != 'x']
    ids = map(int, ids)
    minrest = minid= start * 2 
    for i in ids:
        rest = (1 + (start // i)) * i  - start
        if rest < minrest:
            minrest = rest
            minid = i
    return ( minid * minrest )
print "Solution part 1: %d" %  part1(lines)

start = int(lines[0])
ids = lines[1].split(",")
idrange = len(ids)

busids = []
for i in range(len(ids)):
    offset = i
    busid = ids[i]
    if busid != 'x':
        busids.append((int(busid), offset))

real_data = list(busids)

def compare(a, b):
    valid = [] 
    i = 1
    while True:
        if len(valid) > 11:
            break
        if (a[0] * i + b[1] - a[1]) % b[0] == 0:
            valid.append(i)
        i += 1
    return valid

def part2(busids, multiplyer):
    found = []
    first = busids[0]
    for current in busids[1:]:
        a = compare(first, current)
        found.append(a)

    result = set(found[0])
    for f in found[1:]:
        result = result.intersection(f)
    if len(result) > 0:
        res = min(result) * busids[0][0]  - busids[0][1]
        return res
    else:
        new_busids = [(a[1]-a[0], -a[0] % (a[1]-a[0])) for a in found] 
        p2 = part2(new_busids, busids[0][0])
        res = busids[0][0] *  p2 - busids[0][1]
        #print "-- part2 returns:" , res, p2, multiplyer, busids[0][1]
        return res



# Tests:
# busids = [(17,0), (13,2), (19,3)]
# res = part2(list(busids), busids[0][0]) 
# assert(res == 3417)
# print "Test 1:", res
# print '----------'
# busids = [(67,0), (7,2), (59,3), (61,4)]
# res = part2(list(busids), busids[0][0]) 
# print "Test 2:", res
# assert(res == 779210)
# print '----------'
# busids = [(67,0), (7,1), (59,3), (61,4)]
# res = part2(list(busids), busids[0][0]) 
# assert(res == 1261476)
# print "Test 3:", res
# print '----------'
# busids = [ (1789,0), (37,1), (47,2), (1889,3) ]
# res = part2(list(busids), busids[0][0]) 
# assert(res == 1202161486)
# print "Test 4:", res
# print '----------'
# busids = [ (7 , 0), (13 , 1), (59 , 4), (31 , 6), (19 , 7) ]
# res = part2(list(busids), busids[0][0]) 
# print res
# assert(res == 1068781)
# print "Test 5:", res
# print '----------'

res = part2(list(real_data), real_data[0][0]) 

def validate(res):
    #print "Validate: ", res
    for r in real_data:
        rest = (res + r[1]) % r[0] 
        #print "Validating: ", r, " has rest = ", rest
        if rest != 0:
            return False
    return True

if validate(res):
    print "Solution part 2:" , res

