print(chr(27)+'[2j')
print('\033c', end='')

puzzle_input = 'yjdafjpo'  # My input
#puzzle_input = 'abc' # Test input

from functools import cache
import hashlib
import re

def hash_fn(salt, index):
    return hashlib.md5((salt+str(index)).encode('utf-8')).hexdigest()

@cache
def stretched_hash(salt, index):
    h = hashlib.md5((salt+str(index)).encode('utf-8')).hexdigest()
    for _ in range(2016):
        h = hashlib.md5(h.encode('utf-8')).hexdigest()
    return h

def triple_finder(hash_str):
    triples = re.findall(r'(.)\1\1', hash_str)
    if triples:
        return triples[0][0]
    return None

def five_times(hash_str, char):
    return char*5 in hash_str

def solve(fn):
    index = 0
    keys = []
    while True:
        if len(keys) == 64:
            return keys[-1][0]
        res = fn(puzzle_input, index)
        triple = triple_finder(res)
        if triple:
            for i in range(index+1, index+1001):
                if five_times(fn(puzzle_input, i), triple):
                    print("Found quintuple", index, len(keys))
                    keys.append((index, res))
                    break
        index += 1

print("Solution to part 1: %d" % solve(hash_fn))
print("Solution to part 2: %d" % solve(stretched_hash))
