import datetime
import operator

def sort_dic_by_values(d):
    return sorted(d.items(), key=operator.itemgetter(1))

# Import data
data = [x.strip() for x in open('day_05_input.txt','r').readlines()]
data = data[0]
abc = 'abcdefghijklmnopqrstuvwxyz'

def solve(data_input):
    result = {}
    for (idx,d) in enumerate(data_input):

        foundReact = True
        current = 0
        while(current < len(d)-1):

            if(d[current].upper() == d[current+1].upper() and d[current] != d[current+1]):
                d = d[:current] + d[current+2:]
                # print(d)
                current -= 6
                if current < 0:
                    current = 0
            current += 1
            #if current % 1000 == 0:
            #    print('Iteration %d: %s' % (current, d[:100]))

        print('Length %s: %d' % (abc[idx], len(d)))
        result[abc[idx]] = len(d)

    result = sort_dic_by_values(result)
    print('Winning Letter:', result[0])
    print('-'*80)

# Part 1
print('Part 1')
solve([data])

# --------------------------
# Part 2
print('Part 2')
data2 = []
for c in abc:
    data2.append(data.replace(c,'', len(data)).replace(c.upper(),'', len(data)))
solve(data2)
