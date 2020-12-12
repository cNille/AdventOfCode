lines = [x.strip() for x in open('11.test', 'r').readlines() if x != '']
lines = [x.strip() for x in open('11.input', 'r').readlines() if x != '']

deltas= [
    (-1, -1), (-1, 0), (-1, 1), (0, -1),
    (0, 1), (1, -1), (1, 0), (1, 1),
]

EMPTY = '-'
OCC = '#'
SPACE = ' '

t = []
for l in lines:
    t.append(l.replace('L', EMPTY).replace('.',SPACE))
lines = t 

def part1(data):
    new_data = []
    for row in range(len(data)):
        new_data.append('')
        for col in range(len(data[0])):
            neighbours = [(x+col,y+row) for x,y in deltas]
            neighbours = [(x,y) for x,y in neighbours if (0 <= x < len(data[0])) and (0 <= y < len(data))]
            occ_neighbours = [data[y][x] for x,y in neighbours if data[y][x] == OCC] 
            occ_count = len(occ_neighbours)
            #print occ_count, neighbours
            if data[row][col] == EMPTY:
                if occ_count == 0:
                    new_data[-1] = new_data[-1] + OCC
                else:
                    new_data[-1] = new_data[-1] + EMPTY
            elif data[row][col] == OCC:
                if occ_count >= 4:
                    new_data[-1] = new_data[-1] + EMPTY
                else:
                    new_data[-1] = new_data[-1] + OCC
            else:
                new_data[-1] = new_data[-1] + SPACE
    return new_data

def part2(data):
    new_data = []
    col_width = len(data[0])
    row_width = len(data)
    for row in range(len(data)):
        new_data.append('')
        for col in range(len(data[0])):
            occ_count =  0

            verbose = row == 1 and col == 1
            verbose = False 
            for (x,y) in deltas:
                multiplier = 0
                n = SPACE
                while n == SPACE:
                    multiplier +=1
                    x_delta, y_delta = x * multiplier, y * multiplier
                    x_pos, y_pos = x_delta + col, y_delta + row
                    if verbose:
                        print 'oaeu:', x_pos,y_pos, '::', x,y, '::', col, row, '--', x_delta, y_delta 
                    if 0 <= x_pos < col_width and 0 <= y_pos < row_width:
                        n = data[y_pos][x_pos]
                        if verbose:
                            print '     yes:', n , y_pos, x_pos
                    else:
                        n = 'o'
                        if verbose:
                            print '     no:', n , y_pos, x_pos
                        break
        
                #print x_pos,y_pos,n
                if verbose:
                    print 'nille:', x_pos,y_pos,n
                if n == OCC:
                    occ_count += 1


            if verbose:
                print col,row, occ_count 
            if data[row][col] == EMPTY:
                if occ_count == 0:
                    new_data[-1] = new_data[-1] + OCC
                else:
                    new_data[-1] = new_data[-1] + EMPTY
            elif data[row][col] == OCC:
                if occ_count >= 5:
                    new_data[-1] = new_data[-1] + EMPTY
                else:
                    new_data[-1] = new_data[-1] + OCC 
            else:
                new_data[-1] = new_data[-1] + SPACE

    return new_data

from time import sleep
from os import system, name
import sys
def round(data):
    stale = False
    currentmap = data
    i = 0
    while not stale:
        i+=1
        new_map = part2(currentmap)
        #new_map = part1(currentmap)
        stale = "".join(new_map) == "".join(currentmap)
        sleep(0.04)
        for x in data:
            sys.stdout.write(u"\u001b[%dD" % (len(data)+1))
            sys.stdout.write(u"\u001b[%dA" % (len(data)+1))
        sys.stdout.flush()
        currentmap = new_map
        print '-----------------------------------------MAP: %d' % i
        for n in new_map:
            print n


    tot = 0
    for row in currentmap:
        tot += len([x for x in row if x == OCC])



    print tot 


round(lines)
