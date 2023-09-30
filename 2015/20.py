print(chr(27)+'[2j')
print('\033c', end='')


from math import ceil, sqrt
print("Day 20")

puzzle_input = 36000000
max_presents = 0
house_nbr = 0 
while max_presents < puzzle_input:
    house_nbr += 1
    presents = 0
    until = ceil(sqrt(house_nbr))
    for elf_number in range(until):
        elf_number += 1
        if house_nbr % elf_number == 0:
            other = int(house_nbr / elf_number)
            presents += 10 * (elf_number + other)

    if presents > max_presents:
        max_presents = presents

    if house_nbr % 20000 == 0:
        print("%d, max: %d presents" % (house_nbr, max_presents))
part1 = house_nbr

max_presents = 0
while max_presents < puzzle_input:
    house_nbr += 1
    presents = 0
    for elf_number in range(50):
        elf_number += 1
        if house_nbr % elf_number == 0:
            other = int(house_nbr / elf_number)
            presents += 11 * (elf_number + other)

    if presents > max_presents:
        max_presents = presents

    if house_nbr % 1000 == 0:
        print("%d, max: %d presents" % (house_nbr, max_presents))

print("Part 1: %d" % (part1))
print("Part 2: %d" % (house_nbr))
