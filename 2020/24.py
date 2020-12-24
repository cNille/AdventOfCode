from collections import defaultdict
lines = [x.strip() for x in open('24.test', 'r').readlines()]
lines = [x.strip() for x in open('24.input', 'r').readlines()]

# My solutions below. Here are links to alternative solutions:
# - https://github.com/alexander-yu/adventofcode/blob/master/problems_2020/24.py
# He used sly and cube coordinate system for hexagon
# - https://sly.readthedocs.io/en/latest/sly.html
# - https://math.stackexchange.com/questions/2254655/hexagon-grid-coordinate-system
# - https://www.redblobgames.com/grids/hexagons/

# https://www.reddit.com/r/adventofcode/comments/kj96iw/2020_day_24_solutions/ggvix6u?utm_source=share&utm_medium=web2x&context=3
# https://github.com/sparkyb/adventofcode/blob/master/2020/day24.py
# Used sets  and unions for finding black tiles

# https://www.reddit.com/r/adventofcode/comments/kj96iw/2020_day_24_solutions/ggvimzc?utm_source=share&utm_medium=web2x&context=3
# Clean solution using Counter in collection and just summing the steps

# https://github.com/filipmlynarski/Advent-of-Code/blob/master/2020/24.py
# Using regex to easy parsing lines

# https://www.youtube.com/watch?app=desktop&v=thOifuHs6eY
# Hexagons are bestagons

# https://www.reddit.com/r/adventofcode/comments/kj96iw/2020_day_24_solutions/ggvgu9r?utm_source=share&utm_medium=web2x&context=3
# https://github.com/sophiebits/adventofcode/blob/main/2020/day24.py
# Hexagons are basically rectangular grids?

# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2020/24.py

delta = {
    'se': (0.5,-0.5), 'e': (1,0), 'ne': (0.5,0.5),
    'sw': (-0.5,-0.5), 'w': (-1,0), 'nw': (-0.5,0.5),
}

def get_pos(line):
    if len(line) == 0:
        return (0,0)

    if line[0] in ['e', 'w']:
        tail_x, tail_y = get_pos(line[1:])
        x,y = delta[line[0]]
        return tail_x + x, tail_y + y
    elif line[:2] in ['sw', 'nw', 'se', 'ne']:
        tail_x, tail_y = get_pos(line[2:])
        x,y = delta[line[:2]]
        return tail_x + x, tail_y + y
    else:
        print 'ERROR:', line
        exit()

def part1(lines):
    tiles = defaultdict(bool) 
    for i, line in enumerate(lines):
        pos = get_pos(line)
        tiles[pos] = not tiles[pos]
    count = 0 
    for t in tiles:
        count += 1 if tiles[t] else 0
    print "Part 1 solution: ", count
part1(lines)

def get_neighbours((x,y)):
    return [(a+x, b+y) for a,b in delta.values()]

def part2(lines):
    # Day 0
    tiles = defaultdict(bool) 
    for i, line in enumerate(lines):
        pos = get_pos(line)
        tiles[pos] = not tiles[pos]
    
    # 100 days
    for i in range(1,101):
        # Remove tiles with no black adjacent at all 
        to_rm = []
        for t in tiles:
            neighbours = get_neighbours(t)
            to_rm += [t for t in neighbours if t in tiles and not tiles[t]]
        for t in to_rm:
            if t in tiles and not tiles[t]:
                del tiles[t] 
        # Add neighbours to our tiles
        to_add = []
        for t in tiles:
            neighbours = get_neighbours(t)
            to_add += [t for t in neighbours if t not in tiles]
        for t in to_add:
            tiles[t] = False
        
        # Decide which to flip
        to_flip = []
        for t in tiles:
            black_tiles = [n for n in get_neighbours(t) if n in tiles and tiles[n]]
            count = len(black_tiles)
            if tiles[t]: # Current is black tile
                if count == 0 or count > 2:
                    to_flip.append(t)
            else:
                if count == 2:
                    to_flip.append(t)
        # Flip tiles
        for t in to_flip:
            tiles[t] = not tiles[t]
    
        if i % 10 == 0:
            count = 0
            for t in tiles:
                count += 1 if tiles[t] else 0
            print "Day %d == %d" % (i, count)

    # Count result
    count = 0 
    for t in tiles:
        count += 1 if tiles[t] else 0
    print "Part 2 solution: ", count
part2(lines)
