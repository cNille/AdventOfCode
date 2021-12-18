print(chr(27)+'[2j')
print('\033c')
from itertools import permutations
import json
import math
# f = open('18.input', 'r')
f = open('18.test', 'r')
data = [x.strip() for x in f.readlines()]

def add(neighbour, pos, value):
    if isinstance(neighbour, list):
        neighbour[pos] = add(neighbour[pos], pos, value)
        return neighbour
    else:
        return value + neighbour

def explode_path(numbers, level=0):
    if level == 4:
        return None, numbers[0], numbers[1]
    for i, x in enumerate(numbers):
        if isinstance(x, list):
            explotion = explode_path(x, level + 1)
            if explotion == None:
                continue
            new_numbers, left,right = explotion
            if new_numbers == None:
                numbers[i] = 0
            if left == 0 and right == 0:
                return numbers, left, right

            left_neighbour = i - 1
            if left_neighbour >= 0 and left > 0:
                numbers[left_neighbour] = add(numbers[left_neighbour], -1, left)
                left = 0
            right_neighbour = i + 1
            if right_neighbour < len(numbers) and right > 0:
                numbers[right_neighbour] = add(numbers[right_neighbour], 0, right)
                right = 0
            return numbers, left, right
    return None

def split(numbers, level = 0):
    for i,x in enumerate(numbers):
        if isinstance(x, list):
            splitted = split(x, level + 1)
            if splitted != None:
                numbers[i] = splitted
                return numbers
        else:
            if x > 9:
                half = float(x) / 2.0
                numbers[i] = [math.floor(half), math.ceil(half)]
                return numbers
    return None

def action(numbers,level=0):
    is_finished = False
    while not is_finished:
        explotion = explode_path(numbers)
        if explotion != None:
            numbers = explotion[0]
            continue
        splitted = split(numbers)
        if splitted != None:
            numbers = splitted 
            continue
        is_finished = True
    return numbers

def magnitude(numbers):
    if isinstance(numbers, int):
        return numbers 
    else:
        return 3 * magnitude(numbers[0]) + 2 * magnitude(numbers[1])

summed = eval(data[0])
for i, line in enumerate(data[1:]):
    line = eval(line)
    summed = action([summed, line])
print('Solution part 1: %d' % magnitude(summed))

max_mag = 0
for i,j in permutations(range(len(data)), 2):
    a = eval(data[i])
    b = eval(data[j])
    summed = action([a,b])
    mag = magnitude(summed)
    if mag > max_mag:
        max_mag = mag
print('Solution part 2: %d' % max_mag)
