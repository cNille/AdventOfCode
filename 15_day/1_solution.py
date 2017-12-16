import time
start_time = time.time()

# Puzzle input:
#   Generator A starts with 873
#   Generator B starts with 583

# A uses 16807
# b uses 48271

# divider 2147483647

start_a = 873
start_b = 583

fact_a = 16807
fact_b = 48271

div = 2147483647

test_a = 65
test_b = 8921

def calc(prev, fact, div):
    return (prev * fact) % div

curr_a = start_a
curr_b = start_b

num_of_bits = 32 

matches = 0


for i in range(40000000):
    curr_a = calc(curr_a, fact_a, div)
    curr_b = calc(curr_b, fact_b, div)

    bin_a = bin(curr_a)[2:].zfill(num_of_bits)
    bin_b = bin(curr_b)[2:].zfill(num_of_bits)

    if bin_a[-16:] == bin_b[-16:]:
        matches += 1

    if i % 100000 == 0:
        print(i, bin_a, '\t', bin_b) 

print('matches:',matches)
    
print("--- %s seconds ---" % (time.time() - start_time))

