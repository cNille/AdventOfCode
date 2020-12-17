lines = [x.strip() for x in open('17.input', 'r').readlines() if x != '']
lines = [x.strip() for x in open('17.test', 'r').readlines() if x != '']

# My solution. Here are other for more inspiration:
# https://github.com/r0mainK/advent/blob/master/2020/17.py
# Numpy: https://gist.github.com/sciyoshi/3b0df201d087b4e5beda8a015e7f3699
# Convolution: https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/gg45jot?utm_source=share&utm_medium=web2x&context=3

# Solutions: Either keep track of neighbours coordinates. Or use a space matrix
#            approach with 1 and 0 to calculate. Or use numpy

def part1(lines, verbose=False):
    neighbours = []
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter == '#':
                neighbours.append((x,y,0))

    def get_neighbours(neighbours, x,y,z):
        return [
            n 
            for n in neighbours
            if
            n != (x,y,z) and
            x-1 <= n[0] <= x+1 and
            y-1 <= n[1] <= y+1 and
            z-1 <= n[2] <= z+1
        ]

    def get_range(coordinates, OFFSET=1):
        xs = [c[0] for c in coordinates]
        ys = [c[1] for c in coordinates]
        zs = [c[2] for c in coordinates]
        return (
            min(xs) - OFFSET, max(xs) + OFFSET,
            min(ys) - OFFSET, max(ys) + OFFSET,
            min(zs) - OFFSET, max(zs) + OFFSET,
        )

    def get_spaces(neighbours):
        xmin, xmax, ymin, ymax, zmin, zmax = get_range(neighbours)
        spaces = []
        for z in range(zmin, zmax+1):
            for y in range(ymin, ymax+1):
                for x in range(xmin, xmax+1):
                    spaces.append((x,y,z))
        return spaces

    def print_map(neighbours):
        if not verbose:
            return
        xmin, xmax, ymin, ymax, zmin, zmax = get_range(neighbours, 0)
        for z in range(zmin, zmax+1):
            print "z = %d" % z
            for y in range(ymin, ymax+1):
                line = ""
                for x in range(xmin, xmax+1):
                    ch = "#" if (x,y,z) in neighbours else "."
                    line = line + ch
                print line
                lines.append(line) 
            print ""



    ROUNDS = 6
    print_map(neighbours)
    for i in range(ROUNDS):
        new_neighbours = []
        spaces = get_spaces(neighbours)
        for (x,y,z) in spaces:
            n = get_neighbours(neighbours, x,y,z)
            if (x,y,z) in neighbours:
                if len(n) == 2 or len(n) == 3:
                    new_neighbours.append((x,y,z))
            else:
                if len(n) == 3:
                    new_neighbours.append((x,y,z))
        neighbours = new_neighbours
        print_map(neighbours)

        print "Round %d: %d" % ((i+1), len(neighbours))
    print "Solution part 1:", len(neighbours)

def part2(lines, verbose=False):
    neighbours = []
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter == '#':
                neighbours.append((x,y,0,0))

    def get_neighbours(neighbours, x,y,z,w):
        return [
            n 
            for n in neighbours
            if
            n != (x,y,z,w) and
            x-1 <= n[0] <= x+1 and
            y-1 <= n[1] <= y+1 and
            z-1 <= n[2] <= z+1 and
            w-1 <= n[3] <= w+1
        ]

    def get_range(coordinates, OFFSET=1):
        xs = [c[0] for c in coordinates]
        ys = [c[1] for c in coordinates]
        zs = [c[2] for c in coordinates]
        ws = [c[3] for c in coordinates]
        return (
            min(xs) - OFFSET, max(xs) + OFFSET,
            min(ys) - OFFSET, max(ys) + OFFSET,
            min(zs) - OFFSET, max(zs) + OFFSET,
            min(ws) - OFFSET, max(ws) + OFFSET,
        )

    def get_spaces(neighbours):
        xmin, xmax, ymin, ymax, zmin, zmax, wmin, wmax = get_range(neighbours)
        spaces = []
        for w in range(wmin, wmax+1):
            for z in range(zmin, zmax+1):
                for y in range(ymin, ymax+1):
                    for x in range(xmin, xmax+1):
                        spaces.append((x,y,z,w))
        return spaces

    def print_map(neighbours):
        if not verbose:
            return
        xmin, xmax, ymin, ymax, zmin, zmax, wmin, wmax = get_range(neighbours, 0)
        for w in range(wmin, wmax+1):
            for z in range(zmin, zmax+1):
                print "z = %d, w = %d" % (z, w)
                for y in range(ymin, ymax+1):
                    line = ""
                    for x in range(xmin, xmax+1):
                        ch = "#" if (x,y,z,w) in neighbours else "."
                        line = line + ch
                    print line
                    lines.append(line) 
                print ""

    ROUNDS = 6
    print_map(neighbours)
    print '---------'
    for i in range(ROUNDS):


        new_neighbours = []
        spaces = get_spaces(neighbours)
        for (x,y,z,w) in spaces:
            n = get_neighbours(neighbours, x,y,z,w)
            if (x,y,z,w) in neighbours:
                if len(n) == 2 or len(n) == 3:
                    new_neighbours.append((x,y,z,w))
            else:
                if len(n) == 3:
                    new_neighbours.append((x,y,z,w))
        neighbours = new_neighbours
        print_map(neighbours)

        print "Round %d count: %d" % ((i+1), len(neighbours))
    print "Solution part 2:", len(neighbours)

part1(lines, True)
#part2(lines, False)
