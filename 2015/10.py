def lookandsay(str_data):
    splitsis = [str_data[0]]
    for d in str_data[1:]:
        if d != splitsis[-1][0]:
            splitsis.append(d)
        else:
            splitsis[-1] = splitsis[-1] + d
    return "".join(
        [
            str(len(x)) + x[0] 
            for x 
            in splitsis
        ]
    )

# Part 1
data = '1321131112'
for i in range(40):
    data = lookandsay(data)
print("Part 1 solution: %d " % len(data))

# Part 2
data = '1321131112'
for i in range(50):
    data = lookandsay(data)
print("Part 2 solution: %d " % len(data))
