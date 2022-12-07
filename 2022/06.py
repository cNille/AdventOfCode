print(chr(27)+'[2j')
print('\033c')
f = open('06.input', 'r')
f = open('06.test', 'r')
line = [x for x in f.read().strip()]

def detect(window_size):
    window = []
    for i,ch in enumerate(line):
        if len(window) == window_size:
            window.pop(0)
        window.append(ch)
        if len(set(window)) == window_size:
            return i+1

print("Solution part 1:", detect(4))
print("Solution part 2:", detect(14))
