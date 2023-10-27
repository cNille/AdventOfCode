lines = open('./21_day/my.input', 'r').read().split('\n')


# Rotate key
def rotate_key(key: list[str]):
    if len(key) == 2:
        return "/".join([
            key[1][0] + key[0][0],
            key[1][1] + key[0][1]
        ])
    if len(key) == 3:
        return "/".join([
            key[2][0] + key[1][0] + key[0][0],
            key[2][1] + key[1][1] + key[0][1],
            key[2][2] + key[1][2] + key[0][2],
        ])
    raise Exception('Unknown key size')


# Flip key
def flip_key(key: list[str]):
    if len(key) == 2:
        return "/".join([
            key[1][0] + key[1][1],
            key[0][0] + key[0][1]
        ])
    if len(key) == 3:
        return "/".join([
            key[2][0] + key[2][1] + key[2][2],
            key[1][0] + key[1][1] + key[1][2],
            key[0][0] + key[0][1] + key[0][2],
        ])
    raise Exception('Unknown key size')


rules_list = [
    "../.# => ##./#../...",
    ".#./..#/### => #..#/..../..../#..#"
]

rules_list = lines[:-1]


rules_list = [x.split(' => ') for x in rules_list]
rules: dict[str, str] = {x[0]: x[1] for x in rules_list}

extra_rules = {x: rules[x] for x in rules}
for key in rules:
    rotated_key = rotate_key(key.split('/'))
    flipped_key = flip_key(key.split('/'))
    rotated_flipped_key = rotate_key(flipped_key.split('/'))
    extra_rules[flipped_key] = extra_rules[key]
    extra_rules[rotated_flipped_key] = extra_rules[key]
    rotated_flipped_key = rotate_key(rotated_flipped_key.split('/'))
    extra_rules[rotated_flipped_key] = extra_rules[key]
    rotated_flipped_key = rotate_key(rotated_flipped_key.split('/'))
    extra_rules[rotated_flipped_key] = extra_rules[key]
    rotated_flipped_key = rotate_key(rotated_flipped_key.split('/'))
    extra_rules[rotated_flipped_key] = extra_rules[key]
    extra_rules[rotated_key] = extra_rules[key]
    rotated_key = rotate_key(rotated_key.split('/'))
    extra_rules[rotated_key] = extra_rules[key]
    rotated_key = rotate_key(rotated_key.split('/'))
    extra_rules[rotated_key] = extra_rules[key]

rules = extra_rules
del extra_rules

# for r in rules:
#    print(r, "\t=>\t", rules[r])

image = [
    '.#.',
    '..#',
    '###',
]

for iteration in range(18):
    print("Iteration", iteration)
    if len(image) % 2 == 0:
        new_image = []
        for y in range(0, len(image), 2):
            new_image.append([])
            for x in range(0, len(image), 2):
                key = "/".join([
                    image[y][x:x+2],
                    image[y+1][x:x+2]
                ])
                new_image[-1].append(rules[key].split('/'))
        image = []
        for y in range(len(new_image)):
            for i in range(len(new_image[y][0])):
                image.append('')
            for x in range(len(new_image[y])):
                for i in range(len(new_image[y][x])):
                    image[-1-i] += new_image[y][x][i]
    elif len(image) % 3 == 0:
        new_image = []
        for y in range(0, len(image), 3):
            new_image.append([])
            for x in range(0, len(image), 3):
                key = "/".join([
                    image[y][x:x+3],
                    image[y+1][x:x+3],
                    image[y+2][x:x+3]
                ])
                new_image[-1].append(rules[key].split('/'))
        image = []
        for y in range(len(new_image)):
            for i in range(len(new_image[y][0])):
                image.append('')
            for x in range(len(new_image[y])):
                for i in range(len(new_image[y][x])):
                    image[-1-i] += new_image[y][x][i]
    else:
        raise Exception('Unknown image size')

    # print("\n".join(image))
    # print()

    print("Iteration", iteration, ":", sum([x.count('#') for x in image]))

# Too high: 330
# Next: 162
