import re

moves = open('my.input').read()[:-1].split(',')
letters = list('abcdefghijklmnop')

def spin(x):
    global letters
    letters = letters[-x:] + letters[:-x] 
def exchange(a,b):
    (letters[a], letters[b]) = (letters[b], letters[a])

for m in moves:
    for s in re.findall(r's(\d+)', m):
        spin(int(s))
    for e in re.findall(r'x(\d+)\/(\d+)', m):
        exchange(int(e[0]),int(e[1]))
    for p in re.findall(r'p(\D+)\/(\D+)', m):
        exchange(letters.index(p[0]), letters.index(p[0]))

print('Result:',''.join(letters))
