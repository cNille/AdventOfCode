print(chr(27)+'[2j')
print('\033c')
from itertools import permutations
import json
import math
f = open('24.test', 'r')
f = open('24.input', 'r')
data = [x.strip() for x in f.readlines()]

def get(registers, a):
    if a in registers:
        return registers[a]
    return int(a)

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

def calc(registers, w, v1, v2, v3):
    registers['w'] = w
    registers['x'] = 1 if ((registers['z'] % 26) + v2) != w else 0
    registers['z'] = round(registers['z'] / v1)
    registers['z'] = registers['z'] * ((25 * registers['x']) + 1) 
    registers['y'] = (w + v3) * registers['x']
    registers['z'] = registers['z'] + registers['y']
    return registers

valid_zeros = [0]
for i in range(len(values)):
    print('-- Testing %d' % i)
    new_zeros = []
    for digit in range(1,10):
        for z in range(10000):
            a,b,c = values[(i + 1) * -1]
            registers = { "x": 0, "y": 0, "z": z, "w": 0 }
            new_reg = calc(registers, digit, a, b, c)
            if new_reg['z'] in valid_zeros:
                print("Digit %d , z %d : %d" % (digit, z, new_reg['z']))
                new_zeros.append(z)
    valid_zeros = new_zeros

def monad(i):
    copy_i = [ch for ch in i]
    i = [ch for ch in i]
    registers = {
        "x": 0,
        "y": 0,
        "z": 0,
        "w": 0,
    }
    verbose = False

    # Input 1
    w1 = int(i.pop(0))
    registers['w'] = int(w1)
    registers['x'] = 1
    registers['y'] = 0
    registers['z'] = registers['w'] + 7
    verbose and print('Registers 1:', registers)

    registers = calc(registers, int(i.pop(0)), 1,  11, 15)
    verbose and print('R 2:', registers)
    registers = calc(registers, int(i.pop(0)), 1,  12, 2)
    verbose and print('R 3:', registers)
    registers = calc(registers, int(i.pop(0)), 26, -3, 15)
    verbose and print('R 4:', registers)
    registers = calc(registers, int(i.pop(0)), 1,  10, 14)
    verbose and print('R 5:', registers)
    registers = calc(registers, int(i.pop(0)), 26, -9, 2)
    verbose and print('R 6:', registers)
    registers = calc(registers, int(i.pop(0)), 1,  10, 15)
    verbose and print('Registers 7:', registers)
    registers = calc(registers, int(i.pop(0)), 26, -7, 1)
    verbose and print('Registers 8:', registers)
    registers = calc(registers, int(i.pop(0)), 26,-11, 15)
    verbose and print('Registers 9:', registers)
    registers = calc(registers, int(i.pop(0)), 26, -4, 15)
    verbose and print('Registers 10:', registers)
    registers = calc(registers, int(i.pop(0)), 1,  14, 12)
    verbose and print('Registers 11:', registers)
    registers = calc(registers, int(i.pop(0)), 1,  11, 2)
    verbose and print('Registers 12:', registers)
    registers = calc(registers, int(i.pop(0)), 26, -8, 13)
    verbose and print('Registers 13:', registers)
    registers = calc(registers, int(i.pop(0)), 26,-10, 13)
    verbose and print('Registers 14:', registers)
    return (is_valid, registers)

is_valid = False
nbr = 99978825281377
count = 0

# s = '12345678912345'
# is_valid, regs = monad(s)
# print('Checking %s, zvalue: %d' % (s, regs['z']))
# # s = '9'
# # for i in [9,8,7,6,5,4,3,2,1]:
# #     s = str(i) + '123127543'
# #     is_valid, regs = monad(s)
# #     print('Checking %s, zvalue: %d' % (s, regs['z']))
# exit()

while not is_valid:
    nbr -= 1
    s = str(nbr)
    if '0' in s:
        continue
    count += 1
    is_valid, regs = monad(s) 

    if count % 100000 == 0:
        print('Checking %s' % s, regs)

print('Number %d is valid' % (nbr))
