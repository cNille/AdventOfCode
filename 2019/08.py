from collections import Counter
f = open('08.input', 'r')
content = [x.strip() for x in f.readlines()][0]

w = 25 
h = 6
imgsize = w * h

def chunk(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
    
# Part 1
chunks = chunk(content, imgsize)
counters = [Counter(x) for x in chunks]
counters = [(x['0'], x['1'] * x['2']) for x in counters ]
counters = sorted(counters, key=lambda x : x[0])
print("Part 1 result: %d" % counters[0][1])

# Part 2
img = '2'*imgsize
for c in chunks:
    img = [x if x != '2' else c[i] for i,x in enumerate(img)]
img = "".join(img)

print('Part 2 solution:')
for r in chunk(img, w):
    print(r.replace('0', ' ').replace('1','@'))
