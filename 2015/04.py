import hashlib
data = "ckczppom"

# Part 1:
nbr = 1
while True:
    h = hashlib.md5(("%s%d" % (data, nbr)).encode())
    h = h.hexdigest()
    if h[:5] == "00000":
        break
    nbr += 1
print("Solution part 1: %d" % nbr)

# Part 2:
nbr = 503000000 
nbr = 0
while True:
    h = hashlib.md5(("%s%d" % (data, nbr)).encode()).hexdigest()
    if h[:6] == "000000":
        break
    nbr += 1

print("Solution part 2: %d" % nbr)
