from intcode import *
input_code = '1,9,10,3,2,3,11,0,99,30,40,50'
input_code = open('02.input', 'r').readline().strip()


# Part 1 
intcode = IntCode(input_code)
intcode.instructions[1] = 12
intcode.instructions[2] = 2
program = Program(intcode)
for stack in  program.run(get_stack=True):
    print("Part 1: %d" % stack.stack[0])

# Part 2 

needle = 19690720
for x in range(100):
    for y in range(100):
        intcode = IntCode(input_code)
        intcode.instructions[1] = x 
        intcode.instructions[2] = y 
        program = Program(intcode)
        for stack in  program.run(get_stack=True):
            answ = stack.stack[0]
            if answ == needle:
                print("Part 2: %d" % (100*x+y) )
                exit()


