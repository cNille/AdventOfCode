print(chr(27)+'[2j')
print('\033c', end='')

print("Day 20")
f = open('20.input', 'r')
#f = open('20.test', 'r')
lines = [x.strip() for x in f.readlines()]


ranges = []
for x in lines:
    low, high = map(int, x.split('-'))
    new_ranges = []
    merged = False
    for l, h in ranges:
        if l <= low and low <= h or l <= high and high <= h:
            min_l = min(l, low)
            max_h = max(h, high)
            new_ranges.append((min_l, max_h))
            merged = True
        else:
            new_ranges.append((l, h))
    if not merged:
        new_ranges.append((low,high))
    ranges = new_ranges
ranges = sorted(ranges, key=lambda r: r[1])
ranges = sorted(ranges, key=lambda r: r[0])

lowest = ranges[0][1] + 1
i = 1
while True:
    next_low = ranges[i][0]
    if next_low == lowest:
        lowest = ranges[i][1] + 1
        i += 1
        continue
    else:
        break
print("Part 1:", lowest)

def merge_ranges(ranges):
    any_merge = True
    while any_merge:
        any_merge = False
        for low, high in ranges:
            merged = False
            new_ranges = []
            for l, h in ranges:
                if low == l and h == high:
                    continue
                if l <= low and low <= h or l <= high and high <= h:
                    min_l = min(l, low)
                    max_h = max(h, high)
                    new_ranges.append((min_l, max_h))
                    merged = True
                    any_merge = True
                else:
                    new_ranges.append((l, h))
            if not merged:
                new_ranges.append((low,high))
            ranges = new_ranges
            if merged:
                break
    return ranges

ranges = merge_ranges(ranges)

sum_allowed = 0
for i in range(len(ranges) - 1):
    l0, h0 = ranges[i]
    l1, h1 = ranges[i+1]
    allowed = (l1-h0) - 1
    if allowed > 0:
        sum_allowed += allowed

print("Part 2:", sum_allowed)
