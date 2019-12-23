from collections import deque
from intcode import *
content = [x.strip() for x in open('23.input', 'r').readlines()][0]
input_code = content

computer_names = map(str, range(50))
stream = Streams(computer_names)

computers = {} 
send_queue = deque()
for name in computer_names:
    computers[name] = Program(IntCode(input_code), name=name, stream=stream)
    stream.add(name, int(name))
    send_queue.append((name, -1))

NAT = None
prev = -1
while True:
    if len(send_queue) == 0 and NAT != None:
        if prev == NAT[1]:
            print "Part 2: %d" % prev
            exit()

        prev = NAT[1]
        send_queue.append(("0", NAT[0]))
        send_queue.append(("0", NAT[1]))

    name, value = send_queue.popleft()

    if name == "255":
        X = value
        name, Y = send_queue.popleft()

        if NAT == None:
            print "Part 1: %d" % Y
        NAT = (X,Y)
        continue

    stream.add(name, value)

    # Get outputs from next computer
    output = []
    for out in computers[name].run():
        output.append(out) 


    # Register outputs in stream
    for i in range(0, len(output), 3):
        name = str(output[i])
        X = output[i+1]
        Y = output[i+2]
        send_queue.append((name, X))
        send_queue.append((name, Y))
