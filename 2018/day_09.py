# Import data
data = [x.strip() for x in open('day_09_input.txt','r').readlines()]
data = data[0]
data = data.split()

elfs_nbr = int(data[0])
marbles = int(data[6])
print('Part 1: Number of elfs: %d, number of marbles: %d' % (elfs_nbr, marbles))

elfs = []
for e in range(elfs_nbr):
    elfs.append(0)

# Part 1
def part1():
    circle = []
    circle.append(0)
    curr = 0

    for m in range(1,marbles):
        if m % 23 == 0:
            # Get index of 7 steps back
            curr = (curr - 7 + len(circle)) % len(circle)

            # Assign elf points from next marble and the marble in current pos.
            elf_idx = (m-1) % len(elfs)
            elfs[elf_idx] += m + circle.pop(curr)
        else:
            i = ((curr + 1) % len(circle)) + 1
            circle.insert(i,m)
            curr = i
    print('Part 1 Result: %d' % max(elfs))
part1()
exit()

# Part 2
# ==============================================================================
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

curr = Node(0)
curr.prev = curr
curr.next = curr

marbles = marbles * 100
print('Part 2: Number of elfs: %d, number of marbles: %d' % (elfs_nbr, marbles))

for m in range(1, marbles):
    if m % 23 == 0:
        # Move back 7 steps
        for i in range(7):
            curr = curr.prev

        # Assign elf points
        e = (m-1) % len(elfs)
        elfs[e] += (m + curr.val)

        # Remove current node
        n = curr.next
        curr = curr.prev
        curr.next = n

        # Update current node
        curr = curr.next
    else:
        # Move one step
        curr = curr.next

        # Init new node
        n = Node(m)
        n.next = curr.next
        n.prev = curr

        # Append to list
        curr.next.prev = n
        curr.next = n

        # Set new node as current
        curr = n

print('Part 2 Result: %d' % max(elfs))
