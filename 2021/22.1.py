print(chr(27)+'[2j')
print('\033c')
f = open('22.test', 'r')
f = open('22.test2', 'r')
f = open('22.input', 'r')
data = [x.strip() for x in f.readlines()]
data = data[:-2]

def clamp1(x, minimum, maximum):
    a,b = x
    fully_outside = (a < minimum and b < minimum) or (a > maximum and b > maximum)
    if fully_outside:
        return None
    return (
        max(min(a, maximum), minimum),
        max(min(b, maximum), minimum),
    )

def part1(data):
    on = set()
    for cube in data:
        action, area = cube.split(' ')
        xarea, yarea,zarea = area.split(',')
        xrange = tuple(map(int, xarea[2:].split('..')))
        yrange = tuple(map(int, yarea[2:].split('..')))
        zrange = tuple(map(int, zarea[2:].split('..')))
        xrange = clamp1(xrange, -50, 50)
        yrange = clamp1(yrange, -50, 50)
        zrange = clamp1(zrange, -50, 50)
        if not xrange or not yrange or not zrange:
            continue

        count = 0
        if action =='on':
            for z in range(zrange[0], zrange[1] + 1):
                for y in range(yrange[0], yrange[1] + 1):
                    for x in range(xrange[0], xrange[1] + 1):
                        if (x,y,z) not in on:
                            on.add((x,y,z))
                            count += 1
        else: 
            for z in range(zrange[0], zrange[1] + 1):
                for y in range(yrange[0], yrange[1] + 1):
                    for x in range(xrange[0], xrange[1] + 1):
                        if (x,y,z) in on:
                            on.remove((x,y,z))
                            count += 1
    print('Solution part 1: %d' % len(on))
part1(data)
