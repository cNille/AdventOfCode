from heapq import heappush, heappop, heapify
print(chr(27)+'[2j')
print('\033c', end='')
print('-'*80)
print('-'*80)
print('-'*80)


class Action:
    def __init__(self, name, cost, turns, user_hp_effect, user_mp_effect, target_hp_effect, target_mp_effect):
        self.name = name
        self.turns = turns
        self.cost = cost
        self.user_hp_effect = user_hp_effect
        self.user_mp_effect = user_mp_effect
        self.target_hp_effect = target_hp_effect
        self.target_mp_effect = target_mp_effect


MAGIC_MISSILE = Action("Magic Missile", 53, 1, 0, 0, -4, 0)
DRAIN = Action("Drain", 73, 1, 2, 0, -2, 0)
SHIELD = Action("Shield", 113, 6, 0, 0, 0, 0)
POISON = Action("Poison", 173, 6, 0, 0, -3, 0)
RECHARGE = Action("Recharge", 229, 5, 0, 101, 0, 0)


class Effect:
    def __init__(self, name, turns, hp_effect, mana_effect) -> None:
        self.name = name
        self.hp_effect = hp_effect
        self.mana_effect = mana_effect
        self.turns = turns

    def __str__(self):
        return f'Effect: {self.hp_effect} {self.mana_effect} {self.turns}'

    def __repr__(self):
        return f'Effect: {self.hp_effect} {self.mana_effect} {self.turns}'


counter = 0


class Player:
    effects: list[Effect] = []

    def __init__(self, name, hp, mana, actions, effects=[]) -> None:
        self.name = name
        self.hp = hp
        self.mana = mana
        self.actions = actions
        self.effects = effects

    def apply_action(self, action, target):
        self_effect = Effect(action.name,
                             action.turns, action.user_hp_effect, action.user_mp_effect)
        self.effects.append(self_effect)
        target_effect = Effect(action.name,
                               action.turns, action.target_hp_effect, action.target_mp_effect)
        target.effects.append(target_effect)

    def apply_instant_effects(self):
        for effect in self.effects:
            if not (effect.name == 'Magic Missile' or effect.name == 'Drain' or effect.name == 'Hit'):
                continue
            change = effect.hp_effect + effect.mana_effect
            self.hp += effect.hp_effect
            self.mana += effect.mana_effect
            effect.turns -= 1
            # print(
            #    f'Instant {effect.name} deals {change}, {effect.turns} turns left')
        self.effects = [effect for effect in self.effects if effect.turns > 0]

    def apply_effects(self):
        for effect in self.effects:
            change = effect.hp_effect + effect.mana_effect
            self.hp += effect.hp_effect
            self.mana += effect.mana_effect
            effect.turns -= 1
            # print(
            #    f'{effect.name} deals {change}, {effect.turns} turns left')
        self.effects = [effect for effect in self.effects if effect.turns > 0]

    def has_shield(self):
        for effect in self.effects:
            if effect.name == 'Shield':
                return True
        return False

    def get_actions(self):
        return self.actions
        global counter
        counter += 1
        if counter == 1:
            return [RECHARGE]
        elif counter == 2:
            return [SHIELD]
        elif counter == 3:
            return [DRAIN]
        elif counter == 4:
            return [POISON]
        elif counter == 5:
            return [MAGIC_MISSILE]
        else:
            exit()
            return self.actions

    def copy(self):
        effects_copy = [Effect(effect.name, effect.turns, effect.hp_effect, effect.mana_effect)
                        for effect in self.effects]
        return Player(self.name, self.hp, self.mana, self.actions, effects_copy)

    def __repr__(self):
        return f'{self.name} has {self.hp} hit points, {self.mana} mana'

    def __lt__(self, other):
        if self.name == 'Boss':
            return self.hp < other.hp
        else:
            return self.mana < other.mana


states = []
player_actions = [MAGIC_MISSILE, DRAIN, SHIELD, POISON, RECHARGE]
player = Player('Player', 50, 500, player_actions)
BOSS_HIT = Action('Hit', 0, 1, 0, 0, -10, 0)
boss = Player('Boss', 71, 0, [BOSS_HIT])

# player = Player('Player', 10, 250, player_actions)
# BOSS_HIT = Action('Hit', 0, 1, 0, 0, -8, 0)
# boss = Player('Boss', 14, 8, [BOSS_HIT])

heappush(states, (0, player, boss))
count = 0
part_2 = True
while len(states) > 0:
    mana_spent, player, boss = heappop(states)
    if player.hp <= 0 or player.mana <= 0:
        continue
    count += 1
    if count % 10000 == 0:
        print(mana_spent)

    # print(f'-- Player turn --')
    # print(f'- Player has {player.hp} hit points, 0 armor, {player.mana} mana')
    # print(f'- Boss has {boss.hp} hit points')

    # Players turs
    # get all possible actions
    actions = player.get_actions()

    for action in actions:

        player_copy = player.copy()
        boss_copy = boss.copy()

        if part_2:
            player_copy.hp -= 1
            if player_copy.hp <= 0:
                continue

        # check if action already is in effect
        if action.name in [effect.name for effect in player_copy.effects if effect.turns > 1]:
            continue

        # apply effects
        player_copy.apply_effects()
        boss_copy.apply_effects()

        # apply action
        player_copy.mana -= action.cost
        if player_copy.mana <= 0:
            continue
        player_copy.apply_action(action, boss_copy)
        mana_spent_copy = mana_spent + action.cost

        # print(f'Player casts {action.name}.\n')

        player_copy.apply_instant_effects()
        boss_copy.apply_instant_effects()

        # check if boss is dead
        if boss_copy.hp <= 0:
            print('Player wins!')
            print(f'Mana spent: {mana_spent_copy}')
            exit()

        # Boss turn
        # print(f'-- Boss turn --')
        # print(
        #    f'- Player has {player_copy.hp} hit points, {player_copy.mana} mana')
        # print(f'- Boss has {boss_copy.hp} hit points')
        # apply effects
        player_copy.apply_effects()
        boss_copy.apply_effects()

        # check if boss is dead
        if boss_copy.hp <= 0:
            print('Player wins!')
            print(f'Mana spent: {mana_spent_copy}')
            exit()

        boss.apply_action(boss.actions[0], player_copy)

        player_copy.apply_instant_effects()
        boss_copy.apply_instant_effects()

        if player_copy.has_shield():
            # print('Shield active')
            player_copy.hp += 7

        # check if player is dead
        if player_copy.hp <= 0:
            # print('Boss wins!')
            continue

        # check if boss is dead
        if boss_copy.hp <= 0:
            print('Player wins!')
            print(f'Mana spent: {mana_spent_copy}')
            exit()

        # add new state
        heappush(states, (mana_spent_copy, player_copy, boss_copy))

# 1027 too low
# 1482 too low
