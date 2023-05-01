import sys
import heapq
sys.setrecursionlimit(10000)
print(chr(27)+'[2j')
print('\033c')
f = open('23.input', 'r')
f = open('23.test', 'r')
data = [x[:-1] for x in f.readlines()]
burrow = [list(x) for x in data]

pods = []
for y, line in enumerate(burrow):
    for x, p in enumerate(line):
        if p != '#' and p!= '.' and p != ' ':
            pods.append((p, x, y))

room = { "A": 3, "B": 5, "C": 7, "D": 9 }
step_cost = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
def p_cost(pod):
    return step_cost[pod[0]]

# A class State with a burrow, pods and a cost
class State:
    def __init__(self, burrow, pods, cost, moves):
        self.burrow = burrow
        self.pods = pods
        self.cost = cost
        self.moves = moves

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def __str__(self):
        return self.print()

    def __eq__(self, other):
        return self.value() == other.value()

    def __hash__(self):
        return hash(self.value())

    def heuristic(self):
        return self.cost + sum([abs(p[1] - room[p[0]]) for p in self.pods])

    def is_goal(self):
        for p in self.pods:
            if room[p[0]] != p[1] or p[2] == 1:
                return False
        return True

    def pod_value(self, pod):
        return pod[0] + str(pod[1]) + str(pod[2])

    def value(self):
        v = [self.pod_value(p) for p in self.pods]
        return "".join(v) 

    def print(self):
        for y, line in enumerate(self.burrow):
            print("\t", end='')
            for x, p in enumerate(line):
                if (x, y) in self.pods:
                    print(p, end='')
                else:
                    print(p, end='')
            print()
        print("Cost: ",self.cost)
    
    def move(self, idx, new_pos):
        curr_pod = self.pods[idx]

        # Update burrow
        state_burrow = [[x for x in line] for line in self.burrow]
        state_burrow[curr_pod[2]][curr_pod[1]] = '.'
        state_burrow[new_pos[1]][new_pos[0]] = curr_pod[0]

        # Update pods
        state_pods = self.pods[:]
        state_pods[idx] = (curr_pod[0], new_pos[0], new_pos[1])

        # Update cost
        delta = (
            # Diff in X
            abs(curr_pod[1] - new_pos[0]) + 
            # Up to hallway
            abs(curr_pod[2] - 1) + 
            # Down from hallway
            abs(new_pos[1] - 1)
        )
        state_cost = self.cost + p_cost(curr_pod) * delta

        # Update moves 
        state_moves = [x[:] for x in self.moves]
        state_moves.append((idx, curr_pod[0], new_pos[0], new_pos[1]))

        return State(state_burrow, state_pods, state_cost, state_moves)


def never_stop_outside_room(new_position):
    if (
        new_position[0] == 3 
        or new_position[0] == 5 
        or new_position[0] == 7 
        or new_position[0] == 9
    ):
        return False
    return True

def move_into_room(pods, curr_pod, pos):
    x = pos[0]
    letter, curr_x, _ = curr_pod
    # Cant stop in current room 
    if x == curr_x:
        return False
    # Check if correct room
    if room[letter] != x:
        return False
    # Check no other pod in room
    for p in pods:
        if p[1] == x and p[0] != letter:
            return False
    return True

def move_to_hallway(pod):
    _, _, y = pod
    if y == 1: 
        # Once in hallway an amphipod can only return to room
        return False
    return True

# A recursive function that takes a burrow and position and returns
# a list of possible moves
def possible_moves(burrow, pos, prev_pos):
    # Get directions (up, down, left, right)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # Get new positions
    new_pos = []
    for d in directions:
        x = pos[0] + d[0]
        y = pos[1] + d[1]
        if (x, y) == prev_pos:
            continue
        if burrow[y][x] != '.':
            continue
        new_pos.append((x, y))
        new_pos.extend(possible_moves(burrow, (x, y), pos))
    return new_pos

    
def available_moves(state: State, idx):
    burrow = state.burrow
    pods = state.pods

    curr_pod = pods[idx]

    # Get neighbours in directions
    x,y = curr_pod[1], curr_pod[2]
    stops = possible_moves(burrow, (x, y), (x, y))

    new_states = []
    for s in stops:
        if s[0] == curr_pod[1]:
            continue
        if s[1] == 1 and not never_stop_outside_room(s) :
            continue
        if s[1] == 1 and not move_to_hallway(curr_pod):
            continue
        if s[1] > 1 and not move_into_room(pods, curr_pod, s):
            continue

        new_state = state.move(idx, s)
        if new_state.cost > 15000:
            continue

        new_states.append(new_state)
    return new_states 

# Create the initial state 
initial_state = State(burrow, pods, 0, [])
states = [initial_state]
heapq.heapify(states)
state = heapq.heappop(states)
visited = set([state.value()])
count = 0 
max_cost = 0
while state:
    count += 1
    max_cost = max(max_cost, state.cost)
    if count % 10000 == 0:
        print("Count: ", count, "States_left: ", len(states), "Max cost: ", max_cost)
    if state.is_goal():
        print("Solution found")
        state.print()
        moves = state.moves
        s = initial_state
        print("INITIAL STATE")
        s.print()
        print("-"*20)
        for m in moves:
            idx, letter, x, y = m
            print("Move:", m)
            s = state.move(idx, (x, y))
            s.print()
            print("-"*20)
        break
    #print("Visited: ", len(visited))
    for i, p in enumerate(pods):
        new_states = available_moves(state, i)
        for n in new_states:
            v = n.value()
            if v in visited:
                continue
            if n.cost > 15000:
                continue
            heapq.heappush(states, n)
            visited.add(v)

    if len(states) == 0:
        break
    state = heapq.heappop(states)

print("Done")



# # too low
# 10971
# # too high
# 11471
