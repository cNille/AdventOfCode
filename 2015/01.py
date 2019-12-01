data = open('01.input').readlines()[0]

# Part 1:
up = len([x for x in data if x == '('])
down = len([x for x in data if x == ')'])
result = up - down
print(result)

# Part 2:

idx = 0
for pos, direction in enumerate(data):
    idx += 1 if direction == '(' else -1

    if idx == -1:
        print("Done:", pos + 1)
        break;
