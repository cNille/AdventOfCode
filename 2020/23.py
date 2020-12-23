

cups = '247819356'
cups = [x for x in cups]

def move(cups, current=0):
    print 'Move:', cups, current
    current_cup = cups[current]
    pick_up = []
    x = current + 1
    for i in range(3):
        pick_up.append(cups.pop(x if x < len(cups) else 0))

    print 'pick up:', pick_up

    sorted_cups = sorted(cups)
    if sorted_cups[0] == current_cup:
        destination_cup = sorted_cups[-1]
    else:
        destination_cup = sorted_cups[sorted_cups.index(current_cup)-1]
    print "destination_cup", destination_cup
    
    dest_idx = cups.index(destination_cup) 
    while len(pick_up) != 0:
        cups.insert(dest_idx+1, pick_up.pop())

    current_cup_idx = cups.index(current_cup) 
    new_current = current_cup_idx + 1 if current_cup_idx < len(cups)-1 else 0
    return cups, new_current


#cups = [x for x in '389125467']
idx = 0
for i in range(1,101):
    print "Move: ", i
    cups, idx = move(cups, idx)
    #raw_input()

one_idx = cups.index('1')
result =  cups[one_idx+1:] + cups[:one_idx]

print 'Final', "".join(result)
