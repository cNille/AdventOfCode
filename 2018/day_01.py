import sys

def success_larm():
    for i in range(10):
        sys.stdout.write('\a')
        sys.stdout.flush()

f = open('day_01_input.txt', 'r')
content = [x.strip() for x in f.readlines()]
content = [int(x) for x in content]

s = 0
d = {}

while(True):
    print('Trying...')
    for x in content:
        s = s + x
        if s not in d:
            d[s] = 1
        else:
            print('Success', s)
            success_larm();
            exit()


