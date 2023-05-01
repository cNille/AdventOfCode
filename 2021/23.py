import sys
import heapq
from functools import cache, total_ordering, lru_cache
sys.setrecursionlimit(10000)
print(chr(27)+'[2j')
print('\033c')
#f = open('23.test', 'r')
#f = open('23.test2', 'r')
f1 = open('23.input2', 'r')
f2 = open('23.input', 'r')

goal_found = 9999999
def part(f):
    data = [x[:-1] for x in f.readlines()]
    burrow = "\n".join([x for x in data])

    pods = []
    for y, line in enumerate(burrow.split("\n")):
        for x, p in enumerate(line):
            if p != '#' and p!= '.' and p != ' ':
                pods.append((p, x, y))

    room = { "A": 3, "B": 5, "C": 7, "D": 9 }
    step_cost = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }

    def p_cost(pod):
        return step_cost[pod[0]]

    # A class State with a burrow, pods and a cost
    @total_ordering
    class State:
        def __init__(self, burrow, pods, cost, moves):
            self.burrow = burrow
            self.pods = pods
            self.cost = cost
            self.moves = moves
            self.v = "".join([self.pod_value(p) for p in self.pods]) 

        def __lt__(self, other):
            return self.cost < other.cost

        def __eq__(self, other):
            return self.cost == other.cost

        def __hash__(self):
            return hash(self.value())

        def is_goal(self):
            for p in self.pods:
                if room[p[0]] != p[1] or p[2] == 1:
                    return False
            return True

        def pod_value(self, pod):
            return pod[0] + str(pod[1]) + str(pod[2])

        def value(self):
            return self.v

        def print(self):
            for y, line in enumerate(self.burrow.split('\n')):
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
            state_burrow = [[x for x in line] for line in self.burrow.split('\n')]
            state_burrow[curr_pod[2]][curr_pod[1]] = '.'
            state_burrow[new_pos[1]][new_pos[0]] = curr_pod[0]
            state_burrow = "\n".join(["".join(line) for line in state_burrow])

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
            state_moves = self.moves.copy()
            if idx not in state_moves:
                state_moves[idx] = 0
            state_moves[idx] += 1 

            return State(state_burrow, state_pods, state_cost, state_moves)

    @cache
    def stop_outside_room(new_position):
        return new_position[1] == 1 and (
            new_position[0] == 3 
            or new_position[0] == 5 
            or new_position[0] == 7 
            or new_position[0] == 9
        )

    @cache
    def room_busy(burrow, curr_pod, pos):
        letter, _, _ = curr_pod
        if pos[1] == 1:
            return False
        # Check if correct room
        if room[letter] != pos[0]:
            return True
        # Check no other pod in room
        lines = burrow.split('\n')
        room_col = room[letter]
        for l in lines[2:-1]:
            if l[room_col] == '.':
                continue
            if l[room_col] != letter:
                return True
        return False

    @cache
    def move_within_hallway(pod, new_pos):
        # Once in hallway an amphipod can only return to room
        return new_pos[1] == 1 and pod[2] == 1

    # A recursive function that takes a burrow and position and returns
    # a list of possible moves
    @cache
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
            if burrow.split('\n')[y][x] != '.':
                continue
            new_pos.append((x, y))
            new_pos.extend(possible_moves(burrow, (x, y), pos))
        return new_pos

    @cache
    def available_moves(state: State, idx):
        global goal_found
        burrow = state.burrow
        pods = state.pods

        curr_pod = pods[idx]

        new_states = []
        pos = (curr_pod[1], curr_pod[2])
        stops = possible_moves(burrow, pos, pos)
        for s in stops:
            if s[0] == curr_pod[1]:
                continue
            if move_within_hallway(curr_pod, s):
                continue
            if stop_outside_room(s):
                continue
            if room_busy(burrow, curr_pod, s):
                continue
            if idx in state.moves and state.moves[idx] == 2:
                continue
            new_state = state.move(idx, s)
            if new_state.cost >= goal_found or new_state.cost > 60000:
                continue
            if new_state.is_goal():
                goal_found = new_state.cost
                print("Solution found")
                state = new_state
                state.print()
                print("-"*20)
            new_states.append(new_state)
        return new_states 

    # Create the initial state 
    initial_state = State(burrow, pods, 0, {})
    initial_state.print()
    states = [initial_state]
    heapq.heapify(states)
    state = heapq.heappop(states)
    visited = set([state.value()])
    count = 0 
    max_cost = 0
    goal_found = 9999999
    while state:
        count += 1
        max_cost = max(max_cost, state.cost)
        if count % 10000 == 0:
            print("Count: ", count, "States_left: ", len(states), "max_cost", max_cost)
        if state.cost >= goal_found:
            if len(states) == 0:
                break
            state = heapq.heappop(states)
            continue
        for i, p in enumerate(pods):
            new_states = available_moves(state, i)
            for n in new_states:
                v = n.value()
                if v in visited:
                    continue
                heapq.heappush(states, n)
                visited.add(v)

        if len(states) == 0:
            break
        state = heapq.heappop(states)

res1 = part(f1)
print("Result1:", res1)
res2 = part(f2)
print("Result2:", res2)




# # too low
# 10971
# # too high
# 11471
