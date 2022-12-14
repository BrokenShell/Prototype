from Fortuna import dice, distribution_range, front_poisson
from pydantic import BaseModel, constr, conint
from pydantic.schema import Optional, Literal

from app.monster_data import dice_by_type, name_by_type, resolve
from app.resources import Resource

ShortString = constr(min_length=3, max_length=64)
MonsterCR = conint(ge=1, le=30)
RandomCR = distribution_range(front_poisson, 1, 30)


MonsterType = Literal[
    "Undead", "Giant", "Fiend", "Aberration",
    "Construct", "Elemental", "Dragon",
    "Humanoid", "Beast", "Mythical Beast",
]


class MonsterQuery(BaseModel):
    monster_name: Optional[ShortString]
    monster_type: Optional[MonsterType]
    challenge_rating: Optional[MonsterCR]


class RandomMonster:

    def __init__(self, monster_query: MonsterQuery):
        monster_type = monster_query.monster_type or dice_by_type.random_cat()
        self.monster_name = monster_query.monster_name or name_by_type(monster_type)
        self.monster_type = monster_type
        self.challenge_rating = monster_query.challenge_rating or RandomCR()
        self.health_dice = dice_by_type(self.monster_type)
        self.damage_dice = dice_by_type(self.monster_type) // 2
        self.health = Resource(dice(self.challenge_rating, self.health_dice))
        ac, att = resolve(self.challenge_rating)
        self.damage_formula = f"{self.challenge_rating}d{self.damage_dice}+{att}"
        self.armor_class = ac
        self.attack_bonus = att

    def damage(self):
        return dice(self.challenge_rating, self.damage_dice)

    def __bool__(self):
        return bool(self.health)

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())


if __name__ == '__main__':
    m = RandomMonster(MonsterQuery())
    m.health.sub(10000)
    print(bool(m))
