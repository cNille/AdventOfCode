from itertools import permutations
from collections import deque 
from intcode import *

def print_panels(panels, positions):
    xsorted = sorted([x[0] for x in positions]) 
    ysorted = sorted([x[1] for x in positions]) 
    xmax, xmin = xsorted[-1], xsorted[0]
    ymax, ymin = ysorted[-1], ysorted[0]

    result = []
    print(' '*80)
    for x in range(xmin, xmax):
        row = []
        for y in range(ymin,ymax):
            if (x,y) in panels:
                row.append(panels[(x,y)])
            else:
                row.append(0)
        row = "".join(map(str, row))
        row = row.replace("0", ".")
        print("\t" + row)


positions = [(0,0)]
panels = {}
directions = 'URDL'
currentDirection = 0
deltas = { 'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0) }
start_color = 1
start_color = 0
panels[positions[-1]] = start_color 

# Part 1 
input_code = open('11.input', 'r').readline().strip()
stream = Streams(["A"])
intcode = IntCode(input_code)
program = Program(intcode, name="A", stream=stream)

count = 0
while len(panels.keys()) < 10000:
    count += 1
    position = positions[-1]
    #print("%d CURRENT POSITION: %d %d" % (count, position[0], position[1])) 
    if position not in panels:
        panels[position] = 0

    curr_panel_color = panels[position]

    #print "INPUT", curr_panel_color
    stream.add("A", curr_panel_color) 
    outputted = deque() 
    for out in program.run():
        outputted.append(out)
    #print "OUTPUT", outputted

    if count % 100 == 0:
        print(count)
    if len(outputted) == 0:
        break

    new_color = outputted.popleft()
    direction = outputted.popleft()
    #print("Color: %d, dir: %d" % (new_color, direction))

    # Paint panel
    panels[position] = new_color

    # Move position
    x,y = position
    currentDirection += (1 if direction == 1 else -1)
    currentDirection %= 4
    dx, dy = deltas[directions[currentDirection]]
    new_pos = (x+dx, y+dy)

    positions.append(new_pos)
    if count % 400 == 0:
        print_panels(panels, positions)
    #print_panels(panels, positions)

print_panels(panels, positions)
print("Result: %d " % len(panels.keys()))

