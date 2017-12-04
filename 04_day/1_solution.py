f = open('my.input', 'r')
count = 0

for line in f:
    words = line[:-1].split(' ')

    seen = set()
    valid = True;

    for word in words:
        if word in seen:
            valid = False;
        else:
            seen.add(word)
    
    if valid:
        count +=1

print(count)
