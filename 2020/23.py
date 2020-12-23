#cups = '389125467'
cups = '247819356'
cups = [x for x in cups]

def move(cups, current=0):
    current_cup = cups[current]
    input_cups = list(cups)
    #print 'Move:', ",".join(cups)
    pick_up = []
    x = current + 1
    for i in range(3):
        pick_up.append(cups.pop(x if x < len(cups) else 0))
    pick_up_values = list(pick_up)
    #print 'pick up:', pick_up

    sorted_cups = sorted(map(int,cups))
    if sorted_cups[0] == int(current_cup):
        destination_cup = str(sorted_cups[-1])
    else:
        destination_cup = str(sorted_cups[sorted_cups.index(int(current_cup))-1])
    #print "destination_cup", destination_cup
    
    dest_idx = cups.index(destination_cup) 
    while len(pick_up) != 0:
        cups.insert(dest_idx+1, pick_up.pop())

    #print 'Move:', ",".join(cups)
    current_cup_idx = cups.index(current_cup) 
    new_current = current_cup_idx + 1 if current_cup_idx < len(cups)-1 else 0
    return cups, new_current


def part1(cups):
    idx = 0
    for i in range(1,101):
        cups, idx = move(cups, idx)

    one_idx = cups.index('1')
    #print cups[one_idx: one_idx+3]
    #print cups[:3]

    result =  cups[one_idx+1:] + cups[:one_idx]
    print 'Solution part 1:', "".join(result)
part1(list(cups))

class Cup:
    def __init__(self, value):
        self.value = value

    def set_next(self, next_value):
        self.next = next_value
    def set_prev(self, prev):
        self.prev = prev
    def set_one_lower(self, lower):
        self.lower = lower

    def pop_next_three(self):
        first = self.next
        second = self.next.next
        third = self.next.next.next
        fourth = self.next.next.next.next
        self.next = fourth
        fourth.prev = self
        first.prev = None
        third.next = None
        return [first, second, third]

    def __str__(self):
        lower = self.lower.value if hasattr(self, 'lower') else "None"
        return "[Cup %d. low %s, next: %s, prev: %s]" % (self.value, lower, self.next.value, self.prev.value)

def play_round(current):
    picked = current.pop_next_three()
    picked_values = [p.value for p in picked]
    lower = current.lower if hasattr(current, 'lower') else max_cup 
    while True:
        if lower.value in picked_values:
            lower = lower.lower if hasattr(lower, 'lower') else max_cup 
            continue
        picked[0].prev, picked[2].next, lower.next = lower, lower.next, picked[0]
        break
    return current.next

def generate_linked_list(cups):

    # Create double linked list in a circle.
    head = Cup(int(cups[0]))
    current = head
    for c in cups[1:]:
        cup = Cup(int(c))
        cup.set_prev(current)
        current.set_next(cup)
        current = cup
        if cup.value == 1:
            one_cup = cup
        if cup.value == 9:
            max_cup = cup

    current.next = head
    head.prev = current

    # Set lower 
    current = head
    tmp2 = current.prev
    for i in range(9):
        v = current.value
        current2 = current.prev
        for j in range(9):
            if current2.value == v - 1:
                current.set_one_lower(current2)
                break
            current2 = current2.prev
        current = current.next
    return current, head, one_cup, max_cup
current, head, one_cup, max_cup = generate_linked_list(cups)

def line(tmp):
    values = []
    for i in range(9):
        values.append(tmp.value)
        tmp = tmp.next
    return values

current = head
for i in range(1,101):
    current = play_round(current)
values = line(one_cup)[1:]
print "Solution part 1:", "".join(map(str,values))

current, head, one_cup, max_cup = generate_linked_list(cups)

# Generate all numbers 10 through 1.000.000
current = head.prev
for i in range(10, 1000001):
    cup = Cup(int(i))
    cup.set_prev(current)
    lower = current if i != 10 else max_cup
    cup.set_one_lower(lower)
    current.set_next(cup)
    current = cup
max_cup = current
current.next = head

current = head
for i in range(10000000):
    if i % 1000000 == 0:
        print "Part 2 progress...%d %%" % ((i +1000000) / 100000)
    current = play_round(current)

result = one_cup.next.value * one_cup.next.next.value
print "Solution part 2: ", result
