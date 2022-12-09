print(chr(27)+'[2j')
print('\033c')
f = open('09.test', 'r')
f = open('09.test2', 'r')
f = open('09.input', 'r')
lines = [x.strip() for x in f.readlines()]

DIR = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,-1),
    'D': (0,1),
}

def distance(p1,p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    if max(dx,dy) == 1:
        return 1
    return dy + dx

def diag(p1,p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dx = int(dx / abs(dx)) if dx != 0 else dx
    dy = int(dy / abs(dy)) if dy != 0 else dy
    return (dx,dy) 


def print_map(line, ROPE, MIN, MAX, LENGTH):
    print("------")
    print(line)
    for y in range(MIN,MAX):
        row = ""
        for x in range(MIN,MAX):
            added = False
            for i in range(LENGTH-1, -1,-1):
                if (x,y) == ROPE[i]:
                    row += str(i)
                    added = True
                    break
            if not added:
                if (x,y) == (0,0):
                    row += "s"
                else:
                    row += "."
        print(row)

def part(LENGTH):
    ROPE: list[tuple[int,int]] = [(0,0)] * LENGTH 

    place = []
    for i in range(LENGTH):
        place.append(set())
        place[i].add(ROPE[i])
    MIN = -5
    MAX = 5
    #print_map("INIT", ROPE, MIN, MAX, LENGTH)

    for line in lines:
        d, s = line.split(' ')
        s = int(s)

        for _ in range(s):
            dx,dy = DIR[d]
            ROPE[0] = (ROPE[0][0]+dx, ROPE[0][1]+dy)
            for i in range(1, LENGTH):
                dist = distance(ROPE[i-1],ROPE[i])
                if dist == 2:
                    if ROPE[i][0] == ROPE[i-1][0]:
                        ddx,ddy = diag(ROPE[i-1],ROPE[i])
                        ROPE[i] = (ROPE[i][0], ROPE[i][1]+ddy) 
                    elif ROPE[i][1] == ROPE[i-1][1]:
                        ddx,ddy = diag(ROPE[i-1],ROPE[i])
                        ROPE[i] = (ROPE[i][0]+ddx, ROPE[i][1]) 
                    else:
                        ROPE[i] = (ROPE[i][0]+dx, ROPE[i][1]+dy) 
                elif dist > 2:
                    ddx,ddy = diag(ROPE[i-1],ROPE[i])
                    ROPE[i] = (ROPE[i][0]+ddx, ROPE[i][1]+ddy) 
            for i in range(LENGTH):
                place[i].add(ROPE[i])
        for i in range(LENGTH):
            MIN = min(MIN, ROPE[i][0] - 2, ROPE[i][1] - 2)
            MAX = max(MAX, ROPE[i][0] + 2, ROPE[i][1] + 2)
        #print_map(line, ROPE, MIN, MAX, LENGTH)
    return len(place[-1])

print("Part 1 solution", part(2))
print("Part 2 solution", part(10))
