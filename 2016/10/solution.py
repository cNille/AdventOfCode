from collections import deque
import re 
from collections import defaultdict
lines = [x.strip() for x in open('test.txt', 'r').readlines()]
lines = [x.strip() for x in open('data.txt', 'r').readlines()]

bots = defaultdict(list)
rules = defaultdict(list) 

def work_queue(bots, rules):
    queue = deque([]) 
    for b in bots:
        if len(bots[b]) > 1:
            queue.append(b)

    while len(queue) > 0:
        b = queue.popleft()
        if b in rules and 'output' not in b and len(bots[b]) > 1:
            low, high = sorted(bots[b]) 
            bots[b] = []
            if low == 17 and high == 61: 
                print "Solution part 1: %s" % b
            low_to, high_to = rules[b]
            bots[low_to].append(low)
            bots[high_to].append(high)
            queue.append(low_to)
            queue.append(high_to)
    return bots, rules

for line in lines:
    if 'gives' in line:
        from_bot, low_to, high_to = re.match(r'(\w+ \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', line).groups()
        rules[from_bot] = [low_to, high_to]
    if 'goes' in line:
        value, id = re.match(r'value (\d+) goes to (\w+ \d+)', line).groups()

        bots[id].append(int(value))

bots, rules = work_queue(bots,rules)

outputs = {b: bots[b] for b in bots if 'output' in b}
result = outputs['output 0'][0] * outputs['output 1'][0] * outputs['output 2'][0]
print "Solution part 2: %d" % result
