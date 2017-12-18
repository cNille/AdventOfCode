lines = open('my.input').readlines()
children = set() 
for line in lines:
    cols = line.split('->')
    children.update([c.strip().strip(',') for c in cols[-1].split(' ') if len(cols) > 1])

print(children)
for line in lines:
    cols = line.split('->')
    if len(cols) > 1:
        c = cols[0].split(' ')[0].strip()
        if c not in children:
            print(c, len(c))

print('done')
