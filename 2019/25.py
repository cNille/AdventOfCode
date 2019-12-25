from intcode import *
content = [x.strip() for x in open('25.input', 'r').readlines()][0]
input_code = content


stream = Streams(["A"])
program = Program(IntCode(input_code), name="A", stream=stream)
commands = [
    "east",
    "south",
    "south",
    "take hologram",
    "north",
    "north",
    "west",
    "south",
    "take mouse",
    "east",
    "take shell",
    "west",
    "west",
    "take whirled peas",
    "east",
    "north",
    "west",
    "north",
    "west",
    "south",
    "take hypercube",
    "north",
    "east",
    "north",
    "west",
    "take semiconductor",
    "east",
    "south",
    "south",
    "west",
    "take antenna",
    "west",
    "south",
    "south",
]
commands = [x + '\n' for x in commands]

while len(commands) > 0:
    view = "" 
    for output in program.run():
        view += chr(output)

        if view.endswith('Command?'):
            break

    view = "".join(view)
    print(view)

    #if len(commands) == 0:
    #    command = raw_input()
    #else:
    #    command = commands.pop(0)
    command = commands.pop(0)

    print "Command: %s" % command
    command = [ord(c) for c in command.strip()] + [10]
    for x in command:
        stream.add("A", x)

items = [
    "hologram", 
    "mouse", 
    "shell", 
    "whirled peas", 
    "hypercube", 
    "antenna", 
    "semiconductor"
]
from itertools import permutations
tests = [] 
for i in range(len(items)):
    test = list(permutations(items, i+1))
    for te in test:
        t = list(te)
        t.sort()
        t = tuple(t)
        if t not in tests:
            tests.append(t)

tests.reverse()

for test in tests:
#for test in []:
    for i in items:
        commands += ["drop %s" % i]

    for t in test:
        commands += ["take %s" % t]
    commands += ["south"]


first = True
while True:
    
    view = "" 
    for output in program.run():
        view += chr(output)

        if view.endswith('Command?'):
            break

    view = "".join(view)

    if len(commands) == 0:
        command = raw_input()
        print view
    else:
        command = commands.pop(0)
        if 'You drop the' not in view and 'You take the' not in view and 'You don\'t have that item.' not in view and 'Alert! Droids on this ship are' not in view:
            print(view)
            if not first:
                exit()
            first = False

    print "COMMAND: %s" % command
    command = [ord(c) for c in command.strip()] + [10]
    for x in command:
        stream.add("A", x)

