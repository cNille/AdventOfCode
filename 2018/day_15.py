from time import sleep

def solution(data, verbose, elf_power, no_kill=False):
    global elfs, goblins, cave
    # print('-'*80)
    # print('Elfpower %d' % elf_power)
    cave = [d.strip() for d in data]
    if verbose:
        print('Starting board')
        for i, line in enumerate(cave):
            print('%d\t%s' % (i,line))

    # Find all start positions
    goblins = {}
    elfs = {}
    for y, line in enumerate(cave):
        for x, char in enumerate(line):
            if char == 'G':
                goblins[(y,x)] = 200
            if char == 'E':
                elfs[(y,x)] = 200

    def get_move_order():
        global elfs, goblins
        positions = []
        positions.extend([(True,e) for e in elfs if elfs[e] > 0 ])
        positions.extend([(False,g) for g in goblins if goblins[g] > 0 ])
        return sorted(positions, key = lambda x: (x[1][0], x[1][1]))

    def game_over():
        global elfs, goblins
        hp_elfs = sum([elfs[e] for e in elfs if elfs[e] >= 0])
        hp_goblins= sum([goblins[g] for g in goblins if goblins[g] >= 0])
        if hp_elfs <= 0:
            print('Goblins won!')
            return True
        elif hp_goblins <= 0:
            print('Elfs won!')
            return True
        return False

    def distance (x,y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def get_directions (start, checked, distance):
        global cave
        directions = [
            (start[0]-1, start[1]), # up
            (start[0], start[1]-1), # left
            (start[0], start[1]+1), # right
            (start[0]+1, start[1]), # down
        ]
        res = []
        for d in directions:
            if cave[d[0]][d[1]] != '.':
                continue
            if d not in checked:
                res.append(d)
                continue
            if checked[d] >= distance:
                res.append(d)
        return res

    def find_path(start, enemies):
        global cave
        for e in enemies:
            if distance(start, e) == 1:
                return False
        checked = {}
        paths = [[start]]
        checked[start] = True
        depth = 1
        while True:
            new_paths = []
            valid_paths = []
            for p in paths:
                new_d = get_directions(p[-1], checked, len(paths))
                if len(new_d) == 0:
                    continue
                for d in new_d:
                    if d not in checked:
                        new_paths.append(p+[d])
                        checked[d] = depth

                    if checked[d] > depth:
                        new_paths.append(p+[d])
                        checked[d] = depth
            paths = new_paths
            for p in paths:
                for e in enemies:
                    dist = distance(p[-1],e)
                    if dist == 1:
                        res = [a for a in paths if len(p) == len(a) and distance(a[-1],e) == 1]
                        res = sorted(res, key=lambda x: (x[-1][0],x[-1][1]))

                        if res[-1] not in [i[-1] for i in valid_paths]:
                            valid_paths.append(res[0])
            depth += 1
            if len(valid_paths) > 0:
                return valid_paths
            if len(paths) == 0:
                return False


    def find_new_pos(pos, team):
        enemies = []
        if team:
            enemies = [g for g in goblins if goblins[g] > 0]
        else:
            enemies = [e for e in elfs if elfs[e] > 0]
        enemies = sorted(enemies, key = lambda x: (x[0],x[1]))

        paths = find_path(pos, enemies)
        if not paths or len(paths) == 0:
            return False
        paths = sorted(paths, key=lambda x: (x[-1][0], x[-1][1]))

        first = paths[0][1]
        last = paths[0][-1]
        paths = find_path(pos, [last])
        if not paths or len(paths) == 0:
            return first
        paths = sorted(paths, key=lambda x: (x[-1][0], x[-1][1]))
        return paths[0][1]

    def rep_at_idx(s, c, i):
        return "".join((s[:i], c, s[i+1:]))

    def move(src, dst):
        global cave
        ch = cave[src[0]][src[1]]
        cave[dst[0]] = rep_at_idx(cave[dst[0]],  ch, dst[1])
        cave[src[0]] = rep_at_idx(cave[src[0]], '.', src[1])
        if src in elfs:
            elfs[dst] = elfs[src]
            del elfs[src]
        if src in goblins:
            goblins[dst] = goblins[src]
            del goblins[src]

    def attack(pos, team, elf_power):
        global elfs, goblins
        enemies = []
        attack_elfs = not team
        if team:
            if pos not in elfs:
                return
            enemies = [g for g in goblins if distance(g,pos) == 1]
            enemies = sorted(enemies, key=lambda x: (goblins[x], x[0], x[1]))
        else:
            if pos not in goblins:
                return
            enemies = [e for e in elfs if distance(e,pos) == 1]
            enemies = sorted(enemies, key=lambda x: (elfs[x], x[0], x[1]))

        if len(enemies) == 0:
            return False

        attack = enemies[0]
        if attack_elfs:
            elfs[attack] = elfs[attack] - 3
            if elfs[attack] <= 0:
                if verbose:
                    print('Elf died: %s' % (attack, ))
                cave[attack[0]] = rep_at_idx(cave[attack[0]], '.', attack[1])
                del elfs[attack]
                return no_kill
        else:
            goblins[attack] = goblins[attack] - elf_power
            if goblins[attack] <= 0:
                if verbose:
                    print('Goblin died: %s' % (attack, ))
                cave[attack[0]] = rep_at_idx(cave[attack[0]], '.', attack[1])
                del goblins[attack]
        return False

    rounds = 0;
    is_game_over = False
    while not is_game_over:
        if verbose:
            print('='*20)
            print('Starting round %d' % rounds)

        order = get_move_order()
        team = [o[0] for o in order]
        order = [o[1] for o in order]
        no_move = True
        end_game = False
        for i, o in enumerate(order):
            #print('Moving', o)
            new_pos = find_new_pos(o, team[i])
            #print('Moved to', new_pos)
            if new_pos:
                no_move = False
                move(o, new_pos)
                a = attack(new_pos, team[i], elf_power)
                if a:
                    end_game = True
                    print('Elf died')
                    rounds = -1
            else:
                a = attack(o, team[i], elf_power)
                if a:
                    end_game = True
                    print('Elf died')
                    rounds = -1

            is_game_over = game_over()
            if end_game or is_game_over:
                if i == len(order)-1:
                    rounds+=1
                end_game = True
                break
        if end_game:
            break

        sleep(0.2)
        rounds += 1
        if verbose:
            print('Round %d' % rounds)
            for i, line in enumerate(cave):
                print('%d\t%s' % (i,line))
            print('Elfs: ', elfs)
            print('Goblins:',  goblins)
    hitpoints = sum([elfs[e] for e in elfs])
    hitpoints += sum([goblins[e] for e in goblins])
    result = hitpoints * rounds


    if verbose:
        print('Goblins', goblins)
        print('Elfs', elfs)
        print('Hitpoints left: %d' % hitpoints)
        print('Rounds : %d' % rounds)
        print('Result: %d' % result)
    return result

# Import data
# verbose = False
# if solution(open('day_15_test.txt','r').readlines(), verbose) != 27730:
#     print('Should be 47 * 590 = 27730')
#
# verbose = False
# if solution(open('day_15_test2.txt','r').readlines(), verbose) != 36334:
#     print('Should be 37 * 982 = 36334')
#
# verbose = False
# test3 = open('day_15_test3.txt','r').readlines()
# if solution(test3, verbose) != 28944:
#     print('Should be 54 * 536 = 28944')
#
# verbose = False
# test3 = open('day_15_test4.txt','r').readlines()
# if solution(test3, verbose) != 39514:
#     print('Should be 46 * 859 = 39514')
#
# verbose = False
# if solution(open('day_15_test5.txt','r').readlines(), verbose) != 18740:
#     print('Should be 20 * 937 = 18740')
#
# verbose = False
# if solution(open('day_15_test6.txt','r').readlines(), verbose) != 27755:
#     print('Should be 35 * 793 = 27755')


verbose = True
data = open('day_15_input.txt','r').readlines()
res = solution(data, verbose, 3)
print('part 1:', res)

print('-'*80)
for i in range(4, 20):
    res = solution(data, verbose, i, True)
    print('%d: %d' % (i, res))
    if res > 0:
        print('part 2:', res)
        exit()
