import datetime
import operator
import re

# For diffing datetimes in seconds
epoch = datetime.datetime.utcfromtimestamp(0)
def unix_time_millis(dt):
    return (dt - epoch).total_seconds()
def date_from_format(d, f):
    return datetime.datetime.strptime(d, f)
def datetime_str(d):
    return date_from_format(d, '%Y-%m-%d %H:%M')

# Sorting
def sort_dic_by_keys(d):
    return sorted(d.items(), key=operator.itemgetter(0))
def sort_dic_by_values(d):
    return sorted(d.items(), key=operator.itemgetter(1))

# -----------------------------------------------------------------------------

# Import data
data = [x.strip() for x in open('day_05_input.txt','r').readlines()]
data = data[0]

data2 = []
abc = 'abcdefghijklmnopqrstuvwxyz'
for c in abc:
    data2.append(data.replace(c,'', len(data)).replace(c.upper(),'', len(data)))


result = {}
for (idx,d) in enumerate(data2):

    foundReact = True
    c = 0
    while(foundReact):

        foundReact = False
        for i in range(len(d)-1):

            if(d[i].upper() == d[i+1].upper() and d[i] != d[i+1]):
                d = d[:i] + d[i+2:]
                # print(d)

                foundReact = True
                break
        c += 1
        if c % 1000 == 0:
            print('Iteration %d: %s' % (c, d[:100]))

    print('Length %s: %d' % (abc[idx], len(d)))
    result[abc[idx]] = len(d)

sort_dic_by_values(result)
print('-'*80)
print(result)
