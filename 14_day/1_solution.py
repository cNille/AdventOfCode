from collections import Counter
from functools import reduce

puzzle_input = 'jzgqcdpd'

def reverse(arr, start, steps):
    arr_length = len(arr)
    for i in range(0, int(steps / 2) ):
        pos1 = (start + i) % arr_length
        pos2 = (start + steps - 1 - i) % arr_length
        [arr[pos1], arr[pos2]] = [arr[pos2], arr[pos1]]
    return arr    


def knot_hash(input_word):
    input_word = [ord(c) for c in input_word] + [17, 31, 73, 47, 23]
    skip_size = 0
    current_position = 0
    arr = list(range(0,256))
    rounds = list(range(64))

    for r in rounds:
        for l in input_word:
            l = int(l)
            arr = reverse(arr, current_position, l)
            current_position += l + skip_size 
            skip_size += 1

    n = 16
    chunks = [arr[i:i + n] for i in range(0, len(arr), n)]
    bits = []
    for chunk in chunks:
        bits.append(reduce(lambda i, j: i ^ j, chunk))

    hash_str = [hex(x)[2:] for x in bits]
    for i in range(len(hash_str)):
        if len(hash_str[i]) < 2:
            hash_str[i] = '0' + hash_str[i]

    result = ''.join(hash_str)
    return result


def hex_to_bin(h):
    scale = 16
    num_of_bits = 128 
    b = bin(int(h, scale))[2:].zfill(num_of_bits)
    return b

total = 0
for i in range(128):
    curr = puzzle_input + '-' + str(i)
    hash_str = knot_hash(curr)
    b = hex_to_bin(hash_str)

    used = len([s for s in list(b) if int(s) > 0])
    total += used

    
print('Total:',total)    

