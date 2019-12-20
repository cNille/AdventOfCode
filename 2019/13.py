from intcode import *
import keyboard
from time import sleep
input_code = open('13.input', 'r').readline().strip()

# Part 1
stream = Streams(["A","B"])
intcode = IntCode(input_code)
program = Program(intcode, name="A", stream=stream)

output = []
for out in program.run():
    output.append(out)
print("Part 1: %d" % len([x for i,x in enumerate(output) if (i+1) % 3 == 0 and x == 2]))


# Part 2
tile_types = {
    0: " ",
    1: "#",
    2: "o",
    3: "-",
    4: "@",
}

def render(output,points, bot_playing):
    max_x = 43
    max_y = 19
    for i in range(0,len(output),3):
        points[(output[i], output[i+1])] = output[i+2]
        #max_x = max_x if max_x > output[i] else output[i]
        #max_y = max_y if max_y > output[i+1] else output[i+1]

    tiles_left = 0

    ball = None
    paddle = None
    for y in range(max_y+1):
        row = ""
        for x in range(max_x+1):
            if (x,y) in points:
                tile = points[(x,y)] 
                row += tile_types[tile]

                if tile == 3:
                    paddle = (x,y)
                if tile == 4:
                    ball = (x,y)

                if points[(x,y)] == 2:
                    tiles_left += 1
            else:
                row += " "
        if not bot_playing:
            print row

    score =  None
    if (-1,0) in points:
        score = points[(-1,0)]
        if not bot_playing:
            print "Score: %d" % score 

    return tiles_left, ball, paddle, score


stream = Streams(["A"])
intcode = IntCode("2" + input_code[1:])
program = Program(intcode, name="A", stream=stream)


import sys,tty


tiles_left = 99 
points = {}

fd = sys.stdin.fileno()
old = tty.tcgetattr(fd)
import atexit

def exit_handler():
    tty.tcsetattr(fd, tty.TCSAFLUSH, old)

atexit.register(exit_handler)

game_started = False
bot_playing = True
last_score = 0

while tiles_left > 0:
    output = []
    for out in program.run():
        output.append(out)
    tiles_left, ball, paddle, score = render(output, points, bot_playing)
    last_score = score

    if score != 0:
        game_started = True

    if game_started and score == 0:
        print "GAME OVER"
        exit()

    move = 0
    m = " "

    
    if bot_playing:
        if paddle[0] == ball[0]:
            move = 0
        elif paddle[0] > ball[0]:
            move = -1
        else:
            move = 1
    else:
        tty.setcbreak(sys.stdin)
        key = ord(sys.stdin.read(1))
        if key==97: # a 
            tty.tcsetattr(fd, tty.TCSAFLUSH, old)
            exit()
        if key==104: # h
            move = -1
        if key==116: # t
            move = 1

    stream.add("A", move)
    #sleep(0.1)

print("Part 2: %d" % last_score)
