from collections import defaultdict
import math
lines = [x.strip() for x in open('20.input', 'r').readlines()]
lines = [x.strip() for x in open('20.test', 'r').readlines()]
lines.append('')

tiles = []
tile_inner = {}
while '' in lines:
    delimiter = lines.index('')
    tile = lines[:delimiter]
    tile_id = tile[0].split()[1][:-1]
    tile_sides = []
    tile_sides.append((tile[1], 'U', tile_id))
    tile_sides.append(("".join([t[-1] for t in tile[1:]]), 'R', tile_id))

    tile_inner[tile_id] = ["".join([ch for ch in line[1:-1]]) for line in tile[2:-1]]

    # Reverse for easier comparision with all other sides
    tile_sides.append((tile[-1][::-1], 'D', tile_id))
    tile_sides.append(("".join([t[0] for t in tile[1:]][::-1]), 'L', tile_id))

    lines = lines[delimiter+1:]
    tiles.append(tile_sides)

connections = defaultdict(list)

result = 1
edge_tiles = []
corner_ids = []
for tile in tiles:
    uncompatible_side = 0
    for side in tile: 
        compatible = []
        for other_tile in tiles:
            if tile[2] == other_tile[2]:
                continue
            for other_side in other_tile: 
                if side[0] == other_side[0][::-1]:
                    compatible.append((other_side[2], other_side[1], 'unflipped'))
                if side[0] == other_side[0]:
                    compatible.append((other_side[2], other_side[1], 'flipped'))
        # Assert unique compatibility or none
        assert(len(compatible) < 2)

        if len(compatible) == 0:
            uncompatible_side += 1
            continue

        connections[(side[2], side[1])] = compatible[0]
    if uncompatible_side == 2: # Corner tile
        corner_ids.append(tile[0][2])
    if uncompatible_side == 1: # Side tile
        edge_tiles.append(tile[0][2])

result = 1
for cid in corner_ids:
    result *= int(cid)
print("Solution part 1: %d" % result)
print("----------------")

directions = ['U', 'R', 'D', 'L']
opposite = {
    'U': 'D', 'R': 'L',
    'D': 'U', 'L': 'R',
}

square_size = int(math.sqrt(len(tiles)))
top_left = corner_ids[0] # Id
placed_tiles = {top_left: (0,0)}
tile_positions = {(0,0): top_left}
current_id = top_left
all_edge = edge_tiles + corner_ids

def get_neighbours(id):
  neighbours = filter(None, [connections[(id, d)] for d in directions ])
  return neighbours

def fill_line(start_pos, get_pos, tile_positions, placed_tiles):
    global square_size, direction, connections
    current_id = tile_positions[start_pos] 
    for x in range(1, square_size):
        neighbours = get_neighbours(current_id) 
        for id, direction, flipped in neighbours:
            if id not in placed_tiles and id in all_edge:
                placed_tiles[id] = get_pos(x)
                current_id = id
                tile_positions[get_pos(x)] = current_id 
                break
    return tile_positions, placed_tiles

# Top row 
tile_positions, placed_tiles = fill_line((0,0), lambda x: (0,x), tile_positions, placed_tiles)
# Left column
tile_positions, placed_tiles = fill_line((0,0), lambda x: (x,0), tile_positions, placed_tiles)
# Bottom row
tile_positions, placed_tiles = fill_line((square_size-1,0), lambda x: (square_size-1,x), tile_positions, placed_tiles)
# Right column
tile_positions, placed_tiles = fill_line((0,square_size-1), lambda x: (x,square_size-1), tile_positions, placed_tiles)

# Place middle pieces
for y in range(1, square_size-1):
    for x in range(1, square_size-1):
        neighbours1 = get_neighbours(tile_positions[(y, x-1)]) 
        neighbours2 = get_neighbours(tile_positions[(y-1, x)]) 
        neighbours1 = set([n[0] for n in neighbours1])
        neighbours2 = set([n[0] for n in neighbours2])
        new_tile = [n for n in neighbours1.intersection(neighbours2) if n not in placed_tiles][0]
        tile_positions[(y,x)] = new_tile
        placed_tiles[new_tile] = (y,x)

#for tp in tile_positions:
#    print(tp, tile_positions[tp])
#print(tile_positions)

print(connections)
image = []
for y in range(0, square_size):
    image.append([tile_positions[(y,x)] for x in range(0, square_size)])
    print(image[-1])

flip_img = []
for y in range(0, square_size):
    row = []
    for x in range(0, square_size):
        neighbours = get_neighbours(tile_positions[(y, x)]) 
        flipped = len([1 for n in neighbours if n[2] == 'flipped'])
        row.append(flipped) 
    #print(row)


prev_id = tile_positions[(0,0)] 
flip_grid = {(0,0): False} 
is_flipped = False



for y in range(1, square_size):
    above = image[y-1][0]
    connection = [n for n in get_neighbours(above) if n[0] == image[y][0]][0]
    if connection[2] == 'flipped':
        is_flipped = not is_flipped
    flip_grid[(y,0)] = is_flipped


is_flipped = False
for y in range(0, square_size):
    for x in range(1, square_size):
        left_of = image[y][x-1]
        connection = [n for n in get_neighbours(left_of) if n[0] == image[y][x]][0]

        is_prev_flipped = flip_grid[(y, x-1)]
        is_flipped = (is_prev_flipped and connection[2] == 'unflipped') or (not is_prev_flipped and connection[2] == 'flipped')
        flip_grid[(y,x)] = is_flipped

for y in range(square_size):
    row = ['F' if flip_grid[(y,x)] else '0' for x in range(square_size)] 
    #print(row)


rotation_grid = {} 
for y in range(square_size):
    connection = [n for n in get_neighbours(image[y][1]) if n[0] == image[y][0]][0]
    rotation = (directions.index(connection[1]) + 1 ) % 4
    rotation_grid[(y,0)] = rotation

for y in range(square_size):
    for x in range(1,square_size):
        connection = [n for n in get_neighbours(image[y][x-1]) if n[0] == image[y][x]][0]
        rotation = (directions.index(connection[1]) - 1) % 4 
        rotation_grid[(y,x)] = rotation

for y in range(square_size):
    row = [rotation_grid[(y,x)] for x in range(square_size)] 
    print(row)

import numpy as np
whole_image = {}
for y, row in enumerate(image):
    for x, tile_id in enumerate(row):
        rotate = rotation_grid[(y,x)]
        flip = flip_grid[(y,x)]
        print(rotate, flip)
        tile = tile_inner[tile_id]
        tile_size = len(tile[0])
        #print(tile_id)
        tile = [[1 if ch == '#' else 0 for ch in line] for line in tile]

        tile = np.array(tile, int)
        if flip:
            tile = np.flip(tile, 0)
            rotate = (rotate + 2)%4
            
        #for t in tile:
        #    print(t)


        tile = np.rot90(tile, -rotate)
        #print('...')
        #for t in tile:
            #print(t)

        for a in range(tile_size):
            for b in range(tile_size):
                whole_image[(y*tile_size + a, x*tile_size + b)] = tile[a][b]
        
        

whole_size = tile_size * square_size 
#print(whole_size)

img = []
for y in range(whole_size):
    row = []
    for x in range(whole_size):
        ch = '#' if whole_image[(y,x)] == 1 else '.'
        row.append(ch)
    img.append("".join(row))

for line in img:
    print(line)
        

# Monster coordinates
#   .#...#.###...#.##.O#..
#   O.##.OO#.#.OO.##.OOO##
#   #O.#O#.O##O..O.#O##.##
        
monster = [
    (0, 18),
    (1, 0),
    (1, 5),
    (1, 6),
    (1, 11),
    (1, 12),
    (1, 17),
    (1, 18),
    (1, 19),
    (2, 1),
    (2, 4),
    (2, 7),
    (2, 10),
    (2, 13),
    (2, 16),
]
        

for y in range(whole_size - 3 - 1):
    for x in range(whole_size - 20 - 1):
        relative_coordinates = [(y+a, x+b) for a,b in monster]
        rel = [img[y][x] for (y,x) in relative_coordinates]
        if x == 2 and y == 2:
            print(relative_coordinates)
            print(rel)
        rel = [r == '#' for r in rel]
        found = all(rel)
        if x == 2 and y == 2:
            print(rel)
        if found:
            print(rel)
            print('Found', x,y)
print(whole_size)
print(tile_size)
exit()


# .####...###.#......###..
# #####..#.#.#.....#.###..
# .#.#...#...#..#.#.##..#.
# #.#.##.###..##.######..#
# ..##.####.####..#..####.
# ...#.#..###.#.#...#.#..#
# #.##.#..#.####...####.##
# .###.##.#..#.##..#.#.###
# #.####.##..#.##..##...#.
# ##...#..#.##.#..##..##..
# ..#.##...#.#.##..#...#..
# ....#.##...#...#####...#
# ..##.##...##..##..#.#.#.
# #...#.....#.####..#.#.#.
# .#.##...#.####.##.#...##
# #.###.#..#..###..##.##.#
# #.###.......##.#..#..###
# .###.###..###.#.####.##.
# ..##.#..##..#.######...#
# #.#..##.#.########....##
# #.#####...#.#.#.###.###.
# #....##.###.###.####.###
# #...#....##.###.#.#..#.#
# #..###....######..#.##..
