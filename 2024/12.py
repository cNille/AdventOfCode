from collections import defaultdict


print(chr(27)+'[2j')
print('\033c')
f = open('12.test', 'r')
f = open('12.test2', 'r')
#f = open('12.test3', 'r')
#f = open('12.input', 'r')
lines = [x.strip() for x in f.readlines()]

g = {}
chars = defaultdict(int)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        g[(x,y)] = c  
        chars[c] += 1
    print(line)
print()

fences = defaultdict(int) 
D = [ 
     (0, -1), 
     (1, 0), 
     (0, 1), 
     (-1,0), 
]


def get_perimeter(pos, visited: set, region):
    x,y = pos
    perimeter = 0
    visited.add(pos)
    for d in D:
        dx,dy = d
        n = (x+dx, y+dy)
        if (n,d) in region:
            continue
        region.add((n,d))
        if n not in g:
            perimeter += 1
            continue
        if g[n] == c:
            p, visited, r = get_perimeter(n, visited,region)
            region.union(r)
            perimeter += p
            continue
        else:
            perimeter += 1
            continue
    return perimeter, visited, region

def dist(n1,n2):
    x1,y1=n1
    x2,y2=n2
    return abs(x1-x2) + abs(y1-y2)

def merge(sides):
    for i, s1 in enumerate(sides): 
        for j in range(i+1,len(sides)):
            for (n1,d1) in s1:
                for (n2,d2) in sides[j]:
                    if dist(n1,n2) == 1 and d1 == d2:
                        sides[i].extend(sides[j])
                        del sides[j]
                        return sides, True
    return sides, False

def get_sides(c, region):
    sides = []
    #print(f"c: {c}")
    new_r = set()
    for r in region:
        if r[0] in g and g[r[0]] == c:
            continue
        #print('RR', r)
        new_r.add(r)
    region = new_r

    for (n,d) in region:
        same_side = False
        for i, side in enumerate(sides):
            for (n1,d2) in side:
                if dist(n1,n) == 1 and d == d2:
                    #print('SAME', n1,n , 'd', d, d2)
                    same_side = True
                    sides[i].append((n,d))
                    break
            if same_side:
                break
        if not same_side:
            sides.append([(n,d)])

    can_merge = True
    while can_merge:
        sides, can_merge = merge(sides)

    return len(sides)


prices = {}
visited = set()
total_part1 = 0
total_part2 = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if (x,y) in visited:
            continue
        perimeter, v, region= get_perimeter((x,y), set(), set())
        visited.update(v)
        size = len(v)
        sides = get_sides(c, region)
        price1 = size * perimeter
        price2 = size * sides
        print(f"{c} == Size: {size}, Perimeter: {perimeter}, sides: {sides}, price {price1}, price2 {price2}")
        total_part1 += price1
        total_part2 += price2
print('Solution part1:', total_part1)
print('Solution part2:', total_part2)

