from intcode import *
input_code = '1,9,10,3,2,3,11,0,99,30,40,50'
input_code = open('05.input', 'r').readline().strip()

# Part 1 
stream = Streams(["A","B"])
stream.add("A", 1) 
intcode = IntCode(input_code)
program = Program(intcode, name="A", stream=stream)
for out in program.run(stdin=[1]):
    last = out
print("Part 1: %d" % last)

# Part 2 
intcode = IntCode(input_code)
stream.add("B", 5) 
program = Program(intcode, name="B", stream=stream)
for out in program.run(stdin=[5]):
    print("Part 2: %d" % out)
