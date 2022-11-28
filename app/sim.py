from Fortuna import d

from app.monster_types import RandomMonster, MonsterQuery


def combat_turn(attacker: RandomMonster, defender: RandomMonster):
    att_roll = d(20) + attacker.attack_bonus
    if att_roll >= defender.armor_class:
        defender.heath.sub(attacker.damage())


def combat(unit_1, unit_2):
    # Todo: add initiative?
    # Todo: decide if ties are acceptable
    while unit_1 and unit_2:
        combat_turn(unit_1, unit_2)
        combat_turn(unit_2, unit_1)
    if unit_1:
        winner = unit_1.monster_name
    elif unit_2:
        winner = unit_2.monster_name
    else:
        winner = "tie"
    return winner


if __name__ == '__main__':
    # Todo: loop & collect results for model training
    u1 = RandomMonster(MonsterQuery())
    u2 = RandomMonster(MonsterQuery())
    print({
        "attacker": u1.monster_name,
        "defender": u2.monster_name,
        "winner": combat(u1, u2),
    })
