lines = [x.strip() for x in open('22.test', 'r').readlines()]
lines = [x.strip() for x in open('22.input', 'r').readlines()]

p2idx = lines.index('Player 2:') + 1

p1 = lines[1:p2idx-2]
p2 = lines[p2idx:-1]
p1 = map(int, p1)
p2 = map(int, p2)

def part1(p1, p2):
    r = 0
    while len(p1) > 0 and len(p2) > 0:
        r += 1
        #print 'Round ', r
        #print 'p1', p1
        #print 'p2', p2

        p1wins = p1[0] > p2[0]
        if p1wins:
            p1 = p1[1:] + [p1[0], p2[0]]
            p2.pop(0)
        else:
            p2 = p2[1:] + [p2[0], p1[0]]
            p1.pop(0)
        #print '----'

    multiplyer = 1
    total = 0
    p1.reverse()
    for value in p1:
        total += multiplyer * value
        multiplyer += 1
    print 'Solution part 1:', total
part1(list(p1),list(p2))


def calc_points(player):
    multiplyer = 1
    total = 0
    player.reverse()
    for value in player:
        total += multiplyer * value
        multiplyer += 1
    return total

total_rounds = 0
def part2(p1,p2, subgame=0):
    global total_rounds
    total_rounds += 1
    #if total_rounds % 1000 == 0:
    #    print "Rounds", total_rounds
    r = 0
    prev_rounds = []
    while len(p1) > 0 and len(p2) > 0:
        r += 1
        #print 'Round ', r, ' - subgame ', subgame
        #print 'p1', p1
        #print 'p2', p2
        p1wins = p1[0] > p2[0]

        # Check instant win
        round_str = "p1==" + ",".join(map(str,p1)) + ":p2==" + ",".join(map(str,p2))
        if round_str in prev_rounds:
            #print 'P1 INSTANT WIN'
            p2 = []
            break
        else:
            prev_rounds.append(round_str)

        if len(p1) > p1[0] and len(p2) > p2[0]: # Maybe +1 on len
            #print 'RECURSIVE COMBAT'
            rec_p1 = p1[1:p1[0]+1]
            rec_p2 = p2[1:p2[0]+1]
            p1score, p2score = part2(rec_p1, rec_p2, subgame + 1)
            p1wins = p1score > p2score
            #if p1wins:
            #    print "P1 wins subgame with:", p1score
            #else:
            #    print "P2 wins subgame with:", p2score

        if p1wins:
            p1 = p1[1:] + [p1[0], p2.pop(0)]
        else:
            p2 = p2[1:] + [p2[0], p1.pop(0)]
        #print '----'

    
    return [ 
        calc_points(p1),
        calc_points(p2),
    ] 


p1score, p2score = part2(p1,p2)
print "Solution part 2:", p1score


