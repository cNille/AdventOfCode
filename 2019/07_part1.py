from intcode import *
input_code = open('07.input', 'r').readline().strip()

phaseSettings = permutations([0,1,2,3,4])
res = 0
p = []
values = {}
for phase in phaseSettings:
    intcode = IntCode(input_code)
    program = Program(intcode)
    for out in program.run(stdin=[phase[0], 0]):
        A = out 
        break

    intcode = IntCode(input_code)
    program = Program(intcode)
    for out in program.run(stdin=[phase[1], A]):
        B = out 
        break

    intcode = IntCode(input_code)
    program = Program(intcode)
    for out in program.run(stdin=[phase[2], B]):
        C = out 
        break

    intcode = IntCode(input_code)
    program = Program(intcode)
    for out in program.run(stdin=[phase[3], C]):
        D = out 
        break

    intcode = IntCode(input_code)
    program = Program(intcode)
    for out in program.run(stdin=[phase[4], D]):
        E = out 
        break
    if E > res:
        res = E
        p = phase


print('Part 1 result: %d ' % res)
