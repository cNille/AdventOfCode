import re
lines = [x.strip() for x in open('16.test', 'r').readlines() if x != '']
lines = [x.strip() for x in open('16.input', 'r').readlines() if x != '']

bounds = []
fields = {}
for line in lines:
    matches = re.match(r'^(.*): (\d*)-(\d*) or (\d*)-(\d*)', line)
    if not matches:
        continue
    field, low1, upper1, low2, upper2 = matches.groups()
    bounds.append((int(low1), int(upper1)))
    bounds.append((int(low2), int(upper2)))
    fields[field] = (int(low1), int(upper1), int(low2), int(upper2))


i = lines.index('nearby tickets:')
other_tickets = lines[i+1:]
error_rate = []
tickets = []
for line in other_tickets:
    values = map(int, line.split(','))
    all_valid = True
    for v in values:
        valid = any([a <= v <= b for a,b in bounds])
        if not valid:
            error_rate.append(v)
            all_valid = False
    if all_valid:
        tickets.append(values)

print "Solution part 1: %d" %sum(error_rate)

field_pos = {}
while len(field_pos) < len(fields):
    for i in range(len(fields)):
        values = [t[i] for t in tickets]
        valid_column = [] 
        for f in fields:
            if f in field_pos:
                continue
            l1, u1, l2, u2 = fields[f]
            valid_columns = 
            if all([l1 <= v <= u1 or l2 <= v <= u2 for v in values]):
                valid_column.append(f)

        # If we find only one field that can be True
        if len(valid_column) == 1: 
            field_pos[valid_column[0]] = i

i = lines.index('your ticket:')
my_ticket = map(int, lines[i+1].split(','))

depart = [
    'departure location',
    'departure station',
    'departure platform',
    'departure track',
    'departure date',
    'departure time',
]

values = [my_ticket[field_pos[d]] for d in depart]
tot = 1
for v in values:
    tot *= v
print "Solution part 2: %d" % tot 
