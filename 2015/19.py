print(chr(27)+'[2j')
print('\033c', end='')

from heapq import heappush, heappop

#f = open('19.test', 'r')
f = open('19.input', 'r')
lines = [x.strip() for x in f.readlines()] 

register_replacements = True
replacement = {} 
molecule = '' 
for line in lines:
    if line == '':
        register_replacements = False
        continue
    if register_replacements:
        line = line.split(' => ')
        if line[0] not in replacement:
            replacement[line[0]] = []
        replacement[line[0]].append(line[1])
    else:
        molecule = line

def apply_replacement(molecule, replacement):
    new_molecules = set()
    for i in range(len(molecule)):
        curr = molecule[i:]
        for r in replacement:
            for new_r in replacement[r]:
                if curr.startswith(r):
                    new_molecule = molecule[:i] + new_r + molecule[i+len(r):]
                    new_molecules.add(new_molecule)
    return new_molecules

new_molecules = apply_replacement(molecule, replacement)
print("Part 1:", len(new_molecules))

reverse_replacement = {}
for r in replacement:
    for new_r in replacement[r]:
        if new_r not in reverse_replacement:
            reverse_replacement[new_r] = []
        reverse_replacement[new_r].append(r)

q = []
heappush(q, (0, 0, molecule))
steps = 0
end_result = 'e' 
max_step = 0
visited = set()
while len(q) > 0:
    h, steps, molecule = heappop(q)
    if steps > max_step:
        max_step = steps

    if molecule == end_result:
        break

    new_molecules = apply_replacement(molecule, reverse_replacement)
    for m in new_molecules:
        if m not in visited:
            visited.add(m)
            heappush(q, (steps + len(m), steps + 1, m))

print("Part 2:", steps)
