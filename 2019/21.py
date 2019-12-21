from intcode import *
content = [x.strip() for x in open('21.input', 'r').readlines()][0]
input_code = content


# Part 1
part1 = """
NOT T T
AND A T
AND B T
AND C T
NOT T T
AND D T
NOT T T
NOT T J
WALK
"""

# Part 2
part2 = """
NOT T T
AND A T
AND B T
AND C T
NOT T T
AND D T
NOT T T
NOT T J
AND H J
OR A T
NOT T T
OR T J
RUN
"""

def execute(springscript):

    stream = Streams(["A","B"])
    springscript = [ord(c) for c in springscript[1:-1]] + [10]
    for x in springscript:
        stream.add("A", x)
    program = Program(IntCode(input_code), name="A", stream=stream)

    view = []
    for output in program.run():
        if output < 256:
            view.append(output)
        else:
            return output
    view = [chr(c) for c in view]
    view = "".join(view)
    print(view)

res = execute(part1)
print "Part 1: %d" % res
res = execute(part2)
print "Part 2: %d" % res
