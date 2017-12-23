instr = open('test_input').read().split('\n')
letters = list('abcdefgh')
var = {}
stack = []
for l in letters:
    var[l] = 0
var['a'] = 1    
    
def do_set(curr):
    var[curr[1]] = int(curr[2])

def do_add(curr):
    var[curr[1]] += int(curr[2])

def do_sub(curr):
    var[curr[1]] -= int(curr[2])

def do_mul(curr):
    var[curr[1]] *= int(curr[2])

def do_jmp(curr, i):
    if curr[1].isdigit() and curr[1] != 0:
        return i + int(curr[2]) - 1
    if var[curr[1]] != 0:
        return i + int(curr[2]) - 1
    return i

i = -1

while i < len(instr) - 1:
    i +=1
    curr = instr[i].split(' ')
    
    if i == 25:
        print(i, curr, var)

    if len(curr) > 2 and curr[2] in var:
        curr[2] = var[curr[2]]

    if i == 11:
        if var['b'] % var['d'] == 0:
            var['f'] = 0
        var['e'] = var['b']
        var['d'] += 1 
        var['g'] = var['d'] - var['b']
        i = 22
        continue

    if(curr[0] == 'set'):
        do_set(curr)
    if(curr[0] == 'add'):
        do_add(curr)
    if(curr[0] == 'sub'):
        do_sub(curr)
    if(curr[0] == 'mul'):
        do_mul(curr)
    if(curr[0] == 'jnz'):
        i = do_jmp(curr, i)
        

print('Done, final:', var)
