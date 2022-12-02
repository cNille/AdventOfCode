f = open('02.test', 'r')
f = open('02.input', 'r')
content = [x.strip() for x in f.readlines()]
rounds = [x.split() for x in content if x != '']
rounds = [(x[0],x[1]) for x in rounds]

def part1():
    wins = { 'A': 'Y', 'B': 'Z', 'C': 'X' }
    draws = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
    points = { 'X': 1, 'Y': 2,  'Z': 3 }

    v = 0
    for r in rounds:
        p = points[r[1]] 
        win = 6 if  wins[r[0]] == r[1] else 0
        draw = 3 if  draws[r[0]] == r[1] else 0
        print(r, p, win, draw)

        v += p + win + draw
    return v

print('Part 1', part1())


def part2():
    whand = { 'A': 'Y', 'B': 'Z', 'C': 'X' }
    dhand = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
    lhand = { 'A': 'Z', 'B': 'X', 'C': 'Y' }
    points = { 'X': 1, 'Y': 2,  'Z': 3 }
    wins = { 'X': 0, 'Y': 3,  'Z': 6 }

    v = 0
    for r in rounds:
        win = wins[r[1]] 
        p = 0 
        if win == 0:
            p += points[lhand[r[0]]]
        if win == 3:
            p += points[dhand[r[0]]]
        if win == 6:
            p += points[whand[r[0]]]
        v += p + win 
        print(r, p, win, v)

    print('yay', v)
print('Part 2', part2())
