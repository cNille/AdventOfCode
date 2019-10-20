data = open('02.input').readlines()

# Part 1:
paper = 0
sizes = [
    map(int, d[:-1].split('x'))
    for d
    in data
]
for (w, l, h) in sizes:
    m = min(w*l,l*h,h*w)
    paper += 2*l*w + 2*w*h + 2*h*l + min(w*l,l*h,h*w)
print("Result part 1: %d" % paper)

# Part 2:

sortedSizes = [sorted(s) for s in sizes]
ribbon = 0
for s in sortedSizes:
    ribbon += 2 * s[0] + 2 * s[1]
    ribbon += s[0] * s[1] * s[2]

print("Result part 2: %d" % ribbon)
