# Import data
#data = open('day_13_test.txt','r').readlines()
data = open('day_13_input.txt','r').readlines()

# TODO: Improvement suggestion. Move the carts, don't check for all positions
#       if there is a cart there. Too slow in part 2...
 
 # Create a map over the path without any carts.
 # This map is for easier moving carts and knowing what character goes
 # to their last position
clean_path = []
for d in data:
    clean_d = d
    clean_d = clean_d.replace('^', '|')
    clean_d = clean_d.replace('v', '|')
    clean_d = clean_d.replace('<', '-')
    clean_d = clean_d.replace('>', '-')
    clean_path.append(clean_d)

# Keep track if a crash has occured
crash = False

# Detect crashes
def iscrash(ch,x,y):
    global crash
    l = ['^', 'v', '<','>']
    if ch in l:
        if not crash:
            print('Part 1 solution is: %d, %d' % (x,y))
            crash = True
        print('CRASH IN %d,%d' % (x,y))
        return True

directions = ['^', '>', 'v', '<']
# Turning left, straight or right depending on direction by moving
# along the directions list
def turn(ch, direction):
    i = directions.index(ch)

    new_ch = ((direction % 3) - 1) + i
    result = directions[new_ch % len(directions)]
    return result

carts = {}
# Use template method to minimize code. Not pretty, but quicker to edit...
def moveup(x,y):
    move(x,y,-1,0,'^', '>','<')
def movedown(x,y):
    move(x,y,1,0,'v', '<','>')
def moveleft(x,y):
    move(x,y,0,-1,'<','v','^')
def moveright(x,y):
    move(x,y,0,1,'>','^','v')
def move(x,y, d1, d2, ch, ch1, ch2):
    if x+d2 >= len(data[y+d1]):
        return

    if (x,y) not in carts:
        # Init cart by left turn
        carts[(x,y)] = -2

    # Get the char at the new pos
    newpos = data[y+d1][x+d2]

    if iscrash(newpos,x+d2,y+d1):
        # Remove carts and unset them from carts list
        data[y+d1] = data[y+d1][:x+d2] + clean_path[y+d1][x+d2] + data[y+d1][x+d2+1:]
        data[y] = data[y][:x] + clean_path[y][x] + data[y][x+1:]
        del carts[(x,y)]
        del carts[(x+d2,y+d1)]
        return

    # Handle turns
    newchar = ch
    if newpos == '/':
        newchar = ch1
    if newpos == '\\':
        newchar = ch2
    if newpos == '+':
        carts[(x,y)] += 1
        new_direction = carts[(x,y)]+1
        newchar = turn(ch, new_direction)

    # Move the carts value in the carts dictionary
    carts[(x+d2, y+d1)] = carts[(x,y)]
    del carts[(x,y)]

    # Move the cart one step and use the clean_path to set the 
    # current position to its correct value
    data[y+d1] = data[y+d1][:x+d2] + newchar + data[y+d1][x+d2+1:]
    data[y] = data[y][:x] + clean_path[y][x] + data[y][x+1:]

iteration = 0
while True:
    skip = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x,y) in skip and skip[(x,y)]:
                skip[(x,y)]= False
                continue
            if data[y][x] == '^':
                moveup(x,y)
            if data[y][x] == 'v':
                movedown(x,y)
                skip[(x,y+1)] = True
            if data[y][x] == '<':
                moveleft(x,y)
            if data[y][x] == '>':
                moveright(x,y)
                skip[(x+1,y)] = True
    cs = len(carts)
    if iteration % 100 == 0:
        print('Carts left: %d' % cs)

    if cs <= 1:
        print('One cart left!!')
        print(carts)
        exit()
    iteration += 1
