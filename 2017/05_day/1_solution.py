instr = list(map( lambda x: int(x[:-1]), open('my.input').readlines())) 

count = 0
idx = 0
while idx >= 0 and idx < len(instr):
    temp = idx
    idx += instr[idx]

    instr[temp] +=1
    count += 1

print(count)
