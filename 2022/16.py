print(chr(27)+'[2j')
print('\033c')
from collections import deque
f = open('16.test', 'r')
#f = open('16.input', 'r')
lines = [x.strip() for x in f.readlines()]

print("Day 16")

graph = {}
rates = {}
valves = []
valves_with_rate = []

for line in lines:
    print(line)
    words = line.split(' ')
    valve = words[1]
    to = words[words.index("to")+2:]
    to = [x.replace(',', '') for x in to]
    graph[valve] = to
    rates[valve] = int(words[4].split('=')[1][:-1])
    valves.append(valve)
    if rates[valve] > 0:
        valves_with_rate.append(valve)

distances = {} 
for v in valves:
    distances[v] = {}
    q = deque()
    for n in graph[v]:
        q.append((n, 1))
    while len(q) > 0:
        n, dist = q.popleft()
        if n in distances[v]:
            continue
        distances[v][n] = dist
        for n2 in graph[n]:
            q.append((n2, dist+1))

def generate_permutations(curr, nodes_left, visited, time):
    perms = [visited]
    for nxt in nodes_left:
        cost = distances[curr][nxt] + 1
        if cost < time:
            new_visited = visited + [nxt]
            sub_perms = generate_permutations(
                nxt, 
                {x for x in nodes_left if x not in new_visited}, 
                new_visited, 
                time - cost
            )
            perms.extend(sub_perms)
    return perms

def calculate_permutation(perms, START_TIME):
    releases = []
    for nodes in perms:
        time = START_TIME
        new_release = 0
        if(len(nodes) == 0):
            continue

        curr = 'AA' 
        for nxt in nodes:
            time -= (distances[curr][nxt] + 1)
            if time < 0:
                break
            new_release += (time * rates[nxt])
            curr = nxt
        releases.append((new_release, set(nodes)))
    return releases

print('-'*40)
nodes_left = {x for x in valves_with_rate}
perms = generate_permutations("AA", nodes_left, [], 30)
releases = calculate_permutation(perms, 30)
print("Solution part 1", max([x[0] for x in releases]))

nodes_left = {x for x in valves_with_rate}
perms = generate_permutations("AA", nodes_left, [], 26)
releases = calculate_permutation(perms, 26)

def has_common(set1, set2):
    for s1 in set1:
        if s1 in set2:
            return True
    return False

TOP_SCORE = 0
rows = len(releases)
releases.sort(key=lambda x: -x[0])
for i1, (score1, visited1) in enumerate(releases):
    for (score2, visited2) in releases[i1+1:]:
        if not has_common(visited1, visited2):
            score = score1 + score2
            if TOP_SCORE < score:
                TOP_SCORE = score
print("Solution part 2:", TOP_SCORE)

# Part 1
# TIME = 30
# RELEASED = 0
# RATE = 0
# init_open_valves = tuple([False for _ in valves])
# 
# q = deque()
# q = []
# q.append((0, TIME, "AA", init_open_valves, []))
# TOP_SCORE = 0
# itr = 0 
# while len(q) > 0:
#     released, time, valve, open_valves, visited = q.pop(0)
#     if time < 1:
#         continue
#     if itr % 1000000 == 0:
#         print(itr, TOP_SCORE, len(q))
#     itr += 1
# 
#     # Check that all valves with flow are open.
#     no_more_todo = True
#     for v in valves_with_rate:
#         if not open_valves[valves.index(v)]:
#             no_more_todo = False
#     if no_more_todo:
#         continue
# 
#     new_visited = visited + [valve]
# 
#     # Scenario: Open valve
#     if not open_valves[valves.index(valve)]:
#         new_opened = [v for v in open_valves]
#         new_opened[valves.index(valve)] = True
#         new_opened = tuple(new_opened)
#         gains = (time-1) * rates[valve]
#         new_released = released + gains 
#         if new_released > TOP_SCORE:
#             TOP_SCORE = new_released 
#             print(TOP_SCORE, 
#                 "Open valve", valve, 
#                 "at time", time, 
#                 "gain", gains, 
#             )
#         q.append((new_released, time-1, valve, new_opened, new_visited))
# 
#     # Scenario: Move to other node with flow
#     for next_v in valves_with_rate:
#         if open_valves[valves.index(next_v)]:
#             continue
#         if next_v in new_visited:
#             continue
#         dist = distances[valve][next_v]
#         new_time = time - dist
#         q.append((released, new_time, next_v, open_valves, new_visited))
#     if itr % 100 == 0:
#         q.sort(key=lambda x: -x[0])
# print("Solution part 1:", TOP_SCORE)
