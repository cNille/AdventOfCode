print(chr(27)+'[2j')
print('\033c')
from functools import cache
import math
f = open('24.test', 'r')
f = open('24.input', 'r')
data = [x.strip() for x in f.readlines()]

def round(value):
    return math.floor(value) if value > 0 else math.ceil(value)

values = [
    (1,  11, 15),
    (1,  12, 2),
    (26, -3, 15),
    (1,  10, 14),
    (26, -9, 2),
    (1,  10, 15),
    (26, -7, 1),
    (26,-11, 15),
    (26, -4, 15),
    (1,  14, 12),
    (1,  11, 2),
    (26, -8, 13),
    (26,-10, 13),
]

@cache
def calc(registers, w, A, B, C):
    registers = list(registers)
    registers[3] = w
    registers[0] = 1 if ((registers[2] % 26) + B) != w else 0
    registers[2] = round(registers[2] / A)
    registers[2] = registers[2] * ((25 * registers[0]) + 1) 
    registers[1] = (w + C) * registers[0]
    registers[2] = registers[2] + registers[1]
    return tuple(registers)

digit_calc = [
    (1,  12, 7),  # ✅
    (1,  11, 15),# ✅
    (1,  12, 2),# ✅
    (26, -3, 15),# ✅
    (1,  10, 14),# ✅
    (26, -9, 2),# ✅
    (1,  10, 15),# ✅
    (26, -7, 1),# ✅
    (26,-11, 15),# ✅
    (26, -4, 15),# ✅
    (1,  14, 12),
    (1,  11, 2),
    (26, -8, 13),
    (26,-10, 13),
]
# x = 0 if ((z % 26) + B) == w else 1 
# z = ( (z / A) * ( 25 * x + 1 ) ) + x * (w + C) 

# A = 1, B = 14, C = 12
# x = 0 if ((z % 26) + B) == w else 1 
# z = ( (z / A) * ( 25 * x + 1 ) ) + x * (w + C) 

# 1:  (w1+7) 
# 2:  (w1+7)*26 + (w2+15)
# 3:  (w1+7)*26*26 + (w2+15)*26 + (w3+2)
# 4:  (w1+7)*26 + (w2+15)
# 5:  (w1+7)*26*26 + (w2+15)*26 + (w5+14)
# 6:  (w1+7)*26 + (w2+15)
# 7:  (w1+7)*26*26 + (w2+15)*26 + (w7+15)
# 8:  (w1+7)*26 + (w2+15) 
# 9:  (w1+7)
# 10: 0 
# 11: (w11+12)
# 12: (w11+12)*26 + (w12+2)
# 13: (w12+2)

# w10 = w1 + 3
# w9 = w2 + 4
# w4 = w3 - 1
# w6 = w5 + 5 
# w8 = w7 + 8
# w13 = w12 - 6

# Highest: 65984919997939 
# Lowest:  11211619541713  

def monad(nbr):
    # Input 1
    z = 0
    w = int(nbr[0])
    registers = (0, 0, z, int(w))
    for idx in range(len(nbr)):
        w = int(nbr[0])
        registers = (0, 0, z, int(w))
        a,b,c = digit_calc[idx]
        registers = calc(registers, w, a, b, c)
        z = registers[2]
        nbr = nbr[1:]

    is_valid = z == 0
    return is_valid, registers

# I was close enough so i could just iterate from my guesses
is_valid = False
nbr = 65984919997939
nbr = 11211619541713 
count = 0
while not is_valid:
    s = str(nbr)
    if '0' in s:
        nbr += 1
        continue
    count += 1
    is_valid, regs = monad(s) 
    if is_valid:
        print('Found %s, zvalue: %d' % (s, regs[2]))
        break

    if count % 100 == 0:
        print('Checking %s' % s, regs)
    nbr += 1

print('Number %d is valid' % (nbr))

# Too low
# 7091892073
