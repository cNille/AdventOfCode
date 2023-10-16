print(chr(27)+'[2j')
print('\033c', end='')

# Parse boss stats
f = open('21.input', 'r')
lines = [x.strip() for x in f.readlines()]
hp_line, damage_line, armor_line = lines
boss_hp = int(hp_line.split(' ')[2])
boss_damage = int(damage_line.split(' ')[1])
boss_armor = int(armor_line.split(' ')[1])


# Take turns
def turn(attacker, victim):
    name, hp, attack, armor = victim
    damage = max(1, attacker[2] - armor)
    new_hp = hp - damage
    victim = (name, new_hp, attack, armor)
    return victim, attacker


# Play game
def game(p1, p2):
    victor = None
    while victor == None:
        p1, p2 = turn(p1, p2)
        if p1[1] <= 0:
            victor = p2[0]
    return victor


# Store (cost, damage, armor)
weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

armors = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]

rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]


# All shopping permutations
def all_stats():
    # weapon
    stats = [w for w in weapons]
    # weapon + ring
    for w in weapons:
        for r in rings:
            stats.append((
                w[0] + r[0],
                w[1] + r[1],
                w[2] + r[2]
            ))

    # weapon + ring + ring
    for w in weapons:
        for a in rings:
            for r in rings:
                if a == r:
                    continue
                stats.append((
                    w[0] + a[0] + r[0],
                    w[1] + a[1] + r[1],
                    w[2] + a[2] + r[2]
                ))

    # weapon + armor
    for w in weapons:
        for r in armors:
            stats.append((
                w[0] + r[0],
                w[1] + r[1],
                w[2] + r[2]
            ))

    # weapon + armor + ring
    for w in weapons:
        for a in armors:
            for r in rings:
                stats.append((
                    w[0] + a[0] + r[0],
                    w[1] + a[1] + r[1],
                    w[2] + a[2] + r[2]
                ))

    # weapon + armor + ring + ring
    for w in weapons:
        for a in armors:
            for r1 in rings:
                for r2 in rings:
                    if r1 == r2:
                        continue
                    stats.append((
                        w[0] + a[0] + r1[0] + r2[0],
                        w[1] + a[1] + r1[1] + r2[1],
                        w[2] + a[2] + r1[2] + r2[2]
                    ))
    return stats


stats = all_stats()
stats = sorted(stats)

least = 10000000
most = 0
for s in stats:
    boss = ("Boss", boss_hp, boss_damage, boss_armor)
    player = ("Player", 100, s[1], s[2])
    victor = game(player, boss)
    if victor == "Player":
        least = min(least, s[0])
    if victor == "Boss":
        most = max(most, s[0])

print("Part 1:", least)
print("Part 2:", most)
