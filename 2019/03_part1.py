f = open('03.input', 'r')
content = [x.strip() for x in f.readlines()]
#content = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
#U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
print(content)
wires = content 


wire = wires[0]
data = wire.split(',')
print(data)

coor = (0,0)
dots = {}

for i in data:
    #print(i)
    if i.startswith("R"):
        for x in range(int(i[1:])):
            #print(coor)   
            coor = (coor[0] + 1, coor[1])
            if coor not in dots:
                dots[coor] = 1

    if i.startswith("L"):
        for x in range(int(i[1:])):
            #print(coor)   
            coor = (coor[0] -1, coor[1])
            if coor not in dots:
                dots[coor] = 1

    if i.startswith("U"):
        for x in range(int(i[1:])):
            #print(coor)   
            coor = (coor[0] , coor[1] + 1)
            if coor not in dots:
                dots[coor] = 1

    if i.startswith("D"):
        for x in range(int(i[1:])):
            #print(coor)   
            coor = (coor[0] , coor[1] - 1)
            if coor not in dots:
                dots[coor] = 1


#print(dots)

wire = wires[1]
data = wire.split(',')
print(data)

coor = (0,0)
dotstwo = {}

mini = 999999999 
for i in data:
    #print(i)
    if i.startswith("R"):
        for x in range(int(i[1:])):
            coor = (coor[0] + 1, coor[1])
            if coor not in dotstwo:
                dotstwo[coor] = 1

            if coor in dots:
                print(coor)
                res = abs(coor[1]) + abs(coor[0])
                mini = res if res < mini else mini
                print(res)

    if i.startswith("L"):
        for x in range(int(i[1:])):
            coor = (coor[0] - 1, coor[1])
            if coor not in dotstwo:
                dotstwo[coor] = 1

            if coor in dots:
                print(coor)
                res = abs(coor[1]) + abs(coor[0])
                mini = res if res < mini else mini
                print(res)

    if i.startswith("U"):
        for x in range(int(i[1:])):
            coor = (coor[0] , coor[1] + 1)
            if coor not in dotstwo:
                dotstwo[coor] = 1

            if coor in dots:
                print(coor)
                res = abs(coor[1]) + abs(coor[0])
                mini = res if res < mini else mini
                print(res)

    if i.startswith("D"):
        for x in range(int(i[1:])):
            coor = (coor[0] , coor[1] - 1)
            if coor not in dotstwo:
                dotstwo[coor] = 1

            if coor in dots:
                print(coor)
                res = abs(coor[1]) + abs(coor[0])
                mini = res if res < mini else mini
                print(res)

print("mini %d" % mini)

    #print(coor)


