print(chr(27)+'[2j')
print('\033c')
f = open('20.test', 'r')
f = open('20.input', 'r')
data = [x.strip() for x in f.readlines()]

algorithm = data[0]
img = data[2:]

def img_print(img):
    #return
    for row in img:
        print(row)

def get_pos(img,x,y, even):
    if x < 0 or x >= len(img[0]):
        return '.' if even else '#'
    if y < 0 or y >= len(img):
        return '.' if even else '#'
    return img[y][x]

def get_code(img, x,y, even):
    points = []
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            point = get_pos(img, x+dx, y+dy, even)
            points.append(point)
    return ''.join(points)

def decode(code):
    code = code.replace('.','0').replace('#','1')
    return int(code, 2)

def count_lit(img):
    count = 0
    for line in img:
        for ch in line:
            if ch == '#':
                count+=1
    return count

def lit(img, even):
    output = [] 
    for y in range(-1, len(img)+1):
        output.append('')
        for x in range(-1, len(img[0])+1):
            code = get_code(img, x,y, even)
            pos = decode(code)
            output[-1] += algorithm[pos]
    return output

# Litify
#print("Starting:")
#img_print(img)
#print("Count:", count_lit(img))
for i in range(50):
    img = lit(img, i % 2 == 0)
    #print("Inhanced round: %d" % (i + 1))
    #img_print(img)
    #print("Count:", count_lit(img))
    if i == 1: 
        print("Part 1 solution: %d" % count_lit(img))
print("Part 2 solution: %d" % count_lit(img))
