from intcode import *
from itertools import permutations
content = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
content = "104,1125899906842624,99"
content = "1102,34915192,34915192,7,4,7,99,0"
content = open('09.input', 'r').readline().strip()

input_code = content

# Part 1 
stream = Streams(["A","B"])
stream.add("A", 1) 
intcode = IntCode(input_code)
program = Program(intcode, name="A", stream=stream)
for out in program.run():
    last = out

print("Part 1: %d" % last)

# Part 2 
stream = Streams(["A","B"])
stream.add("B", 2) 
intcode = IntCode(input_code)
program = Program(intcode, name="B", stream=stream)
for out in program.run():
    last = out

print("Part 2: %d" % last)


