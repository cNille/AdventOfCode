f = open('03.input', 'r')
content = [x.strip() for x in f.readlines()]
#content = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
#U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""


wires = [
    "R75,D30,R83,U83,L12,D49,R71,U7,L72",
    "U62,R66,U55,R34,D71,R55,D58,R83"
]
wires = [
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
]
wires = content 
for w in wires:
    print(w)

wire = wires[0]
data = wire.split(',')

coor = (0,0)
dots = {}

steps = 0
for i in data:
    if i.startswith("R"):
        for x in range(int(i[1:])):
            coor = (coor[0] + 1, coor[1])
            steps += 1
            if coor not in dots:
                dots[coor] = steps

    if i.startswith("L"):
        for x in range(int(i[1:])):
            coor = (coor[0] -1, coor[1])
            steps += 1
            if coor not in dots:
                dots[coor] = steps

    if i.startswith("U"):
        for x in range(int(i[1:])):
            coor = (coor[0] , coor[1] + 1)
            steps += 1
            if coor not in dots:
                dots[coor] = steps

    if i.startswith("D"):
        for x in range(int(i[1:])):
            coor = (coor[0] , coor[1] - 1)
            steps += 1
            if coor not in dots:
                dots[coor] = steps

wire = wires[1]
data = wire.split(',')

coor = (0,0)
dotstwo = {}

mini = 999999999 
stepstwo = 0
for i in data:
    if i.startswith("R"):
        for x in range(int(i[1:])):
            coor = (coor[0] + 1, coor[1])
            stepstwo += 1
            if coor not in dotstwo:
                dotstwo[coor] = stepstwo

            if coor in dots:
                res = dots[coor] + dotstwo[coor]
                mini = res if res < mini else mini
                print(res, dots[coor], dotstwo[coor], coor)

    if i.startswith("L"):
        for x in range(int(i[1:])):
            coor = (coor[0] - 1, coor[1])
            stepstwo += 1
            if coor not in dotstwo:
                dotstwo[coor] = stepstwo

            if coor in dots:
                res = dots[coor] + dotstwo[coor]
                mini = res if res < mini else mini
                print(res, dots[coor], dotstwo[coor], coor)

    if i.startswith("U"):
        for x in range(int(i[1:])):
            coor = (coor[0] , coor[1] + 1)
            stepstwo += 1
            if coor not in dotstwo:
                dotstwo[coor] = stepstwo

            if coor in dots:
                res = dots[coor] + dotstwo[coor]
                mini = res if res < mini else mini
                print(res, dots[coor], dotstwo[coor], coor)

    if i.startswith("D"):
        for x in range(int(i[1:])):
            coor = (coor[0] , coor[1] - 1)
            stepstwo += 1
            if coor not in dotstwo:
                dotstwo[coor] = stepstwo

            if coor in dots:
                res = dots[coor] + dotstwo[coor]
                mini = res if res < mini else mini
                print(res, dots[coor], dotstwo[coor], coor)

print("mini %d" % mini)



# Not 16517
