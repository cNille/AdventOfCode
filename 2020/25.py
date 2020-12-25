lines = [x.strip() for x in open('25.input', 'r').readlines()]

def loop(value, subject_number):
    return (value * subject_number) % 20201227

def find(key):
    value = 1
    loop_size = 1
    while True:
        value = loop(value, 7)
        if value == key:
            return loop_size 
        loop_size += 1

def encrypt(key, loop_size):
    value = 1
    for i in range(loop_size):
        value = loop(value, key)
    return value

assert find(5764801) == 8
assert find(17807724) == 11 
assert encrypt(5764801, 11) == 14897079

A, B = map(int, lines)
A_loop_size = find(A) 
B_loop_size = find(B) 
print "Solution: %d" % encrypt(A, B_loop_size)
