from time import sleep
vault = [x.strip() for x in open('18.input', 'r').readlines()]


doors = {}
locks = {}
lock_pos = {}
pos = None
for y, row in enumerate(vault):
    for x, c in enumerate(row):
        if c == "@":
            pos = (x,y)
        if c.isupper():
            doors[c] = (x,y)
        if c.islower():
            locks[(x,y)] = c 
            lock_pos[c] = (x,y)

def getNextSteps(vault,x,y,path):
    directions = [ (1,0), (-1,0), (0,-1), (0,1) ]
    next_steps = [] 
    return [
        (x+dx, y+dy)
        for dx, dy in directions
        if (
            vault[y+dy][x+dx] == '.'       # isEmpty spot
            or vault[y+dy][x+dx].islower() # isLock
        ) and (x+dx, y+dy) not in path     # not already visited
    ]

def updateVault(vault, x,y, c):
    vault[y] = vault[y][:x] + c + vault[y][x+1:]
    return vault

class Navigator:
    def __init__(self, vault, x,y, steps, visited, dependencies):
        self.vault = vault
        self.x = x
        self.y = y
        self.steps = steps
        self.visited = visited
        self.dependencies = dependencies

    def __str__(self):
        return "Nav(%d, %d, %d)" % (self.x, self.y, self.steps)
    def __repr__(self):
        return "Nav(%d, %d, %d)" % (self.x, self.y, self.steps)

# Remove start character from map
x,y = pos

def getNextNonWall(vault,x,y,path, dep=""):
    directions = [ (1,0), (-1,0), (0,-1), (0,1) ]
    next_steps = [] 
    return [
        (x+dx, y+dy, vault[y+dy][x+dx], dep)
        for dx, dy in directions
        if (
            vault[y+dy][x+dx] != '#'       # isEmpty spot
        ) and (x+dx, y+dy) not in path     # not already visited
    ]

def getDependencies(vault, x, y, locks):
    steps = 1
    path = []
    dep = {}
    nextSteps = getNextNonWall(vault,x,y,path, "@")
    while len(nextSteps) > 0:
        newSteps = []
        for a,b,c,d in nextSteps:
            if c.isupper():
                d += c
            if c.islower():
                dep[c] = d
            path.append((a,b))
            newSteps += list(set(getNextNonWall(vault,a,b,path, d)))
        nextSteps = newSteps
        steps += 1
    return dep


def getDistances(vault, x, y, locks):
    steps = 1
    path = []
    dist = {}
    nextSteps = getNextNonWall(vault,x,y,path, "@")
    while len(nextSteps) > 0:
        newSteps = []
        for a,b,c,d in nextSteps:
            if c.islower():
                dist[c] = steps
            path.append((a,b))
            newSteps += list(set(getNextNonWall(vault,a,b,path)))
        nextSteps = newSteps
        steps += 1
    return dist


print "Get distances...."
distances = {}
#for (lx,ly) in locks:
#    distances[(lx,ly)] = getDistances(vault, lx,ly, locks)
distances = {(77, 77): {'a': 246, 'c': 156, 'b': 220, 'e': 354, 'd': 14, 'g': 480, 'f': 120, 'i': 194, 'h': 272, 'k': 2, 'j': 400, 'm': 520, 'l': 178, 'o': 284, 'n': 344, 'q': 466, 'p': 366, 's': 100, 'r': 302, 'u': 454, 't': 490, 'w': 204, 'v': 414, 'y': 440, 'x': 260, 'z': 510}, (23, 41): {'a': 112, 'c': 286, 'b': 86, 'e': 216, 'd': 180, 'g': 342, 'f': 250, 'i': 2, 'h': 78, 'k': 194, 'j': 262, 'm': 382, 'l': 44, 'o': 150, 'n': 206, 'q': 328, 'p': 232, 's': 94, 'r': 164, 'u': 316, 't': 352, 'w': 66, 'v': 276, 'y': 302, 'x': 122, 'z': 372}, (29, 7): {'a': 328, 'c': 506, 'b': 302, 'e': 436, 'd': 400, 'g': 66, 'f': 470, 'i': 276, 'h': 354, 'k': 414, 'j': 14, 'm': 106, 'l': 264, 'o': 366, 'n': 426, 'q': 548, 'p': 448, 's': 314, 'r': 112, 'u': 40, 't': 572, 'w': 210, 'v': 2, 'y': 26, 'x': 158, 'z': 96}, (31, 23): {'a': 394, 'c': 572, 'b': 368, 'e': 502, 'd': 466, 'g': 2, 'f': 536, 'i': 342, 'h': 420, 'k': 480, 'j': 80, 'm': 40, 'l': 330, 'o': 432, 'n': 492, 'q': 614, 'p': 514, 's': 380, 'r': 178, 'u': 26, 't': 638, 'w': 276, 'v': 66, 'y': 40, 'x': 224, 'z': 30}, (35, 21): {'a': 368, 'c': 546, 'b': 342, 'e': 476, 'd': 440, 'g': 26, 'f': 510, 'i': 316, 'h': 394, 'k': 454, 'j': 54, 'm': 66, 'l': 304, 'o': 406, 'n': 466, 'q': 588, 'p': 488, 's': 354, 'r': 152, 'u': 2, 't': 612, 'w': 250, 'v': 40, 'y': 14, 'x': 198, 'z': 56}, (19, 19): {'a': 434, 'c': 612, 'b': 408, 'e': 542, 'd': 506, 'g': 40, 'f': 576, 'i': 382, 'h': 460, 'k': 520, 'j': 120, 'm': 2, 'l': 370, 'o': 472, 'n': 532, 'q': 654, 'p': 554, 's': 420, 'r': 218, 'u': 66, 't': 678, 'w': 316, 'v': 106, 'y': 80, 'x': 264, 'z': 10}, (65, 35): {'a': 2, 'c': 338, 'b': 130, 'e': 272, 'd': 232, 'g': 394, 'f': 302, 'i': 112, 'h': 190, 'k': 246, 'j': 314, 'm': 434, 'l': 96, 'o': 194, 'n': 262, 'q': 384, 'p': 276, 's': 146, 'r': 216, 'u': 368, 't': 408, 'w': 118, 'v': 328, 'y': 354, 'x': 174, 'z': 424}, (79, 11): {'a': 194, 'c': 376, 'b': 108, 'e': 310, 'd': 270, 'g': 432, 'f': 340, 'i': 150, 'h': 228, 'k': 284, 'j': 352, 'm': 472, 'l': 134, 'o': 2, 'n': 300, 'q': 422, 'p': 254, 's': 184, 'r': 254, 'u': 406, 't': 446, 'w': 156, 'v': 366, 'y': 392, 'x': 212, 'z': 462}, (37, 13): {'a': 354, 'c': 532, 'b': 328, 'e': 462, 'd': 426, 'g': 40, 'f': 496, 'i': 302, 'h': 380, 'k': 440, 'j': 40, 'm': 80, 'l': 290, 'o': 392, 'n': 452, 'q': 574, 'p': 474, 's': 340, 'r': 138, 'u': 14, 't': 598, 'w': 236, 'v': 26, 'y': 2, 'x': 184, 'z': 70}, (17, 63): {'a': 408, 'c': 582, 'b': 382, 'e': 136, 'd': 476, 'g': 638, 'f': 546, 'i': 352, 'h': 430, 'k': 490, 'j': 558, 'm': 678, 'l': 340, 'o': 446, 'n': 146, 'q': 24, 'p': 528, 's': 390, 'r': 460, 'u': 612, 't': 2, 'w': 362, 'v': 572, 'y': 598, 'x': 418, 'z': 668}, (23, 35): {'a': 118, 'c': 296, 'b': 92, 'e': 226, 'd': 190, 'g': 276, 'f': 260, 'i': 66, 'h': 144, 'k': 204, 'j': 196, 'm': 316, 'l': 54, 'o': 156, 'n': 216, 'q': 338, 'p': 238, 's': 104, 'r': 98, 'u': 250, 't': 362, 'w': 2, 'v': 210, 'y': 236, 'x': 56, 'z': 306}, (73, 75): {'a': 232, 'c': 142, 'b': 206, 'e': 340, 'd': 2, 'g': 466, 'f': 106, 'i': 180, 'h': 258, 'k': 14, 'j': 386, 'm': 506, 'l': 164, 'o': 270, 'n': 330, 'q': 452, 'p': 352, 's': 86, 'r': 288, 'u': 440, 't': 476, 'w': 190, 'v': 400, 'y': 426, 'x': 246, 'z': 496}, (17, 19): {'a': 424, 'c': 602, 'b': 398, 'e': 532, 'd': 496, 'g': 30, 'f': 566, 'i': 372, 'h': 450, 'k': 510, 'j': 110, 'm': 10, 'l': 360, 'o': 462, 'n': 522, 'q': 644, 'p': 544, 's': 410, 'r': 208, 'u': 56, 't': 668, 'w': 306, 'v': 96, 'y': 70, 'x': 254, 'z': 2}, (1, 13): {'a': 174, 'c': 352, 'b': 148, 'e': 282, 'd': 246, 'g': 224, 'f': 316, 'i': 122, 'h': 200, 'k': 260, 'j': 144, 'm': 264, 'l': 110, 'o': 212, 'n': 272, 'q': 394, 'p': 294, 's': 160, 'r': 46, 'u': 198, 't': 418, 'w': 56, 'v': 158, 'y': 184, 'x': 2, 'z': 254}, (65, 73): {'a': 302, 'c': 52, 'b': 276, 'e': 410, 'd': 106, 'g': 536, 'f': 2, 'i': 250, 'h': 328, 'k': 120, 'j': 456, 'm': 576, 'l': 234, 'o': 340, 'n': 400, 'q': 522, 'p': 422, 's': 156, 'r': 358, 'u': 510, 't': 546, 'w': 260, 'v': 470, 'y': 496, 'x': 316, 'z': 566}, (61, 3): {'a': 276, 'c': 458, 'b': 146, 'e': 392, 'd': 352, 'g': 514, 'f': 422, 'i': 232, 'h': 310, 'k': 366, 'j': 434, 'm': 554, 'l': 216, 'o': 254, 'n': 382, 'q': 504, 'p': 2, 's': 266, 'r': 336, 'u': 488, 't': 528, 'w': 238, 'v': 448, 'y': 474, 'x': 294, 'z': 544}, (71, 23): {'a': 130, 'c': 312, 'b': 2, 'e': 246, 'd': 206, 'g': 368, 'f': 276, 'i': 86, 'h': 164, 'k': 220, 'j': 288, 'm': 408, 'l': 70, 'o': 108, 'n': 236, 'q': 358, 'p': 146, 's': 120, 'r': 190, 'u': 342, 't': 382, 'w': 92, 'v': 302, 'y': 328, 'x': 148, 'z': 398}, (3, 5): {'a': 216, 'c': 394, 'b': 190, 'e': 324, 'd': 288, 'g': 178, 'f': 358, 'i': 164, 'h': 242, 'k': 302, 'j': 98, 'm': 218, 'l': 152, 'o': 254, 'n': 314, 'q': 436, 'p': 336, 's': 202, 'r': 2, 'u': 152, 't': 460, 'w': 98, 'v': 112, 'y': 138, 'x': 46, 'z': 208}, (43, 49): {'a': 96, 'c': 270, 'b': 70, 'e': 204, 'd': 164, 'g': 330, 'f': 234, 'i': 44, 'h': 122, 'k': 178, 'j': 250, 'm': 370, 'l': 2, 'o': 134, 'n': 194, 'q': 316, 'p': 216, 's': 78, 'r': 152, 'u': 304, 't': 340, 'w': 54, 'v': 264, 'y': 290, 'x': 110, 'z': 360}, (65, 45): {'a': 146, 'c': 192, 'b': 120, 'e': 254, 'd': 86, 'g': 380, 'f': 156, 'i': 94, 'h': 172, 'k': 100, 'j': 300, 'm': 420, 'l': 78, 'o': 184, 'n': 244, 'q': 366, 'p': 266, 's': 2, 'r': 202, 'u': 354, 't': 390, 'w': 104, 'v': 314, 'y': 340, 'x': 160, 'z': 410}, (33, 79): {'a': 272, 'c': 446, 'b': 246, 'e': 2, 'd': 340, 'g': 502, 'f': 410, 'i': 216, 'h': 294, 'k': 354, 'j': 422, 'm': 542, 'l': 204, 'o': 310, 'n': 10, 'q': 112, 'p': 392, 's': 254, 'r': 324, 'u': 476, 't': 136, 'w': 226, 'v': 436, 'y': 462, 'x': 282, 'z': 532}, (53, 73): {'a': 338, 'c': 2, 'b': 312, 'e': 446, 'd': 142, 'g': 572, 'f': 52, 'i': 286, 'h': 364, 'k': 156, 'j': 492, 'm': 612, 'l': 270, 'o': 376, 'n': 436, 'q': 558, 'p': 458, 's': 192, 'r': 394, 'u': 546, 't': 582, 'w': 296, 'v': 506, 'y': 532, 'x': 352, 'z': 602}, (23, 79): {'a': 262, 'c': 436, 'b': 236, 'e': 10, 'd': 330, 'g': 492, 'f': 400, 'i': 206, 'h': 284, 'k': 344, 'j': 412, 'm': 532, 'l': 194, 'o': 300, 'n': 2, 'q': 122, 'p': 382, 's': 244, 'r': 314, 'u': 466, 't': 146, 'w': 216, 'v': 426, 'y': 452, 'x': 272, 'z': 522}, (7, 43): {'a': 190, 'c': 364, 'b': 164, 'e': 294, 'd': 258, 'g': 420, 'f': 328, 'i': 78, 'h': 2, 'k': 272, 'j': 340, 'm': 460, 'l': 122, 'o': 228, 'n': 284, 'q': 406, 'p': 310, 's': 172, 'r': 242, 'u': 394, 't': 430, 'w': 144, 'v': 354, 'y': 380, 'x': 200, 'z': 450}, (27, 3): {'a': 314, 'c': 492, 'b': 288, 'e': 422, 'd': 386, 'g': 80, 'f': 456, 'i': 262, 'h': 340, 'k': 400, 'j': 2, 'm': 120, 'l': 250, 'o': 352, 'n': 412, 'q': 534, 'p': 434, 's': 300, 'r': 98, 'u': 54, 't': 558, 'w': 196, 'v': 14, 'y': 40, 'x': 144, 'z': 110}, (27, 61): {'a': 384, 'c': 558, 'b': 358, 'e': 112, 'd': 452, 'g': 614, 'f': 522, 'i': 328, 'h': 406, 'k': 466, 'j': 534, 'm': 654, 'l': 316, 'o': 422, 'n': 122, 'q': 2, 'p': 504, 's': 366, 'r': 436, 'u': 588, 't': 24, 'w': 338, 'v': 548, 'y': 574, 'x': 394, 'z': 644}}
x,y = pos
distances[(x,y)] = getDistances(vault, x,y,locks)

print "Get dependencies...."
#dependencies = getDependencies(vault, x,y, locks)
dependencies = {'a': '@', 'c': '@JV', 'b': '@IW', 'e': '@R', 'd': '@', 'g': '@ODNFC', 'f': '@P', 'i': '@', 'h': '@', 'k': '@', 'j': '@ODNF', 'm': '@ODNFCTZ', 'l': '@', 'o': '@I', 'n': '@R', 'q': '@RU', 'p': '@IWE', 's': '@', 'r': '@O', 'u': '@ODNFC', 't': '@RUG', 'w': '@', 'v': '@ODNF', 'y': '@ODNFC', 'x': '@', 'z': '@ODNFCT'}

print locks
print lock_pos
print distances
print dependencies
print("")
print("")
print("")
print("")


# ===================================
# ===================================

def getLockDistances(vault, x, y, locks):
    print("aoeu" )


def copy(a):
    return "\n".join(a).split('\n')

x,y = pos
locks[(40,40)] = 0
visited = ["@"]
paths = [Navigator(vault, x,y, 0, visited, dependencies)]

min_steps = 99999
count = 0

while len(paths) > 0:
    nav = paths.pop(0)
    if nav.steps < min_steps and len(nav.visited) >= len(locks):
        min_steps = min_steps if min_steps < nav.steps else nav.steps
        print "New min found at: %d " % nav.steps

    count += 1
    if count % 100000 == 0:
        print "Iteration %d , %d" % (count, len(paths))

    possible = []
    new_dep = {}
    for d in [nd for nd in nav.dependencies if nd not in nav.visited]:
        new_dep[d] = [x for x in nav.dependencies[d] if x.lower() not in nav.visited]

        if len(new_dep[d]) == 0:
            possible.append(d)

    if len(possible) == 0:
        continue
            
    new_paths = []
    for p in possible:
        distance = distances[(nav.x, nav.y)][p]
        lx,ly = lock_pos[p]

        visited = nav.visited + [p]
        if (distance + nav.steps) < min_steps:
            new_paths.append(Navigator(vault, lx, ly, distance + nav.steps, visited, new_dep))

    paths = sorted(new_paths, key=lambda n: n.steps) + paths



# too high: 5420
# too high: 5308
# too high: 5156
# too high: 5044
