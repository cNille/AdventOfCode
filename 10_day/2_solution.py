from collections import Counter
from functools import reduce

lengths = open('my.input').read().split()[0]
lengths = [ord(c) for c in lengths] + [17, 31, 73, 47, 23]

def reverse(arr, start, steps):
    arr_length = len(arr)
    for i in range(0, int(steps / 2) ):
        pos1 = (start + i) % arr_length
        pos2 = (start + steps - 1 - i) % arr_length
        [arr[pos1], arr[pos2]] = [arr[pos2], arr[pos1]]
    return arr    


skip_size = 0
current_position = 0
arr = list(range(0,256))
rounds = list(range(64))

for r in rounds:
    for l in lengths:
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

print(result)
