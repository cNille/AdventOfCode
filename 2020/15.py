from collections import defaultdict, deque
import re

data = '1,3,2'
data = '0,3,6'
data = '15,5,1,4,7,0'


turn = 1
spoken = defaultdict(deque) 
prev = 0

for x in map(int,data.split(',')):
    spoken[x] = [turn]
    prev = x
    turn += 1

prev = 0 

X = 30000001    # Part 2
X = 2021        # Part 1
from time import time
start = time()
while turn < X:
    if turn % 1000000 == 0:
        print time() - start, turn
        start = time()

    if len(spoken[prev]) <= 1:
        prev = 0
    else:
        prev = spoken[prev][-1] - spoken[prev][-2]
    if prev not in spoken:
        spoken[prev] = deque(maxlen=2)
    spoken[prev].append(turn)
    turn += 1

print prev

