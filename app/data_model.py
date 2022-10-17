"""
Monsters
    - Stats
        - Monster Type (Undead, Demon, Animal)
        - Level
        - Resistances (Fire, Frost, Lightning, Physical)
        - Armor
        - Damage (Elemental + regular)
        - Health Points
        - Health Regen Rate
        - Movement Speed
        - XP Reward (Meta)
    - Tier (Rank)
"""
from typing import Literal

from app.utilities import dice, d


class Monster:
    level: int
    damage_dice: int
    monster_type: str
    resistance: float
    armor: int
    health: int
    regen: float
    movement_speed: int
    xp_reward: int
    tier: Literal["Minion", "Monster", "Elite", "Legendary"]

    def damage(self):
        return dice(self.level, self.damage_dice)


class RandomMonster:
    monster_lookup = {
    }

    def __init__(self):
        self.level = d(100)
