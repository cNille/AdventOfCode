numbers = [int(x.strip()) for x in open('09.input', 'r').readlines() if x != '']

from collections import deque
def part1(numbers):
    q = deque(numbers[:25])

    for n in numbers[25:]:
        if len(q) > 25:
            q.popleft()

        def valid(n):
            rests = set()
            for x in q:
                if n - x in rests:
                    return True
                else: 
                    rests.add(x)
            return False

        if valid(n):
            q.append(n)
        else:
            return n 

def part2(numbers, needle):
    q = deque()
    for i, n in enumerate(numbers):
        q.append(n)
        s = sum(q)

        while s > needle:
            q.popleft()
            s = sum(q)
        if s == needle:
            return max(q) + min(q)
        

solution1 = part1(numbers)
print "Solution part1: %d" % solution1
print "Solution part2: %d" % part2(numbers, solution1)
