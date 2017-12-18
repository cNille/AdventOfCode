instr = open('my.input').read().split('\n')
letters = list('aipbf')
var = {}
stack = []
for l in letters:
    var[l] = 0
    
def do_set(curr):
    var[curr[1]] = int(curr[2])

def do_add(curr):
    var[curr[1]] += int(curr[2])

def do_mul(curr):
    var[curr[1]] *= int(curr[2])

def do_mod(curr):
    var[curr[1]] %= int(curr[2])

def do_snd(curr):
    stack.append(var[curr[1]])

def do_rcv(curr):
    if var[curr[1]] > 0:
        print('Hej', stack.pop())
        exit()

def do_jmp(curr, i):
    if var[curr[1]] > 0:
        return i + int(curr[2]) - 1
    return i
i = -1
while i < len(instr):
    i +=1
    curr = instr[i].split(' ')

    print(i, curr, var)

    if len(curr) > 2 and curr[2] in var:
        curr[2] = var[curr[2]]

    if(curr[0] == 'snd'):
        do_snd(curr)
    if(curr[0] == 'set'):
        do_set(curr)
    if(curr[0] == 'add'):
        do_add(curr)
    if(curr[0] == 'mul'):
        do_mul(curr)
    if(curr[0] == 'mod'):
        do_mod(curr)
    if(curr[0] == 'rcv'):
        do_rcv(curr)
    if(curr[0] == 'jgz'):
        i = do_jmp(curr, i)
        

