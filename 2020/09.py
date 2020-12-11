numbers = [int(x.strip()) for x in open('09.input', 'r').readlines() if x != '']

def part1slow(numbers):
    # Iterate all numbers
    for i, n in enumerate(numbers):              
        # Skip "preamble"
        if i < 25:
            continue

        # Iterate all 25 previous numbers
        is_valid = False
        for j in range(i-25,i):
            # Try out all combinations to sum to n 
            for k in range(i-25, i):
                if j != k:
                    if numbers[j] + numbers[k] == n:
                        is_valid = True
                        break
                if is_valid:
                    break
            if is_valid:
                break

        # If is not valid, then we found our answer
        if not is_valid:                    
            return n 

def part1list(numbers):
    q = numbers[:25] 

    for n in numbers[25:]:              

        def valid(n):
            rests = set()
            for x in q:
                if n - x in rests:
                    return True
                else: 
                    rests.add(x)
            return False
        rests = set([n - x for x in q])
        is_valid = len(rests.intersection(q)) 
        #is_valid = len([x for x in rests if x in q]) > 0


        if not is_valid:                    
            return n 
        else:
            q.append(n)                 
            q.pop(0)



from collections import deque
def valid(arr, n):
    differences = set()
    for x in arr:
        if n - x in differences:
            return True
        differences.add(x)
    return False

def part1(numbers):
    window = deque(numbers[:25], maxlen=25)
    for n in numbers[25:]:
        if not valid(window, n):
            return n
        window.append(n)

numbers = [int(x.strip()) for x in open('09.input', 'r').readlines() if x != '']
from collections import deque
def part1(numbers):
    q = deque(numbers[:25], maxlen=25)

    for n in numbers[25:]:              
        is_valid, rests = False, set()
        for x in q:
            if n - x in rests:
                is_valid = True
                break
            rests.add(x)

        if not is_valid:                    
            return n 
        q.append(n)                 

def part2(numbers, needle):
    window, window_sum = deque(), 0

    for n in numbers:
        window.append(n)                     
        window_sum += n

        while window_sum > needle:
            window_sum -= window.popleft()                  
        if window_sum == needle:                 
            return max(window) + min(window)      

solution1 = part1(numbers)
print "Solution part1: %d" % solution1
print "Solution part2: %d" % part2(numbers, solution1)

    numbers = [int(x.strip()) for x in open('09.input', 'r').readlines() if x != '']
    from collections import deque
    window = deque(numbers[:25], maxlen=25)

    for n in numbers[25:]:              
        is_valid, differences = False, set()
        for x in window:
            if x in differences:
                is_valid = True
            differences.add(n - x)

        if not is_valid:                    
            invalid = n
            break
        window.append(n)                 
    print "Solution part1: %d" % invalid 

    window, window_sum = deque(), 0
    for n in numbers:
        window.append(n)                     
        window_sum += n

        while window_sum > invalid:
            window_sum -= window.popleft()                  
        if window_sum == invalid:                 
            print "Solution part2: %d" % (max(window) + min(window))
            break
