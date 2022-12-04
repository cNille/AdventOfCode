print(chr(27)+'[2j')
print('\033c')
import itertools
import functools

f = open('21.test', 'r')
f = open('21.input', 'r')
data = [x.strip() for x in f.readlines()]

p1 = int(data[0][-1])
p2 = int(data[1][-1])
print("Player 1 starts with %d points" % (p1))
print("Player 2 starts with %d points" % (p2))

rolls = 0
score1 = 0
score2 = 0
turn = 0

while score1 < 1000 and score2 < 1000:
    roll = 0
    # roll 1
    rolls = (rolls + 1) % 100 
    roll = (roll + rolls) % 10

    # roll 2
    rolls = (rolls + 1) % 100 
    roll = (roll + rolls) % 10

    # roll 3
    rolls = (rolls + 1) % 100 
    roll = (roll + rolls) % 10

    if turn % 2 == 0:
        p1 += roll
        score1 += 10 if p1 % 10 == 0 else p1 % 10  
    else:
        p2 += roll
        score2 += 10 if p2 % 10 == 0 else p2 % 10  
    turn += 1

print("Part 1 solution: %d" % (min(score1,score2) * turn * 3))


p1 = int(data[0][-1])
p2 = int(data[1][-1])

@functools.lru_cache(maxsize=None)
def part2(position1, score1, position2, score2):
    win1 = 0
    win2 = 0
    for roll1, roll2, roll3 in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        new_position = position1 + roll1+roll2+roll3
        if(new_position > 10):
            new_position -= 10
        new_score = score1 + new_position
        if new_score >= 21:
            win1 += 1
        else:
            w2, w1 = part2(position2, score2, new_position, new_score)    
            win1 += w1
            win2 += w2
    return win1, win2

wins = part2(p1, 0, p2, 0)
print("Solution part 2:", max(wins))
