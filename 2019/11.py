from itertools import permutations
from collections import deque 

content = open('11.input', 'r').readline().strip()

def new_data():
    return [int(x) for x in content.split(',')]

def val(data, mode, idx, relative):
    assert mode in [0,1,2]
    if mode == 0:
        return get_position(data, idx)
    elif mode == 1:
        return immediate(data, idx)
    elif mode == 2:
        return immediate(data, relative + immediate(data, idx))
    
def immediate(data,idx):
    return get(data, idx)

def rel_pos(data,idx):
    return get(data, idx)
     
def get_position(data,idx):
    return get(data, get(data, idx))

def get_modes(opcode):
    mode_a = (opcode % 1000) / 100
    mode_b = (opcode % 10000) / 1000
    mode_c = (opcode % 100000) / 10000
    return mode_a, mode_b, mode_c

mem = {}
def save(data, pos, val):
    if pos >= len(data) or pos < 0:
        mem[pos] = val
    else:
        data[pos] = val
    return data

def get(data, pos, mode_c=0, relative=0):
    if mode_c == 2:
        return _get(data,pos) + relative
    else:
        return _get(data,pos)

def _get(data, pos):
    if pos > len(data):
        if pos not in mem:
            mem[pos] = 0
        return mem[pos] 
    else:
        return data[pos] 
    
def add(data,A,B,curr, mode_c,relative):
    return save(data, get(data, curr+3, mode_c,relative), A+B), curr + 4

def multiply(data,A,B,curr, mode_c,relative):
    return save(data, get(data, curr+3, mode_c, relative), A * B), curr + 4

def inputs(data, curr, mode_a, relative, programCode):
    #print("INPUT at %d" % (curr+1), mode_a, relative, outputStore[programCode])
    if len(outputStore[programCode]) > 0:
        val = outputStore[programCode].popleft() 
        data = save(data, get(data, curr+1, mode_a, relative), val)
        return data, curr + 2, True
    else:
        return data, curr, False

def outputs(data, A, curr, programCode, mode, relative):
    #print("OUTPUT %d, at %d" % (A, curr), get(data, curr, mode, relative), mode)
    outputStore[nextP[programCode]].append(A)
    datas[programCode] = (data, curr)
    #q.append(nextP[programCode])
    return data, curr + 2

def goto_true(A,B,curr):
    return B if A != 0 else curr+3

def goto_false(A,B,curr):
    return B if A == 0 else curr+3

def less(data, A, B, curr, mode_c,relative):
    save(data, get(data, curr+3, mode_c,relative), 1 if A < B else 0)
    curr += 4
    return data, curr

def equals(data, A, B, curr, mode_c,relative):
    save(data, get(data, curr+3, mode_c,relative), 1 if A == B else 0)
    curr += 4
    return data, curr

def update_relative(relative, A, curr):
    return relative + A, curr+2


def program(programCode):
    state = datas[programCode]
    data, curr = state
    relative = 0
    while data[curr] != 99:
        # print("OPERATION %d: %d %d %d" % (
        #     curr, 
        #     data[curr], 
        #     get(data, curr+1),
        #     get(data, curr+2),
        # ))
        opcode = data[curr] % 100
        mode_a, mode_b, mode_c = get_modes(data[curr])

        A = val(data, mode_a, curr+1, relative)
        if opcode in [1,2,5,6,7,8]:
            B = val(data, mode_b, curr+2, relative)
        
        if opcode == 1:
            data, curr = add(data,A,B,curr, mode_c,relative)
        elif opcode == 2:
            data, curr = multiply(data,A,B,curr, mode_c,relative)
        elif opcode == 3:
            data,curr,proceed = inputs(data, curr, mode_a, relative, programCode)
            if not proceed:
                datas[programCode] = (data, curr) 
                return
        elif opcode == 4:
            data, curr = outputs(data, A, curr, programCode, mode_a, relative)
        elif opcode == 5:
            curr = goto_true(A,B,curr) 
        elif opcode == 6:
            curr = goto_false(A,B,curr)
        elif opcode == 7:
            data, curr = less(data,A,B,curr, mode_c,relative)
        elif opcode == 8:
            data, curr = equals(data,A,B,curr, mode_c,relative)
        elif opcode == 9:
            relative, curr = update_relative(relative, A, curr)
        else: 
            exit('fatal error, opcode received: %d' % opcode)
        datas[programCode] = (data, curr) 
    return 

datas = {
    'a': (new_data(), 0),
    'b': (new_data(), 0),
}
outputStore = {
    'a': deque([]),
    'b': deque([]),
}
nextP = {
    'a': 'b',
}
q = deque('a')

positions = [(0,0)]
panels = {}
directions = 'URDL'
currentDirection = 0
deltas = {
    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),
}

start_color = 0
start_color = 1
panels[positions[-1]] = start_color 

def print_panels(panels, positions):
    xsorted = sorted([x[0] for x in positions]) 
    ysorted = sorted([x[1] for x in positions]) 
    xmax, xmin = xsorted[-1], xsorted[0]
    ymax, ymin = ysorted[-1], ysorted[0]

    result = []
    print(' '*80)
    for x in range(xmin, xmax):
        row = []
        for y in range(ymin,ymax):
            if (x,y) in panels:
                row.append(panels[(x,y)])
            else:
                row.append(0)
        row = "".join(map(str, row))
        row = row.replace("0", ".")
        print("\t" + row)

count = 0
while len(panels.keys()) < 10000:
    count += 1
    position = positions[-1]
    print("%d CURRENT POSITION: %d %d" % (count, position[0], position[1]), datas['a'][1]) 
    if position not in panels:
        panels[position] = 0

    curr_panel_color = panels[position]
    outputStore['a'].append(curr_panel_color)
    program('a')

    outputted = outputStore['b']
    if count % 100000 == 0:
        print(count)
    if len(outputted) == 0:
        break
        # outputted = outputStore['b']
        # while len(outputted) == 0:
        #     count += 1
        #     program('a')
        #     if count % 100000 == 0:
        #         print(count)

    new_color = outputStore['b'].popleft()
    direction = outputStore['b'].popleft()
    #print("Color: %d, dir: %d" % (new_color, direction))

    # Paint panel
    panels[position] = new_color

    # Move position
    x,y = position
    currentDirection += (1 if direction == 1 else -1)
    currentDirection %= 4
    dx, dy = deltas[directions[currentDirection]]
    new_pos = (x+dx, y+dy)

    positions.append(new_pos)
    if count % 50 == 0:
        print_panels(panels, positions)
    #print_panels(panels, positions)

print_panels(panels, positions)
print("Result: %d " % len(panels.keys()))
