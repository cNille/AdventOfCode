import hashlib

data = "ckczppom"
# Part 1:

nbr = 1
while True:
    h = hashlib.md5(("%s%d" % (data, nbr)).encode())
    h = h.hexdigest()
    if h[:5] == "00000":
        break
    if nbr % 100000 == 0:
        print("Iteration %d" % nbr)
    nbr += 1

print("Solution part 1: %d" % nbr)

# incorrect: ckczppom117946

# Part 2:

nbr = 386700000

while True:
    h = hashlib.md5(("%s%d" % (data, nbr)).encode())
    h = h.hexdigest()
    if h[:5] == "000000":
        break
    if nbr % 100000 == 0:
        print("Iteration %d" % nbr)
    nbr += 1

print("Solution part 1: %d" % nbr)
