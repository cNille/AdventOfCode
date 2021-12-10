f = open('10.test', 'r')
#f = open('10.input', 'r')
lines = [x.strip() for x in f.readlines()]

print('---')
def get_illegal_points(ch):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return points[ch]

def get_incomplete_points(ch):
    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    return points[ch]

illegal_points = 0
incomplete_points = []
t = str.maketrans("([{<", ")]}>")
for line in lines:
    chunk = []
    for ch in line:
        if ch in '({[<':
            chunk.append(ch)
        if ch in ')}]>':
            last = chunk.pop()
            if ch == last.translate(t):
                continue
            illegal_points += get_illegal_points(ch)
            chunk = None
            break
    if chunk is None:
        continue
    
    incomplete = 0
    while len(chunk) > 0:
        last = chunk.pop()
        incomplete *= 5
        incomplete += get_incomplete_points(last)
    incomplete_points.append(incomplete)
    
incomplete_points.sort()
incomplete_winner = incomplete_points[len(incomplete_points) // 2]

print('Solution part 1: %d' % illegal_points)
print('Solution part 2: %d' % incomplete_winner)
