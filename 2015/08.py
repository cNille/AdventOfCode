data = [x.strip() for x in open('08.input', 'r').readlines()]

# Part 1
tot = 0
ev = 0
for d in data:
    #print(d, len(d), eval(d), len(eval(d)))

    tot += len(d)
    ev += len(eval(d))
print("Part 1 solution: %d" % (tot-ev))

# Part 2
import re
tot = 0
esc = 0 
for d in data:
    e = re.escape(d)
    #print(d, len(d), e, len(e))
    tot += len(d) 
    esc += len(e) + 2

print("Part 2 solution: %d" % (esc-tot))
