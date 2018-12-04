import datetime
import operator

# First bash to sort
# cat day_04_input.txt | sort > day_04_sorted.txt

f = open('day_04_sorted.txt','r')
data = [x.strip() for x in f.readlines()]

# For diffing datetimes in seconds
epoch = datetime.datetime.utcfromtimestamp(0)
def unix_time_millis(dt):
    return (dt - epoch).total_seconds()

sleep = {}
curr = -1
guards = set()
for line in data:
    if 'begins' in line:
        curr = line.split('#')[1].split(' ')[0]
        guards.add(curr)
        if curr not in sleep:
            sleep[curr] = []
    else:
        sleep[curr].append(line)

score = {}
minutes = {}
for g in guards:
    diff = 0
    times = sleep[g]
    if g not in minutes:
        l = []
        for i in range(60):
            l.append(0)
        minutes[g] = l

    for i in range(0,len(times)-1,2):
        d1 = times[i + 0].split(']')[0].split('[')[1]
        d2 = times[i + 1].split(']')[0].split('[')[1]
        date1 = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M')
        date2 = datetime.datetime.strptime(d2, '%Y-%m-%d %H:%M')
        diff = diff + unix_time_millis(date2) - 60 - unix_time_millis(date1)

        d2 = date2.minute
        if date2.minute <= date1.minute:
            d2 +=60

        hours = ((date2.hour - date1.hour) + 24) % 24

        for m in range(date1.minute, d2):
            minutes[g][m % 60] += 1

    score[g] = diff / 60

sorted_score = sorted(score.items(), key=operator.itemgetter(1))
max_guard = sorted_score[-1]

max_min = minutes[max_guard[0]]

m = -1
mm = -1
for i in range(len(max_min)):
    if max_min[i] > m:
        m = max_min[i]
        mm = i

print('Max minute:', mm)
print('inute:', max_min[mm])
print('Result', mm * int(max_guard[0]))

# Part 2

max_min = -1
max_g = -1
max_i = -1
for g in minutes:
    for idx,m in enumerate(minutes[g]):
        if max_min < m:
            max_min = m
            max_g = g
            max_i = idx

print('-'*80)
print(max_i, max_g)
print('result2:', max_i * int(max_g))
