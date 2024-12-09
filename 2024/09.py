print(chr(27)+'[2j')
print('\033c')
f = open('09.test', 'r')
#f = open('09.input', 'r')
lines = [x.strip() for x in f.readlines()]
diskmap = lines[0]

def checksum(blocks, ids):
    checksum = 0
    for i, v in enumerate(blocks):
        if v == '.':
            continue
        c = i * ids[i]
        checksum += c
    return checksum


def create_blocks(diskmap):
    blocks = ''
    ID = -1 
    ids = {}
    for i in range(0, len(diskmap), 2):
        ID += 1
        for _ in range(int(diskmap[i])):
            id_digit = str(ID)
            id_digit = id_digit[len(id_digit)-1] 
            ids[len(blocks)] = ID
            blocks += id_digit 
    
        if (i+1) < len(diskmap):
            for _ in range(int(diskmap[i+1])):
                blocks += '.' 
    return ids, blocks

def defrag1(blocks, ids):
    blocks = list(blocks)
    left = 0
    right = len(blocks) - 1
    while left != right:
        while blocks[right] == '.' and left != right:
            right -= 1
        while blocks[left] != '.' and left != right:
            left += 1

        ids[left] = ids[right]
        if left != right:
            del ids[right]
        blocks[right], blocks[left] = blocks[left], blocks[right]
    return blocks

def defrag2(blocks, ids):
    files = {}
    curr_id = 0
    for i in ids:
        curr_id = max(ids[i], curr_id)
        if ids[i] not in files:
            files[ids[i]] = []
        files[ids[i]].append(i)

    blocks = list(blocks)
    while curr_id >= 0:
        print('ID', curr_id)
        size = len(files[curr_id])
        pos = files[curr_id][0]

        left = 0
        while left < pos:
            while blocks[left] != '.' and left < pos:
                left += 1
            right = left
            while blocks[right] == '.' and right < pos:
                right += 1
            empty_size = right - left 

            if size <= empty_size:
                for i, v in enumerate(files[curr_id]):
                    ids[left+i] = ids[v]
                    blocks[left+i] = blocks[v]
                    blocks[v] = '.'

            left += 1


        curr_id -= 1



    return blocks

# Part 1
ids, blocks = create_blocks(diskmap)
blocks = defrag1(blocks, ids)
print('Solution part1:', checksum(blocks, ids))

# Part 2
ids, blocks = create_blocks(diskmap)
blocks = defrag2(blocks, ids)
print('Solution part2:', checksum(blocks, ids))
