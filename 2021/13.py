f = open('13.test', 'r')
#f = open('13.input', 'r')
content = [x.strip() for x in f.readlines()]

def print_dots(dots):
    min_y = min([y for x,y in dots])
    max_y = max([y for x,y in dots])
    min_x = min([x for x,y in dots])
    max_x = max([x for x,y in dots])

    for y in range(min_y, max_y + 1):
        s = ''
        for x in range(min_x, max_x + 1):
            s += '#' if (x,y) in dots else '.'
        print(s)

dots = set()
for i in content[:content.index('')]:
    x,y = map(int, i.split(','))
    dots.add((x,y))

folds = []
result1 = 0
for idx, fold in enumerate(content[content.index('')+1:]):
    axis, line = fold.split()[-1].split('=')
    line = int(line)

    new_dots = set()
    for x,y in dots:
        if axis == 'y':
            if y < line:
                dot = (x,y)
            else:
                dot = (x, line - abs(y-line))
        else:
            if x < line:
                dot = (x,y)
            else:
                dot = (line - abs(x-line), y)
        new_dots.add(dot)
    dots = new_dots
    if idx == 0:
        result1 = len(dots)
        

print('Solution part 2:')
print_dots(dots)
print("Solution part 1: %d" % result1)
