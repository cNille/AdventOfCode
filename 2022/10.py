print(chr(27)+'[2j')
print('\033c')
f = open('10.test', 'r')
f = open('10.input', 'r')
lines = [x.strip() for x in f.readlines()]

stops = [20, 60, 100, 140, 180, 220]
total = 0
cycle = 0
x = 1
pxls = []

def print_px():
    line = ""
    for i, px in enumerate(pxls):
        if i % 40 == 0 and i > 0:
            line += "\n"
        line += px 
    print("Solution part 2:")
    print(line)

def add_cycle():
    global total, cycle, x, stops
    px = "█" if abs((cycle % 40) - x) < 2  else " "
    pxls.append(px)
    cycle += 1
    if len(stops) > 0 and cycle == stops[0]:
        signal = cycle * x 
        total += signal
        stops.pop(0)

for i, line in enumerate(lines):
    if line.startswith("addx"):
        _, value = line.split(' ')
        add_cycle()
        add_cycle()
        x += int(value)
    elif line.startswith("noop"):
        add_cycle()

print("Solution part 1:", total)
print_px()
