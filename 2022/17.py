print(chr(27)+'[2j')
print('\033c')
f = open('17.test', 'r')
f = open('17.input', 'r')
pushes = [x for x in f.read().strip()]

def show(curr, rest, H):
    print("--------- Fall")
    max_h = max(
        H+3, 
        max({x[1] for x in rest})+3, 
        max({x[1] for x in curr}), 
    )
    rows = 0
    for y in range(max_h, -1, -1):
        line = "|"
        for x in range(W):
            if (x,y) in curr:
                line += '@'
            elif (x,y) in rest:
                line += '#'
            else:
                line += '.'
        line += "|"
        print(line)
        rows += 1 
        if rows > 10:
            break
    print("---------")

SHAPES = [
    {(0,0), (1,0), (2,0), (3,0)},
    {(1,0), (0,1), (1,1), (1,2), (2,1)},
    {(0,0), (1,0), (2,0), (2,1), (2,2)},
    {(0,0), (0,1), (0,2), (0,3)},
    {(0,0), (0,1), (1,0), (1,1)},
]

print("Day 17")
print("P", len(pushes))
S = len(SHAPES)
P = len(pushes)
W = 7

def play(nbr):
    print("PLAY FOR", nbr)
    print("ROCKS", S)
    print("PUSHES", P)
    H = 0
    floor = {(0,-1), (1,-1), (2,-1), (3,-1), (4,-1), (5,-1), (6,-1)}
    rest = floor 
    count = -1 
    optimize = False 
    start_h = 0
    start_i = 0
    offset = 0
    start_curr = 0
    last_h = 0
    i = -1
    while i < nbr:
        #if skip_i > 0:
        #    skip_i -= 1
        #    continue
        i += 1
        if i % 100000 == 0:
            print("Itr", i, H)
        si = i % len(SHAPES)
        x_offset = 2
        y_offset = H + 3 
        curr = {(x+x_offset, y+y_offset) for x,y in SHAPES[si]}
        
        is_resting = False
        #show(curr, rest, H)
        while not is_resting:
            # Push
            count += 1
            if  optimize and i % 5 == start_curr and count % P == offset:
                print('-'*20)
                round_length = (i - start_i)
                left = (nbr - i) 
                rounds_left = left // round_length
                old_h = H
                old_i = i 
                new_i = i + (rounds_left * round_length)
                new_h = H + (rounds_left * (H-start_h)) 
                new_h += 1 - last_h # Guess it's a off by 1 err and a rock counted twice.
                print("Optimize", H, count , i, start_curr)
                print("Rounds length", round_length)
                print("Left", left)
                print("Rounds left", rounds_left)
                print("old_h", old_h)
                print("New_h", new_h)
                print("diff_h", new_h - old_h)
                print("old_i", old_i)
                print("New_i", new_i)
                print("diff_i", new_i - old_i)
                diff = new_h - old_h
                H = new_h
                i = new_i
                rest = {(x, y+diff) for x,y in rest}
                is_resting = True
                break
            if i > 10000 and count % S == 0 and count % P == 0 and not optimize:
                print("Match", count, P, S)
                print("Highest point", H)
                optimize = True
                offset = count % P
                start_h = H
                start_curr = i % 5
                start_i = i
                print("offset", offset)
                print("start_curr", start_curr)

            p = pushes[count % len(pushes)]
            dx = 1 if p == '>' else -1
            side = {(x+dx, y) for x,y in curr}
            xs = {x[0] for x in side}
            if not side & rest and 0 <= min(xs) and max(xs) < W:
                curr = side
            # Fall
            down = {(x, y-1) for x,y in curr}
            if down & rest or down & floor:
                break
            curr = down

        rest = rest | curr
        if i % 10 == 0:
            rest = {(x,y) for x,y in rest if H-y < 40}
        h0 = H
        H = max(H, max({x[1] for x in curr}) +1)
        h1 = H
        last_h = h1 - h0
    return H

part1 = play(2022)
print("Solution part 1:", part1)
part2 = play(1000000000000)
print("Result part 2:", part2)
