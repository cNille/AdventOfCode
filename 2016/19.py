print(chr(27)+'[2j')
print('\033c', end='')
print("Day 19")
puzzle_input = 3014387 
# test
#puzzle_input = 5
#puzzle_input = 9 
start_elfs = puzzle_input

class Elf:
    def __init__(self, id: int, prev: 'Elf' = None, nxt: 'Elf' = None) -> None:
        self.id = id
        self.prev = prev
        self.nxt = nxt
        self.value = 1

first_elf = Elf(1, None, None)
curr_elf = first_elf

for i in range(puzzle_input - 1):
    new_elf = Elf(i + 2, curr_elf, None)
    curr_elf.nxt = new_elf
    curr_elf = new_elf

curr_elf.nxt = first_elf
first_elf.prev = curr_elf
curr_elf = first_elf

# part1
while True: 
    if curr_elf == None or curr_elf.nxt == None:
        print("Error, None:", curr_elf)
        break
    if curr_elf.id == curr_elf.nxt.id:
        print("Part 1: Elf", curr_elf.id, "took all")
        break

    new_presents = curr_elf.value + curr_elf.nxt.value
    took_from = curr_elf.nxt.id
    #print("Elf", curr_elf.id, "had", curr_elf.value, "and now", new_presents, "presents. Took from elf", took_from)
    curr_elf.value = new_presents
    curr_elf.nxt.value = 0
    curr_elf.nxt = curr_elf.nxt.nxt

    curr_elf = curr_elf.nxt
  

# part2
first_elf = Elf(1, None, None)
curr_elf = first_elf

for i in range(puzzle_input - 1):
    new_elf = Elf(i + 2, curr_elf, None)
    curr_elf.nxt = new_elf
    curr_elf = new_elf

curr_elf.nxt = first_elf
first_elf.prev = curr_elf
curr_elf = first_elf

halfway = int((puzzle_input + 1) / 2)
victim = curr_elf.nxt
for i in range(halfway - 2):
    if victim != None:
        victim = victim.nxt
while True: 
    if curr_elf.id == victim.id:
        print("Part 2: Elf", curr_elf.id, "took all")
        break

    new_value = curr_elf.value + victim.value
    #print("Elf %d took from elf %d (%d presents)" % (curr_elf.id, victim.id, new_value))
    curr_elf.value = new_value
    victim.value = 0
    victim.prev.nxt = victim.nxt
    victim.nxt.prev = victim.prev
    victim = victim.nxt
    if puzzle_input % 2 == 1:
        victim = victim.nxt

    puzzle_input -= 1
    curr_elf = curr_elf.nxt
