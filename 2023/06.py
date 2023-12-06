print(chr(27)+'[2j')
print('\033c')
f = open('06.input', 'r')
#f = open('06.test', 'r')
content = [x.strip() for x in f.readlines()]
lines = content

print('Day 06')
times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))

def win_race(time, distance):
    count_ways_to_win = 0
    count = 0
    for i in range(1,time+1):
        count += 1

        speed = i
        time_left = time - i
        d = time_left * speed
        if d > distance:
            count_ways_to_win += 1
    return count_ways_to_win

res = 1
for i, _ in enumerate(times):
    ways_to_win = win_race(times[i], distances[i])
    res *= ways_to_win

print('Part1:', res)

# Part 2
time = ''
distance = ''
for i, _ in enumerate(times):
    time += str(times[i])
    distance += str(distances[i])
time = int(time)
distance = int(distance)

ways_to_win = win_race(time, distance)
print('Part2:', ways_to_win)

