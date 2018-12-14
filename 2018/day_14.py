def part1():
    data = 503761
    recipes = [3,7]
    i1 = 0
    i2 = 1

    while len(recipes) < (data+10):
        score1 = recipes[i1]
        score2 = recipes[i2]
    
        for char in str(score1 + score2):
            recipes.append(int(char))
    
        i1 = (i1 + score1 + 1) % len(recipes)
        i2 = (i2 + score2 + 1) % len(recipes)
        
    print('Result is: %s' % ''.join([str(i) for i in recipes[data:data+10]]))

def part2():
    data2 = '503761'
    i1 = 0 
    i2 = 1
    recipes2 = '37'
    while data2 not in recipes2[-8:]:
        score1 = int(recipes2[i1])
        score2 = int(recipes2[i2])
        recipes2 += str(score1 + score2)
        i1 = (i1 + score1 + 1) % len(recipes2)
        i2 = (i2 + score2 + 1) % len(recipes2)

        if(len(recipes2) % 500001 == 0):
            print('Iteration: %d ' % len(recipes2))

    result = recipes2.index(data2)
    print('Found answer!')
    print('At index %d' % result)
    

print('Part1')
part1()
print('-'*80)
print('Part2')
part2()
