testlines = [x.strip() for x in open('12.test', 'r').readlines() if x != '']
lines = [x.strip() for x in open('12.input', 'r').readlines() if x != '']

directions = ['N', 'E', 'S', 'W']
deltas = { 'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0) }
turns = { 'L': -1, 'R': 1 }
def part1(lines):
    x,y = 0, 0
    facing = 'E' 
    for i,line in enumerate(lines):
        direction = line[0]
        distance = int(line[1:])
        if direction in deltas:
            dx, dy = deltas[direction]              
            x += distance * dx
            y += distance * dy
        elif direction in turns:
            rotation = (distance // 90) * turns[direction]
            new_idx = directions.index(facing) + rotation
            facing = directions[new_idx % 4]
        elif direction == 'F':
            dx, dy = deltas[facing]              
            x += distance * dx
            y += distance * dy

    manhattan_distance = abs(x) + abs(y)
    print "Solution part 1: %d" % manhattan_distance 

#part1(testlines)
part1(lines)

# How direction and distance changes the x,y positions 
deltas = { 'N': ( 0, 1), 'E': ( 1, 0), 'S': ( 0,-1), 'W': (-1, 0) }
# Contains how to flip x,y on left and right turns
turns = { 'L': (-1, 1), 'R': ( 1,-1) }
def part2(lines):
    x,y = 0, 0                                      # Position of ship
    wx, wy = 10, 1                                  # Waypoint position
    for i,line in enumerate(lines):
        direction = line[0]
        distance = int(line[1:])
        if direction in deltas:
            # Update waypoints position
            dx, dy = deltas[direction]              
            wx += distance * dx
            wy += distance * dy
        elif direction in turns:
            # Rotate waypoint around the ship
            dx, dy = turns[direction]               # dx,dy -> Helps flipping correctly 
            for i in range(distance // 90):         # Turn 90 at a time
                # Oneline to avoid need for 
                # tmp-variable when swapping
                wx, wy = dx * wy, dy * wx           # Swap x and y and flip
        elif direction == 'F':
            # Update ships position
            x += wx * distance
            y += wy * distance 

    manhattan_distance = abs(x) + abs(y)
    print "Solution part 2: %d" % manhattan_distance 

#part2(testlines)
part2(lines)
# - https://github.com/peter-roland-toth/AoC-2020-Python/blob/main/Day%2012/prog.py
# - https://github.com/sophiebits/adventofcode/blob/main/2020/day12.py
