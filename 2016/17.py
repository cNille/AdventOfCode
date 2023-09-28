print(chr(27)+'[2j')
print('\033c', end='')

from heapq import heappush, heappop
import hashlib

open_chars = [
    "b",
    "c",
    "d",
    "e",
    "f",
]
closed_chars = [
    "a",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
path_chars = ["U", "D", "L", "R"]


puzzle_input = "veumntbg"


print("Day 17")

def maze(passcode: str):
    print("Passcode", passcode)
    paths: list[tuple[int, str, int, int]] = [(0, passcode, 0, 0)]

    h = []
    heappush(h, paths[0])
    visited = set() 

    shortest = None
    longest = 0

    while len(h) > 0:
        size, path, x,y = heappop(h) 
        if path in visited:
            continue
        visited.add(path)
        if x == 3 and y == 3 :
            if size > longest:
                longest = size
            #print("Shortest in", size)
            if shortest == None:
                shortest = path[len(passcode):]
            continue

        hash = hashlib.md5(path.encode("utf-8")).hexdigest()[:4]

        for idx, ch in enumerate(hash):
            if ch in open_chars:
                direction = path_chars[idx]
                new_path = path + direction 
                x1 = x 
                y1 = y
                if direction == "U":
                    y1 -= 1
                if direction == "D":
                    y1 += 1
                if direction == "L":
                    x1 -= 1
                if direction == "R":
                    x1 += 1
                
                if 0 <= x1 <= 3 and 0 <= y1 <= 3:
                    new_item = (len(new_path) - len(passcode), new_path, x1, y1)
                    heappush(h, new_item)

    print("Shortest", shortest)
    print("Longest", longest)
    return shortest


print('-'*80)
#print(maze("hijkl"))
print('-'*80)
test ="ihgpwlah" 
print("Resulting path", maze(test))
# assert(maze(test) == "DDRRRD" )
test ="kglvqrro" 
print("Resulting path", maze(test))
# assert(maze(test) == "DDUDRLRRUDRD")
test ="ulqzkmiv" 
print("Resulting path", maze(test))
# assert(maze(test) == "DRURDRUDDLLDLUURRDULRLDUUDDDRR")



print("Resulting path", maze(puzzle_input))
