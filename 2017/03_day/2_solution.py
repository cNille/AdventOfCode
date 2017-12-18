
def calculateRing(startvalue, width, maxvalue, acc = []):
    
    half = int(width / 2)
    startPos = (half , -half + 1)

    positions = getPositions(width, startPos)

    for p in positions:
        neighbours = [elem for elem in acc if isNeighbour(p, elem[0]) ]

        value = sum(list(map((lambda x: x[1]), neighbours)))

        acc.append( (p, value) )

    if(acc[-1][1] <= maxvalue):
        return calculateRing(startvalue, width + 2, maxvalue, acc)
    else:    
        return acc

def isNeighbour(x,y):
    return abs(x[0] - y[0]) <= 1 and abs(x[1] - y[-1]) <= 1


def getPositions(width, startPos):
    positions = []
    x = startPos[0]
    y = startPos[1]

    deltaY = 0
    deltaX = 0
    for i in range(0, width - 1):
        positions.append( (x, y + i ) )
        deltaY = i 

    for i in range(1, width ):
        positions.append( (x - i, y + deltaY ) )
        deltaX = i

    for i in range(1, width ):
        positions.append( (x - deltaX, y + deltaY - i ) )

    deltaY = int((width / 2) )
    for i in range(1, width ):
        positions.append( (x - deltaX + i, -deltaY ) )
    return positions


acc = calculateRing(1, 1, 289326, [((0,0), 1)])

biggerThan = [elem for elem in acc if elem[1] > 289326]
print("Result:" , biggerThan[0])

for a in acc:
    print(a[1])

