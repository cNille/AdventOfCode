#from time import sleep
from heapq import heappush, heappop
print(chr(27)+'[2j')
print('\033c')
#f = open('17.input', 'r')
f = open('17.test', 'r')
lines = [x.strip() for x in f.readlines()]

mtx = []
for line in lines:
    mtx.append(list(line))


def within_bounds(mtx, new_pos):
    if new_pos[1] < 0 or new_pos[1] >= len(mtx):
        return False
    if new_pos[0] < 0 or new_pos[0] >= len(mtx[0]):
        return False
    return True


N, E, S, W = (0, -1), (1, 0), (0, 1), (-1, 0)
end_pos = (len(mtx[0])-1, len(mtx)-1)
DIRS = [N, E, S, W]


def solve(part2=False):
    start_pos = (0, 0)
    q = []
    heappush(q, (0, 0, start_pos, 1, 1, set()))
    heappush(q, (0, 0, start_pos, 2, 1, set()))
    min_score = 0
    min_scores = {}
    max_score = 999999999

    while q:
        _, heat_loss, pos, d, straight, prev_visited = heappop(q)
        # sleep(0.7)
        if heat_loss > min_score:
            min_score = heat_loss
            #print(heat_loss, pos, d, straight, len(q))
        x, y = pos
        if (x, y, d, straight) not in min_scores:
            min_scores[(x, y, d, straight)] = heat_loss
        else:
            if heat_loss >= min_scores[(x, y, d, straight)]:
                continue
        if pos == end_pos:
            max_score = min(max_score, heat_loss)
        if heat_loss >= max_score:
            continue
        has_visited = False
        for i in range(4):
            if (x, y, i) in prev_visited:
                has_visited = True
                break
        if has_visited:
            continue
        visited = prev_visited | {(x, y, d)}

        if part2:
            can_straight = straight < 10
            can_turn = straight > 3
        else:
            can_straight = straight < 3
            can_turn = straight >= -1

        for i in range(4):
            dx, dy = DIRS[i]
            x2, y2 = (x+dx, y+dy)
            new_pos = (x2, y2)
            if not within_bounds(mtx, new_pos):
                continue
            h2 = heat_loss + int(mtx[y2][x2])
            # no 180 turn
            if abs(d - i) >= 2:
                continue
            if i == d:
                if can_straight:
                    heappush(q, (h2, h2, new_pos, d, straight+1, visited))
            elif i != d and can_turn:
                # turn 90
                heappush(q, (h2, h2, new_pos, i, 1, visited))

    #print('Min score', min_score)
    #print('Max score', max_score)
    return max_score


print('Part 1:', solve())
print('Part 2:', solve(True))
