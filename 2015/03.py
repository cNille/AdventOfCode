data = open('03.input').read()

# Part 1:

directions = {
    '>' : (0 , 1),
    '<' : (0 , -1),
    '^' : (1 , 0),
    'v' : (-1 , 0),
}

position = (0, 0)
visited = { (0,0): 0}
for s in data:
    if s not in directions:
        continue

    newx, newy = directions[s]
    x,y = position
    position = (x + newx, y + newy)

    if position not in visited:
        visited[position] = 0
    else:
        visited[position] += 1

print("Solution part 1: %d" % len(visited.items()))


# Part 2:

positions = ((0, 0), (0,0))
visited = { (0,0): 2}

for i, s in enumerate(data):

    if s not in directions:
        continue

    newx, newy = directions[s]
    position = positions[i%2]
    x,y = position
    position = (x + newx, y + newy)

    if position not in visited:
        visited[position] = 0
    else:
        visited[position] += 1

    if i%2 == 0:
        positions = (position, positions[1])
    else:
        positions = (positions[0], position)



print("Solution part 2: %d" % len(visited.items()))

