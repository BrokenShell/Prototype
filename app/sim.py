from Fortuna import d
from pandas import DataFrame

from app.monster_types import RandomMonster, MonsterQuery


def combat_turn(attacker: RandomMonster, defender: RandomMonster):
    att_roll = d(20) + attacker.attack_bonus
    if att_roll >= defender.armor_class:
        defender.health.sub(attacker.damage())


def initiative(attacker, defender):
    a_roll, b_roll = d(20), d(20)
    if a_roll > b_roll:
        return attacker, defender
    elif b_roll > a_roll:
        return defender, attacker
    else:
        return initiative(attacker, defender)


def combat(unit_1, unit_2):
    attacker, defender = initiative(unit_1, unit_2)

    while attacker and defender:
        combat_turn(attacker, defender)
        if defender:
            combat_turn(defender, attacker)

    if unit_1:
        winner = unit_1.monster_name
    else:
        winner = unit_2.monster_name

    return winner


if __name__ == '__main__':
    data = []
    for _ in range(1000):
        u1 = RandomMonster(MonsterQuery(challenge_rating=10))
        u2 = RandomMonster(MonsterQuery(challenge_rating=10))
        data.append({
            "attacker": u1.monster_name,
            "defender": u2.monster_name,
            "winner": combat(u1, u2),
        })
    df = DataFrame(data)
    print(df.head())
