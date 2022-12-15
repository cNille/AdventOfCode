print(chr(27)+'[2j', '\033c')


run_test = True
run_test = False 
if run_test:
    f = open('15.test', 'r')
    MAX = 20
    NTH_PRINT = 1
    PART1_ROW = 10
else:
    f = open('15.input', 'r')
    MAX = 4000000
    NTH_PRINT = 100000
    PART1_ROW = 2000000
lines = [x.strip() for x in f.readlines()]

def tuning(x,y):
    return x * 4000000 + y

print("Day 15")
MIN = 0
beacs = []
print('-'*80)
for l in lines:
    print(l)
    parts = l.split(' ')
    x = int(parts[2][2:-1])
    y = int(parts[3][2:-1])
    bx = int(parts[8][2:-1])
    by = int(parts[9][2:])
    dx,dy= abs(bx - x), abs(by - y)
    dist = dx + dy
    beacs.append((x,y,dist))
print('-'*80)

res1 = 0
res2 = 0
for ROW in range(MAX):
    if ROW % NTH_PRINT == 0:
        print("Sensor",ROW)

    beacon_range = []
    for (x,y,dist) in beacs:
        offset = 0
        drow = abs(ROW-y)
        if drow > dist:
            continue
        min_x = x - (dist - drow)
        max_x = x + (dist - drow)
        beacon_range.append((min_x, max_x))

    done = False
    while not done:
        done = True
        merged_range = []
        for min_x, max_x in beacon_range:
            update = False
            for i, (min_r, max_r) in enumerate(merged_range):
                if (min_r <= max_x and max_x <= max_r) or (min_x <= max_r and max_r <= max_x):
                    new_min = min(min_r, min_x)
                    new_max = max(max_r, max_x)
                    merged_range[i] = (new_min, new_max)
                    update = True
                    break
            if not update :
                merged_range.append((min_x,max_x))
            else:
                done = False
        beacon_range = merged_range

    if ROW == PART1_ROW:
        min_x, max_x = beacon_range[0]
        res1 = max_x - min_x

    if (len(beacon_range) == 1):
        continue


    diff = beacon_range[1][0] - beacon_range[0][1]
    if  diff > 1:
        x,y = beacon_range[0][1]+1, ROW
        res2 = tuning(x,y)
        break

print("Solution part 1:", res1)
print("Solution part 2:", res2)

# Part1
# no_beacon = set()
# beacons = set()
# ROW=10 # Testdata
# ROW=2000000 # Real
# for l in lines:
#     print('-'*80)
#     print(l)
#     parts = l.split(' ')
#     x = int(parts[2][2:-1])
#     y = int(parts[3][2:-1])
#     bx = int(parts[8][2:-1])
#     by = int(parts[9][2:])
#     dx,dy= abs(bx - x), abs(by - y)
#     dist = dx + dy
#     beacons.add((bx,by))
# 
#     offset = 0
#     while True:
#         drow = abs(ROW-y) + offset
#         if drow > dist:
#             break
#         no_beacon.add((x+offset, ROW)) 
#         no_beacon.add((x-offset, ROW)) 
#         offset += 1
# 
# count = 0
# for nob in no_beacon:
#     if nob not in beacons:
#         count += 1
# print("Solution part 1:",count)
