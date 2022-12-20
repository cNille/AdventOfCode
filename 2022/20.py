print(chr(27)+'[2j')
print('\033c')
f = open('20.test', 'r')
#f = open('20.input', 'r')
lines = [x.strip() for x in f.readlines()]
print("Day 20")
from dataclasses import dataclass
from typing import Any

@dataclass
class Nbr:
    value: int
    original_index: int
    prev: Any
    next: Any

    def __str__(self) -> str:
        return str(self.original_index) + ":" +  str(self.value)

lines = [int(x) for x in lines]
def init(lines, mult): 
    lines = [x * mult for x in lines]
    first = lines[0]
    start = Nbr(int(first), 0, None, None)
    curr = start
    for i, l in enumerate(lines[1:]):
        value = int(l)
        new_nbr = Nbr(value, i+1, curr, start)
        curr.next = new_nbr
        start.prev = new_nbr
        curr = new_nbr
    return start, curr

def row(lines, start):
    curr = start
    row = [] 
    for _ in range(len(lines)):
        row.append(curr.value)
        curr = curr.next
    return row

def mix(lines, start):
    L = len(lines)
    for x in range(len(lines)):
        curr = start
        while x != curr.original_index:
            curr = curr.next

        value = curr.value 
        if value > 0:
            times = value % (L-1)  if value > L else value
            if times == 0:
                continue
            curr.next.prev, curr.prev.next = curr.prev, curr.next
            after = curr
            if curr == start:
                start = curr.next
            for _ in range(times):
                after = after.next
            curr.prev, curr.next = after, after.next
            after.next.prev = curr
            after.next = curr
        elif value < 0:
            times = abs(value) % (L-1)  if abs(value) > L else abs(value)
            if times == 0:
                continue
            curr.next.prev, curr.prev.next = curr.prev, curr.next
            before = curr
            if curr == start:
                start = curr.next
            for _ in range(times):
                before = before.prev
            curr.next, curr.prev = before, before.prev
            before.prev.next = curr
            before.prev = curr
    return lines, start

def get_groove(numbers):
    groove_numbers = [
        numbers[(1000+numbers.index(0)) % len(numbers)],
        numbers[(2000+numbers.index(0)) % len(numbers)],
        numbers[(3000+numbers.index(0)) % len(numbers)],
    ]
    return sum(groove_numbers)

# Part 1
start, curr = init(lines, 1)
lines, start =  mix(lines, start)
numbers = row(lines,start)
groove_numbers = [
    numbers[(1000+numbers.index(0)) % len(numbers)],
    numbers[(2000+numbers.index(0)) % len(numbers)],
    numbers[(3000+numbers.index(0)) % len(numbers)],
]
print("Solution part 1:", get_groove(numbers))

# Part 2
start, curr = init(lines, 811589153) 
curr = start
for i in range(10):
    lines, start =  mix(lines, start)
r = row(lines, start)
numbers = row(lines,start)
print("Solution part 2:", get_groove(numbers))
