import re

moves = open('my.input').read()[:-1].split(',')
letters = list('abcdefghijklmnop')

def spin(x):
    global letters
    letters = letters[-x:] + letters[:-x] 
def exchange(a,b):
    (letters[a], letters[b]) = (letters[b], letters[a])

memory = []
startpos = 0
endpos = 0
for i in range(1000):
    for m in moves:
        for s in re.findall(r's(\d+)', m):
            spin(int(s))
        for e in re.findall(r'x(\d+)\/(\d+)', m):
            exchange(int(e[0]),int(e[1]))
        for p in re.findall(r'p(\D+)\/(\D+)', m):
            exchange(letters.index(p[0]), letters.index(p[0]))
    
    positions = ''.join(letters)
    if positions in memory:
        endpos = i
        startpos = memory.index(positions)
        break
        
    memory.append(positions)    
    print(i, '\t', positions)

res_idx = (1000000000 - 1) % (endpos - startpos)
res = memory[res_idx]
print('\nResult:', res)

