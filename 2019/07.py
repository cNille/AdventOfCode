from intcode import *
input_code = open('07.input', 'r').readline().strip()

phaseSettings = permutations([0,1,2,3,4])
res = 0
values = {}
for phase in phaseSettings:
    intcode = IntCode(input_code)
    next_input = 0 
    names = ["A", "B","C","D","E"]
    for i, name in enumerate(names):
        stream = Streams([name])
        program = Program(intcode, name=name, stream=stream)
        stream.add(name, phase[i])
        stream.add(name, next_input)
        
        for out in program.run():
            next_input = out

    res = res if res > next_input else next_input


print('Part 1 result: %d ' % res)

input_code = open('07.input', 'r').readline().strip()
phaseSettings = permutations([5,6,7,8,9])
res = 0
p = []
values = {}

for phase in phaseSettings:
    names = ["A", "B", "C","D","E"]
    stream = Streams(names)
    programs = [
        Program(IntCode(input_code), name="A", stream=stream),
        Program(IntCode(input_code), name="B", stream=stream),
        Program(IntCode(input_code), name="C", stream=stream),
        Program(IntCode(input_code), name="D", stream=stream),
        Program(IntCode(input_code), name="E", stream=stream),
    ]
    stream.add("A", phase[0])
    stream.add("A", 0)
    stream.add("B", phase[1])
    stream.add("C", phase[2])
    stream.add("D", phase[3])
    stream.add("E", phase[4])
    
    count = 0
    while count < 100:   
        count += 1

        pidx = [0,1,2,3,4]
        nidx = [1,2,3,4,0]
        for p,n in zip(pidx, nidx):
            for out in programs[p].run():
                stream.add(names[n], out)
                last = out
                break
        if last > res:
            res = last 
            p = phase

print('Part 2 result: %d ' % res)
