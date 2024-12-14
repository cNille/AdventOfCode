from collections import defaultdict
from time import sleep
import sys


print(chr(27)+'[2j')
print('\033c')
f = open('14.test', 'r')
f2 = open('14.test2', 'r')
f3 = open('14.input', 'r')

def group(bots):
    g = defaultdict(int) 
    for (x,y,_,_) in bots:
        g[(x,y)] += 1
    return g
        

def print_map(bots, width, height, quadrant=False):
    g = group(bots)

    for y in range(height):
        line = ''
        for x in range(width):
            if quadrant:
                if x == (width //2) or y == (height //2):
                    line += ' '
                    continue
            if (x,y) in g:
                line += str(g[(x,y)])
            else:
                line += '.'
        print(line)
            

def parse(f):
    lines = [x.strip() for x in f.readlines()]
    bots = []
    for line in lines:
        p, v = line.split(' ')
        x,y = [int(n) for n in p[2:].split(',')]
        vx,vy = [int(n) for n in v[2:].split(',')]
        bots.append((x,y,vx,vy))
    return bots

def round(r, bots, width, height):
    for i in range(len(bots)):
        x,y,vx,vy = bots[i]
        bots[i] = (
            (x+vx) % width,
            (y+vy) % height,
            vx,
            vy
        )

    #print('---')
    #print(f'Round {r}')
    #print_map(bots, width,height)
    #print('')

def get_score(bots, width, height):
    g = group(bots)
    q = [0,0,0,0]

    for y in range(height):
        line = ''
        for x in range(width):
            wm = (width // 2)
            hm = (height // 2)
            if x == wm or y == hm:
                continue
            if (x,y) not in g:
                continue
            if x < wm and y < hm:
                q[0] += g[(x,y)]
            if x > wm and y < hm:
                q[1] += g[(x,y)]
            if x < wm and y > hm:
                q[2] += g[(x,y)]
            if x > wm and y > hm:
                q[3] += g[(x,y)]



    print(q)
    score = 1
    for n in q:
        score *= n
    return score


def get_distances(bots):
    distances = 0
    for b1 in bots:
        x1, y1, _, _ = b1
        min_d = 9999
        for b2 in bots:
            if b1 == b2:
                continue
            x2, y2, _, _ = b2
            d = abs(x2-x1) + abs(y2-y1)
            min_d = min(d, min_d)
        distances += max(min_d, 1)
    return distances



width=101
height=103
bots = parse(f3)

#width=11
#height=7
#bots = parse(f)

rounds = 1000000

#print('Bots:', bots)
max_d = 0 
min_d = 9999
for i in range(rounds):
    round(i+1,bots, width, height)
    if i < 7620:
        continue
    distances = get_distances(bots)

    if distances < 1300:
        print_map(bots, width,height)

    max_d = max(distances, max_d)
    min_d = min(distances, min_d)

    progress = distances / max_d
    bar_length = 40  
    filled_length = int(bar_length * progress)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rProgress: [{bar}] {progress:.1%} d: {distances} (Round {i+1})')
    #sleep(0.1)

print_map(bots, width,height, True)
score = get_score(bots,width,height)
print(f"Score: {score}")

# 489
