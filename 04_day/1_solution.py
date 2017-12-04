


f = open('my.input', 'r')

def isAnagram(w1,w2):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for l in letters:
        if w1.count(l) != w2.count(l):
            return False
    print(w1, w2)
    return True

count = 0

for line in f:
    
    words = line[:-1].split(' ')

    seen = set()
    valid = True;

    for word in words:
        for s in seen:
            if isAnagram(s,word):
                valid = False

        if word in seen:
            valid = False;
        else:
            seen.add(word)
    

    
    if valid:
        count +=1
        




print(count)
