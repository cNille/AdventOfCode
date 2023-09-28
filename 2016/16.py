print(chr(27)+'[2j')
print('\033c', end='')

puzzle_input = "10111011111001111"

def dragon_curve(in_data:str):
    a = in_data
    b = ""
    for i in range(len(in_data)):
        b += "0" if a[-i-1] == "1" else "1"
    return a + "0" + b

def checksum(in_data:str):
    curr = in_data
    while True:
        i = 0
        nxt = ""
        print("Length of current checksum:", len(curr))
        if len(curr) % 2 == 1:
            return curr
        while True:
            if i >= len(curr):
                curr = nxt
                break
            pair = curr[i:i+2]
            nxt += "1" if pair[0] == pair[1] else "0" 
            i += 2

def combined(length: int, state: str):
    curr_state = state
    count = 0
    while len(curr_state) < length:
        count += 1
        if count % 100 == 0:
            print("Round", count)
        curr_state = dragon_curve(curr_state)

    print("Dragon curve finished with length", len(curr_state))
    curr_state = curr_state[:length]
    result = checksum(curr_state)
    return result



# Test dragon curve
# tests = [
#     "1",
#     "0",
#     "11111",
#     "111100001010"
# ]
# for t in tests:
#     print(t, "gives", dragon_curve(t))
# 
# # Test checksum
# print("Checksum:", checksum("110010110100"))
# # Test combined
# print("Test:", combined(20, "10000"))


print("Part 1:", combined(272, "10111011111001111"))
print("Part 2:", combined(35651584, "10111011111001111"))
