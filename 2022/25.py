print(chr(27)+'[2j')
print('\033c')
f = open('25.test', 'r')
f = open('25.input', 'r')
lines = [x.strip() for x in f.readlines()]
print("Day 25")

tot = 0
for l in lines:
    num = 0
    for i,n in enumerate(l):
        p = pow(5,len(l)-1-i)
        if n == '=':
            n = -2
        elif n == '-':
            n = -1
        else:
            n = int(n)
        num += n*p

    tot += num

p = 0
num = []
while True:
    x = pow(5,p)
    if tot - x < x*2.5:
        num = [1] if tot / x < 1.5 else [2]
        tot -= x * num[0]
        for i in range(p):
            x = pow(5,p-1-i)
            n = round(tot / x)
            num += [n]
            tot -= n*x
        break
    p += 1 

res = ""
for n in num:
    if n == -2:
        res += "="
    if n == -1:
        res += "-"
    if n == 0:
        res += "0"
    if n == 1:
        res += "1"
    if n == 2:
        res += "2"

print("Solution part 1:", res)
