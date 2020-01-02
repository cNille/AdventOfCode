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

#deck = [0,1,2,3,4,5,6,7,8,9]
deck = range(10007)

for i in instr:
    if i.startswith('cut'):
        deck = cut(deck, int(i.split(' ')[1]))
    elif i.startswith('deal with'):
        deck = deal_increment(deck, int(i.split(' ')[3]))
    elif i.startswith('deal into'):
        deck = new_stack(deck)

for i, d in enumerate(deck):
    if d == 2019:
        print "Part 1 result: %d" % i


# Part 2
