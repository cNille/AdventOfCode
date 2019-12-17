from intcode import *
from itertools import permutations
content = open('17.input', 'r').readline().strip()


# Part 1 
def part1():
    input_code = content
    stream = Streams(["A","B"])
    stream.add("A", 1) 
    intcode = IntCode(input_code)
    program = Program(intcode, name="A", stream=stream)

    view = [out for out in program.run()]
    view = [chr(c) for c in view]
    view = "".join(view)
    print(view)
    view = [x for x in view.split('\n') if len(x) > 0]

    result = 0
    for y in range(1,len(view)-2):
        for x in range(1, len(view[0])-2):
            coord = [
                (x, y),
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1),
            ]
            intersection = True
            for a,b in coord:
                if view[b][a] == '.':
                    intersection = False
            if not intersection:
                continue
            
            result += x * y
    print "Part 1: %d" % result
#part1()



def find_path(view, path):
    robots = "^>v<"
    directions = {
        "^": ((-1,0), (1,0)),
        ">": ((0,-1), (0,1)),
        "v": ((1,0), (-1,0)),
        "<": ((0,1), (0,-1)),
    }
    turns = {
        "^": "<>",
        ">": "^v",
        "v": "><",
        "<": "v^",
    }
    leftright = "LR"
    for y, row in enumerate(view):
        for x, c in enumerate(row):
            if c in robots:
                pos = (x,y)
                robot = c
    
    # Look for next direction
    x,y = pos
    for d in directions:
        if robot == d:
            next_found = False
            for i, (dx,dy)  in enumerate(directions[d]):
                if view[y+dy][x+dx] == "#":
                    view[y] = view[y][:x] + turns[robot][i] + view[y][x+1:] 
                    new_robot = turns[robot][i]
                    curr_dir = (dx,dy)
                    next_found = True
                    turn_instruction = leftright[i]
                    break

            # No new direction found
            if not next_found:
                return path

    # Remove old robot position
    view[y] = view[y][:x] + "#" + view[y][x+1:] 

    # Step robot forward
    steps = 0
    (dx,dy) = curr_dir
    while (
        y+dy >= 0 and
        x+dx >= 0 and
        y+dy < len(view) and
        x+dx < len(view[y+dy]) and
        view[y+dy][x+dx] == "#"
    ):
        steps += 1
        y += dy
        x += dx

    # Paint out robot in new position
    view[y] = view[y][:x] + new_robot + view[y][x+1:] 

    # Calculate instructions
    path = "%s,%d," % (turn_instruction, steps)
    return path + find_path(view, path)

    


# Part 2 
def pathfinder():
    intcode = IntCode(input_code)
    program = Program(intcode, name="A", stream=stream)

    view = []
    for out in program.run():
        view.append(out) 
    view = [ chr(c) for c in view]
    view = "".join(view)
    print(view)

    full_path = find_path(view.split('\n'), '')[:-1]
    print full_path

input_code = "2" + content[1:]


# TODO: Programmatically find the abc. Maybe by starting with two first 
#       instructions and continuing until matches go down. Then start with 
#       b until match go down, or found next A.
#       C should be the rest.


#R,6,L,6,L,10,L,8,L,6,L,10,L,6,R,6,L,6,L,10,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,R,6,L,6,L,10,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,R,6,L,6,L,10,R,6,L,8,L,10,R,6,R,6
A = "R,6,L,6,L,10"
#A,L,8,L,6,L,10,L,6,A,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,A,L,8,L,6,L,10,L,6,R,6,L,8,L,10,R,6,A,R,6,L,8,L,10,R,6,R,6
B = "L,8,L,6,L,10,L,6"
#A,B,A,B,R,6,L,8,L,10,R,6,A,B,R,6,L,8,L,10,R,6,A,R,6,L,8,L,10,R,6,R,6
C = "R,6,L,8,L,10,R,6"
main = "A,B,A,B,C,A,B,C,A,C"

stream = Streams(["A"])

# Main input
main = [ord(c) for c in main] + [10]
for x in main:
    stream.add("A", x)
# A input
A = [ord(c) for c in A] + [10]
for x in A:
    stream.add("A", x)
# B input
B = [ord(c) for c in B] + [10]
for x in B:
    stream.add("A", x)
# C input
C = [ord(c) for c in C] + [10]
for x in C:
    stream.add("A", x)
# feed input
feed = "y"
feed = "n"
feed = [ord(feed), 10]
for x in feed:
    stream.add("A", x)

intcode = IntCode(input_code)
program = Program(intcode, name="A", stream=stream)

done = False
while not done:
    out = []
    for o in program.run():
        out.append(o)
        if out[-1] == 10 and out[-2] == 10:
            break

    res = [c for c in out if c >= 256]
    out = [chr(c) for c in out if c < 256]
    out = "".join(out)
    print(out)
    done = len(out) == 0

print "Result", res[0]
