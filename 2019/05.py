from intcode import *
input_code = '1,9,10,3,2,3,11,0,99,30,40,50'
input_code = open('05.input', 'r').readline().strip()

# Part 1 
intcode = IntCode(input_code)
program = Program(intcode)
for out in program.run(stdin=[1]):
    print("Part 1: %d" % out)

# Part 2 
intcode = IntCode(input_code)
program = Program(intcode)
for out in program.run(stdin=[5]):
    print("Part 2: %d" % out)
