data = [x.strip() for x in open('07.input', 'r').readlines()]

def get_instructions():
    instr = {}
    for d in data:
        i, var = d.split(' -> ')
        instr[var] = i
    return instr 

def complement(instr):
    val = instr.split(' ')[1]
    A = int(val) if val not in instr else get_value(val)
    return (A ^ 65535) 
def and_op(a,b):
    A = int(a) if a not in instr else get_value(a)
    B = int(b) if b not in instr else get_value(b)
    return A & B 
def or_op(a,b):
    A = int(a) if a not in instr else get_value(a)
    B = int(b) if b not in instr else get_value(b)
    return A | B 
def lshift_op(a,b):
    A = int(a) if a not in instr else get_value(a)
    B = int(b) if b not in instr else get_value(b)
    return A << B 
def rshift_op(a,b):
    A = int(a) if a not in instr else get_value(a)
    B = int(b) if b not in instr else get_value(b)
    return A >> B 

def get_value(var):
    if var in cache:
        return cache[var]
    i = instr[var]
    #print('Getting %s with instruction: %s' % (var, i))
    if i.startswith('NOT'):
        result = complement(i)
    else:
        i = i.split(' ')
        if len(i) == 1:
            a = i[0]
            result =  int(a) if a not in instr else get_value(a)
        else:
            a, op, b = i
            if op == 'AND':
                result = and_op(a,b)
            if op == 'OR':
                result = or_op(a,b)
            if op == 'LSHIFT':
                result = lshift_op(a,b)
            if op == 'RSHIFT':
                result = rshift_op(a,b)
    cache[var] = result
    return result

# Part 1
cache = {}
instr = get_instructions()
a = get_value('a')
print("Solution of part 1 is: %d " % a) 

# Part 2
cache = {}
instr = get_instructions()
instr['b'] = str(a) 
print("Solution of part 1 is: %d " % get_value('a')) 
