print(chr(27)+'[2j')
print('\033c')
#f = open('15.input', 'r')
f = open('15.test', 'r')
lines = [x.strip() for x in f.readlines()]


def get_hash(s: str):
    current_value = 0
    for char in s:
        v = ord(char)
        current_value += v
        current_value *= 17
        current_value %= 256
    return current_value


def start_letters(s: str):
    letters = []
    for c in s:
        if c.isalpha():
            letters.append(c)
        else:
            break
    return ''.join(letters)


def calculate_power(boxes: dict[int, list[str]]):

    power = 0
    box_keys = list(boxes.keys())
    sorted_keys = sorted(box_keys)
    for box in sorted_keys:
        box_number = box + 1
        lenses = boxes[box]

        for i in range(len(lenses)):

            slot_number = i + 1
            focal_length = lenses[i].split()[1]
            focal_length = int(focal_length)
            lens_power = box_number * focal_length * slot_number
            power += lens_power
    return power


total = 0
power = 0
boxes = {}
sequence = lines[0].split(',')
for s in sequence:
    total += get_hash(s)
    label = start_letters(s)
    box_value = get_hash(label)
    assert(box_value >= 0)
    assert(box_value <= 255)
    if box_value not in boxes:
        boxes[box_value] = []

    if '=' in s:
        lens = " ".join(s.split('='))
        if label not in [start_letters(x) for x in boxes[box_value]]:
            boxes[box_value].append(lens)
        else:
            idx = [start_letters(x) for x in boxes[box_value]].index(label)
            boxes[box_value][idx] = lens
    elif '-' in s:
        boxes[box_value] = [l for l in boxes[box_value]
                            if label != start_letters(l)]
        if len(boxes[box_value]) == 0:
            del boxes[box_value]
    else:
        raise Exception("Unknown command", s)

power = calculate_power(boxes)


print("Part1", total)
print("Part2", power)
