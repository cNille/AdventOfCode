data = open('24.in', 'r').read().split('\n\n')

#data = open('24test.in', 'r').read().split('\n\n')


class Unit(object):
    def __init__(self, line, team, idx):
        self.team = team
        self.id = "%s %d" % (team, idx + 1)
        s, s2 = line.split('points ')
        s = s.split()
        self.units = int(s[0])
        self.hitpoints = int(s[4])
        self.immune = ''
        self.weak = ''
        if s2.startswith('('):
            s = s2[1:].split(')')[0].split(';')
            for x in s:
                x = x.strip()
                if x.startswith('immune'):
                    self.immune = x[10:]
                if x.startswith('weak'):
                    self.weak = x[8:]
        s2 = s2.split('does ')[1].split()
        self.damage = int(s2[0])
        self.type = s2[1]
        self.initiative = int(s2[-1])

    def effective_power(self):
        return self.damage * self.units

    def attacked(self, damage, by):
        units_killed = int(float(damage) / float(self.hitpoints))
        self.units -= units_killed

        # print("%s attacked by %s with %d damage! %d killed, %d left" %
        #       (self.id, by, damage, units_killed, self.units))

    def __repr__(self):
        return "%s = %d units; %d hp; %d initiative" % (
            self.id, self.units, self.hitpoints, self.initiative)


def parse_data(data):
    immune = [line for line in data[0].split('\n')[1:] if len(line) > 0]
    infection = [line for line in data[1].split('\n')[1:] if len(line) > 0]

    immune = [Unit(line, 'immune', idx) for idx, line in enumerate(immune)]
    infection = [
        Unit(line, 'infection', idx) for idx, line in enumerate(infection)
    ]
    units = immune + infection
    return units


def get_enemies(unit, others):
    return [x for x in others if x.team != unit.team]


def calc_damage(unit, enemy):
    coeff = 1
    if unit.type in enemy.immune:
        coeff = 0
    if unit.type in enemy.weak:
        coeff = 2
    damage = unit.effective_power() * coeff
    return max(0, damage)


def attack_damage(unit, enemies):
    attack = []
    for enemy in enemies:
        damage = calc_damage(unit, enemy)
        if damage <= 0:
            continue
        attack.append((damage, unit.initiative, enemy.initiative, unit.id,
                       enemy.id, enemy.effective_power(), enemy.hitpoints))
    return sorted(attack, key=lambda x: (-x[0], -x[5], -x[2]))


def battle(units, boost):

    i = 1
    unit_ids = [u.id for u in units]
    for unit in units:
        if unit.team == 'immune':
            unit.damage += boost
    loosing_score = 1
    did_attack = False
    while loosing_score > 0:
        if i % 1000000 == 0:
            print('-' * 40)
            print('Round %d' % i)

            units = sorted(units, key=lambda x: (x.units))
            print("Team immune")
            for u in [u for u in units if u.team == "immune"]:
                print("%s with %d units left" % (u.id, u.units))
            print("Team infection")
            for u in [u for u in units if u.team == "infection"]:
                print("%s with %d units left" % (u.id, u.units))
            print('')

        # Target phase
        damages = []
        units = sorted(
            units,
            key=lambda x: (x.effective_power(), x.initiative),
            reverse=True)

        targets = []
        for unit in units:
            damages.append(attack_damage(unit, get_enemies(unit, units)))
            for damage in damages[-1]:
                _, _, _, attacker, target, _, _ = damage
                if target in [x[1] for x in targets]:
                    continue
                targets.append((attacker, target))
                break
        # Attack phase
        units = sorted(units, key=lambda x: x.initiative, reverse=True)
        did_attack = False
        for unit in units:
            if unit.units <= 0:
                continue

            ts = [t for t in targets if t[0] == unit.id]
            if len(ts) == 0:
                continue

            _, attacked_id = ts[0]
            enemy = [e for e in units if e.id == attacked_id][0]
            damage = calc_damage(unit, enemy)
            enemy.attacked(damage, unit.id)
            if damage >= enemy.hitpoints:
                did_attack = True

        units = [u for u in units if u.units > 0]

        loosing_score = min(
            len([_ for _ in units if _.team == 'immune']),
            len([_ for _ in units if _.team != 'immune']),
        )

        if not did_attack:
            return ('draw', 0)

        i += 1

    winner = units[0].team
    points = sum([u.units for u in units])
    return (winner, points)


winner = ''
boost = 0
while winner != 'immune':
    units = parse_data(data)
    winner, points = battle(units, boost)
    print("BOOST %d == %s won with %d points" % (boost, winner, points))

    boost += 1
