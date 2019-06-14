import operator

# Part 1

def sort_dic_by_values(d):
    return sorted(d.items(), key=operator.itemgetter(1))


# import data
data = [r.strip() for r in open('23.in', 'r').readlines()]


class Bot:
    def __init__(self, pos, r):
        self.pos = pos
        self.r = r

    def distance(self, other):
        return abs(other.pos[0] - self.pos[0]) + abs(
            other.pos[1] - self.pos[1]) + abs(other.pos[2] - self.pos[2])

    def __repr__(self):
        return 'Bot {pos: %s, range: %d}' % (','.join(map(str, self.pos)),
                                             self.r)


bots = []
minrange = 999999999
maxrange = 0
maxx = 0
maxy = 0
maxz = 0
minx = 0
miny = 0
minz = 0
for line in data:
    p, r = line.split(', ')
    r = int(r[2:])
    pos = [int(s) for s in p[5:-1].split(',')]
    b = Bot(pos, r)
    bots.append(b)
    maxrange = max(maxrange, b.r)
    minrange = min(minrange, b.r)
    maxx = max(maxx, b.pos[0])
    maxy = max(maxy, b.pos[1])
    maxz = max(maxz, b.pos[2])
    minx = min(minx, b.pos[0])
    miny = min(miny, b.pos[1])
    minz = min(minz, b.pos[2])

start_pos = [bot for bot in bots if bot.r == maxrange][0]
within_range = [bot for bot in bots if bot.distance(start_pos) < maxrange]

print('Part 1: %d' % len(within_range))
print('Maxrange:', maxrange)

