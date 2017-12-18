from collections import Counter

lengths = open('my.input').read().split()[0].split(',')


def reverse(arr, start, steps):
    arr_length = len(arr)
    for i in range(0, int(steps / 2) ):
        pos1 = (start + i) % arr_length
        pos2 = (start + steps - 1 - i) % arr_length
        [arr[pos1], arr[pos2]] = [arr[pos2], arr[pos1]]
    return arr    

print(lengths)

skip_size = 0
current_position = 0
arr = list(range(0,256))

for l in lengths:
    l = int(l)

    arr = reverse(arr, current_position, l)
    current_position += l + skip_size 
    skip_size += 1

    print(arr) 
    
