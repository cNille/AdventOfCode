instr = [x.strip() for x in open('22.inputtest', 'r').readlines()]
instr = [x.strip() for x in open('22.input', 'r').readlines()]

def new_stack(deck):
    deck.reverse()
    return deck

def cut(deck, pos):
    return deck[pos:] + deck[:pos]

def deal_increment(deck, incr):
    d = [-1] * len(deck)
    for i, card in enumerate(deck):
        d[(i*incr) % len(deck)] = card
    return d

deck = range(10007)

x = 0
positions = {}
for i in instr:
    if i.startswith('cut'):
        deck = cut(deck, int(i.split(' ')[1]))
    elif i.startswith('deal with'):
        deck = deal_increment(deck, int(i.split(' ')[3]))
    elif i.startswith('deal into'):
        deck = new_stack(deck)

for i, d in enumerate(deck):
    if d == 2019:
        print "Part 1: %d" % (i)
        positions[i] = x
        break

# ===========================
# Part 2

deck_size = 119315717514047 
MOD = deck_size
iterations = 101741582076661
pos = 2020

offset = 0
increment = 1
for i in instr:
    i = i.split(' ')
    if 'cut' in i:
        offset += increment * int(i[1])
        offset %= MOD
    elif 'with' in i:
        increment *= pow(int(i[3]), MOD-2, MOD)
        increment %= MOD
    elif 'into' in i:
        increment *= -1    
        increment %= MOD
        offset += increment
        offset %= MOD

all_multi = pow(increment, iterations, MOD)
all_addi = (offset * (1 - all_multi) * pow(1-increment, MOD-2, MOD)) % MOD
res = (pos * all_multi + all_addi) % MOD
print "Part 2: %d" % res
