data = open('24.in', 'r').read().split('\n\n')
#data = open('24test.in', 'r').read().split('\n\n')
immune = [line for line in data[0].split('\n')[1:] if len(line) > 0]
infection = [line for line in data[1].split('\n')[1:] if len(line) > 0]


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

    def attacked(self, damage):
        units_killed = int(float(damage) / float(self.hitpoints))

        self.units -= units_killed

        # print("%s attacked with %d damage! %d killed, %d left" %
        #       (self.id, damage, units_killed, self.units))

    def __repr__(self):
        return "%s = %d units; %d hp; %d initiative" % (
            self.id, self.units, self.hitpoints, self.initiative)


immune = [Unit(line, 'immune', idx) for idx, line in enumerate(immune)]
infection = [
    Unit(line, 'infection', idx) for idx, line in enumerate(infection)
]
units = immune + infection
unit_ids = [u.id for u in units]
loosing_score = len(immune)


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
        attack.append((damage, unit.initiative, enemy.initiative, unit.id,
                       enemy.id, enemy.effective_power()))
    attack = sorted(attack, key=lambda x: (-x[0], -x[5], -x[2]))

    if len(attack) > 0 and attack[0][0] <= 0:
        return []

    return attack


def target_phase(units):
    damages = []
    units = sorted(
        units, key=lambda x: (x.effective_power(), x.initiative), reverse=True)

    #print('-' * 80)
    #print('Damages')
    targets = []
    for unit in units:
        damage = attack_damage(unit, get_enemies(unit, units))
        #print(damage)
        while len(damage) > 0:
            _, _, _, attacker, target, _ = damage.pop(0)
            if target in [x[1] for x in targets]:
                continue
            targets.append((attacker, target))
            break
    #print('-' * 80)
    #print('TARGETS')
    #for t in targets:
    #    print(t)
    #print('-' * 80)
    return targets


def attack_phase(units, targets):
    units = sorted(units, key=lambda x: x.initiative, reverse=True)

    for unit in units:
        if unit.units <= 0:
            continue

        ts = [t for t in targets if t[0] == unit.id]
        if len(ts) == 0:
            continue

        _, attacked_id = ts[0]
        enemy = [e for e in units if e.id == attacked_id][0]
        damage = calc_damage(unit, enemy)
        #print('ATTACK', unit, enemy)
        enemy.attacked(damage)

    return [u for u in units if u.units > 0]


i = 1
while loosing_score > 0:
    print('-' * 80)
    print('Round %d' % i)

    if i > 70 and False:
        exit()

    immune = [u for u in units if u.team == 'immune']
    infection = [u for u in units if u.team == 'infection']

    print('Immune system:')
    for u in immune:
        print("%s has %d units" % (u.id, u.units))
    print('Infection:')
    for u in infection:
        print("%s has %d units" % (u.id, u.units))
    print('')

    targets = target_phase(units)
    units = attack_phase(units, targets)

    loosing_score = min(
        len([_ for _ in units if _.team == 'immune']),
        len([_ for _ in units if _.team != 'immune']),
    )
    i += 1

print('@' * 80)
print('@' * 80)
print('')
print('GAME OVER')
print('')
for u in units:
    print("%s with %d units left" % (u.id, u.units))
print('')
print('Result: %d' % sum([u.units for u in units]))

# Too low: 13216
# Too low: 13311
# Correct: 13327
