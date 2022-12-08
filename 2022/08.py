print(chr(27)+'[2j')
print('\033c')
f = open('08.test', 'r')
f = open('08.input', 'r')
lines = [x.strip() for x in f.readlines()]

width = len(lines[0])
height = len(lines)
mtx = [[int(y) for y in x] for x in lines]

tvisible = set()
bvisible = set()
lvisible = set()
rvisible = set()
t = [x for x in mtx[0][1:-1]] 
b = [x for x in mtx[-1][1:-1]]
r = [x[-1] for x in mtx[1:-1]] 
l = [x[0] for x in mtx[1:-1]] 
max_score = 0
for y in range(1, height-1):
    for x in range(1, width - 1):

        # Part 1
        tx,ty = x,y
        from_top = mtx[ty][tx]
        if from_top > t[x-1]:
            tvisible.add((tx,ty))
            t[x-1] = from_top

        bx, by = x, height-y-1
        from_bottom = mtx[by][bx]
        if from_bottom > b[x-1]:
            bvisible.add((bx, by))
            b[x-1] = from_bottom

        lx, ly = x,y
        from_left = mtx[ly][lx]
        if from_left > l[y-1]:
            lvisible.add((lx,ly))
            l[y-1] = from_left

        rx, ry = width-x-1, y
        from_right = mtx[ry][rx]
        if from_right > r[y-1]:
            rvisible.add((rx,ry))
            r[y-1] = from_right

        # Part2
        directions=[ 
            (1,0),
            (0,-1),
            (0,1),
            (-1,0),
        ]  
        score =1 
        step = 1
        while len(directions) > 0:
            new_directions = []
            for d in directions:
                dx,dy = d[0]*step, d[1]*step
                x2,y2 = dx + x, dy + y
                if x2 < 0 or y2 < 0:
                    score *= (step-1)
                    continue
                if x2 == width or y2 == height:
                    score *= (step-1)
                    continue
                if mtx[y][x] <= mtx[y2][x2]:
                    score *= step
                    continue
                new_directions.append(d)
            step += 1
            directions = new_directions
        max_score = score if score > max_score else max_score

from colorama import Fore, Back, Style
for y in range(height):
    line = ""
    for x in range(width):
        cell = str(mtx[y][x])
        if (x,y) in tvisible:
            line += Back.BLUE + cell + Style.RESET_ALL
        elif (x,y) in bvisible:
            line += Back.YELLOW  + Fore.BLACK + cell + Style.RESET_ALL
        elif (x,y) in lvisible:
            line += Back.GREEN + Fore.BLACK + cell + Style.RESET_ALL
        elif (x,y) in rvisible:
            line += Back.RED + cell + Style.RESET_ALL
        else:
            line +=  cell 
    print(line)

visible = tvisible.union(bvisible).union(lvisible).union(rvisible)
count = len(visible) + (width-1)*4
print("Solution part 1:", count)
print("Solution part 2:", max_score)
