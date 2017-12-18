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

a_list = []
b_list = []

i = 0
while min(len(a_list), len(b_list)) < 5000001:
    curr_a = calc(curr_a, fact_a, div)
    curr_b = calc(curr_b, fact_b, div)

    if curr_a % 4 == 0:
        a_list.append(curr_a)
    if curr_b % 8 == 0:
        b_list.append(curr_b)

    if i % 100000 == 0:
        print(i, curr_a, '\t', curr_b) 
    i+=1    

print(len(a_list))
print(len(b_list))
print(a_list[:5])
print(b_list[:5])

for i in range(min(len(a_list),len(b_list))):
    a = a_list[i]
    b = b_list[i]
    bin_a = bin(a)[2:].zfill(num_of_bits)
    bin_b = bin(b)[2:].zfill(num_of_bits)

    if bin_a[-16:] == bin_b[-16:]:
        print(i, bin_a, '\t', bin_b) 
        matches += 1


print('matches:',matches)
    
print("--- %s seconds ---" % (time.time() - start_time))

