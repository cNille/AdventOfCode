lines = open('my.input', 'r').read().split('\n')

image = [
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#'],
]

def convert_to_int(x):
    if x == '#':
        return 1
    return 0    

def two_square_to_tuple(x):
    return (
        (x[0][0], x[0][1]),
        (x[1][0],x[1][1])
    )
def three_square_to_tuple(x):
    return (
        (x[0][0], x[0][1], x[0][2]),
        (x[1][0], x[1][1], x[1][2]),
        (x[2][0], x[2][1], x[2][2]),
    )

def convert_2_square(image):
    new_image = []
    for x in range(len(image)/2):
        new_row = []
        for y in range(len(image)/2):
            new_row.append([
                image[x*2][y*2],
                image[x*2][y*2+1],
            ])
        

enhancements = {}
lines = [line for line in lines if len(line) > 0]
for line in lines:
    [inp, out] = line.split(' => ')

    inp = [list(x) for x in inp.split('/')]
    out = [list(x) for x in out.split('/')]

    if len(inp) == 2:
        inp = two_square_to_tuple(inp)
        #out = two_square_to_tuple(out)
    else:    
        inp = three_square_to_tuple(inp)
        #out = three_square_to_tuple(out)
    enhancements[inp] = out 

for i in range(5):
    if len(image) % 2 == 0:
        image = convert_2_square(image)
