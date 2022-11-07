from Fortuna import QuantumMonty, FlexCat, TruffleShuffle
from pandas import DataFrame

elements = (
    "Air", "Water", "Earth", "Fire",
    "Smoke", "Frost", "Shadow", "Molten",
)

dragon_colors = (
    "Green", "Blue", "White", "Black", "Red", "Shadow",
    "Silver", "Bronze", "Gold", "Electrum", "Platinum", "Mithril",
)

dice_by_type = FlexCat({
    "Humanoid": (4, 8, 12),
    "Beast": (4, 8, 12),
    "Construct": (4, 8, 12),
    "Giant": (8, 12, 20),
    "Elemental": (8, 12, 20),
    "Undead": (12, 8, 20, 4),
    "Fiend": (12, 8, 20, 4),
    "Aberration": (12, 20, 8, 4),
    "Dragon": (20, 12, 8, 4),
    "Mythical Beast": (20, 12, 8, 4),
}, key_bias="front_linear", val_bias="front_linear")

common_humanoids = TruffleShuffle((
    "Carleton", "Carny", "Merchant",
    "Thug", "Grave Robber", "Cut Throat",
    "Thief", "Archer", "Hunter",
    "Barbarian", "Cavalier", "Gladiator",
    "Druid", "Sorcerer", "Shaman",
))

rare_humanoids = TruffleShuffle((
    "Assassin", "Ninja", "Monk",
    "Mage", "Magician", "Wizard",
    "Summoner", "Warlock", "Necromancer",
    "Royal Knight", "Paladin",
    "Exorcist", "Cleric", "Priest",
))

epic_humanoid = QuantumMonty((
    "Champion", "Royal Guard",
    "Arch Mage", "Inquisitor",
    "Royal Captain", "Black Knight",
    "Executioner", "Blood Queen",
)).front_linear

name_by_type = FlexCat({
    "Humanoid": (common_humanoids, rare_humanoids, epic_humanoid),
    "Beast": ("Lion", "Tiger", "Bear", "Hyena", "Wolf", "Fox"),
    "Construct": ("Animated Book", "Flying Broom", "Gnome Mech"),
    "Giant": ("Cave Troll", "Hill Giant", "Frost Giant", "Flame Giant", "Storm Giant"),
    "Elemental": (f"{element} Elemental" for element in elements),
    "Undead": ("Skeleton", "Zombie", "Ghost", "Vampire", "Lich"),
    "Fiend": ("Imp", "Succubus", "Winged Demon", "Balrog"),
    "Aberration": ("Intellect Devour", "Mind Flayer", "Hive Mind"),
    "Dragon": (f"{color} Dragon" for color in dragon_colors),
    "Mythical Beast": ("Pixie", "Dryad", "Fey", "Pegasus", "Manticore", "Unicorn"),
}, key_bias="front_linear", val_bias="front_linear")

ac_by_cr = {
    "1/16": QuantumMonty((10, 11, 12, 13)).middle_linear,
    "1/8": QuantumMonty((10, 11, 12, 13)).middle_linear,
    "1/4": QuantumMonty((11, 12, 13, 14)).middle_linear,
    "1/2": QuantumMonty((11, 12, 13, 14)).middle_linear,
    "1": QuantumMonty((12, 13, 14, 15)).middle_linear,
    "2": QuantumMonty((12, 13, 14, 15)).middle_linear,
    "3": QuantumMonty((12, 13, 14, 15)).middle_linear,
    "4": QuantumMonty((12, 13, 14, 15)).middle_linear,
    "5": QuantumMonty((13, 14, 15, 16)).middle_linear,
    "6": QuantumMonty((13, 14, 15, 16)).middle_linear,
    "7": QuantumMonty((14, 15, 16, 17)).middle_linear,
    "8": QuantumMonty((14, 15, 16, 17)).middle_linear,
    "9": QuantumMonty((15, 16, 17, 19)).middle_linear,
    "10": QuantumMonty((15, 16, 17, 19)).middle_linear,
    "11": QuantumMonty((15, 16, 17, 19)).middle_linear,
    "12": QuantumMonty((15, 16, 17, 19)).middle_linear,
    "13": QuantumMonty((15, 16, 17, 19)).middle_linear,
    "14": QuantumMonty((16, 17, 18, 19)).middle_linear,
    "15": QuantumMonty((16, 17, 18, 19)).middle_linear,
    "16": QuantumMonty((16, 17, 18, 19)).middle_linear,
    "17": QuantumMonty((17, 18, 19, 20)).middle_linear,
    "18": QuantumMonty((17, 18, 19, 20)).middle_linear,
    "19": QuantumMonty((17, 18, 19, 20)).middle_linear,
    "20": QuantumMonty((17, 18, 19, 20)).middle_linear,
    "21": QuantumMonty((18, 19, 20, 21)).middle_linear,
    "22": QuantumMonty((18, 19, 20, 21)).middle_linear,
    "23": QuantumMonty((18, 19, 20, 21)).middle_linear,
    "24": QuantumMonty((18, 19, 20, 21)).middle_linear,
    "25": QuantumMonty((19, 20, 21, 22)).middle_linear,
    "26": QuantumMonty((19, 20, 21, 22)).middle_linear,
    "27": QuantumMonty((19, 20, 21, 22)).middle_linear,
    "28": QuantumMonty((19, 20, 21, 22)).middle_linear,
    "29": QuantumMonty((20, 21, 22, 23)).middle_linear,
    "30": QuantumMonty((21, 22, 23, 24)).middle_linear,
}

stats_by_cr = [
    {"CR": "1/16", "Armor": (10, 11, 12, 13), "Save DC": (10, 11, 12, 13), "Attack": (0, 1, 2), "Proficiency": 2},
    {"CR": "1/8", "Armor": (10, 11, 12, 13), "Save DC": (10, 11, 12, 13), "Attack": (2, 3, 4), "Proficiency": 2},
    {"CR": "1/4", "Armor": (11, 12, 13, 14), "Save DC": (11, 12, 13, 14), "Attack": (2, 3, 4), "Proficiency": 2},
    {"CR": "1/2", "Armor": (11, 12, 13, 14), "Save DC": (11, 12, 13, 14), "Attack": (3, 4, 5), "Proficiency": 2},
    {"CR": "1", "Armor": (12, 13, 14, 15), "Save DC": (12, 13, 14, 15), "Attack": (3, 4, 5), "Proficiency": 2},
    {"CR": "2", "Armor": (12, 13, 14, 15), "Save DC": (12, 13, 14, 15), "Attack": (4, 5, 6), "Proficiency": 2},
    {"CR": "3", "Armor": (12, 13, 14, 15), "Save DC": (12, 13, 14, 15), "Attack": (4, 5, 6), "Proficiency": 2},
    {"CR": "4", "Armor": (12, 13, 14, 15), "Save DC": (12, 13, 14, 15), "Attack": (5, 6, 7), "Proficiency": 2},
    {"CR": "5", "Armor": (13, 14, 15, 16), "Save DC": (13, 14, 15, 16), "Attack": (5, 6, 7), "Proficiency": 3},
    {"CR": "6", "Armor": (13, 14, 15, 16), "Save DC": (13, 14, 15, 16), "Attack": (6, 7, 8), "Proficiency": 3},
    {"CR": "7", "Armor": (14, 15, 16, 17), "Save DC": (14, 15, 16, 17), "Attack": (6, 7, 8), "Proficiency": 3},
    {"CR": "8", "Armor": (14, 15, 16, 17), "Save DC": (14, 15, 16, 17), "Attack": (7, 8, 9), "Proficiency": 3},
    {"CR": "9", "Armor": (15, 16, 17, 19), "Save DC": (15, 16, 17, 19), "Attack": (7, 8, 9), "Proficiency": 4},
    {"CR": "10", "Armor": (15, 16, 17, 19), "Save DC": (15, 16, 17, 19), "Attack": (8, 9, 10), "Proficiency": 4},
    {"CR": "11", "Armor": (15, 16, 17, 19), "Save DC": (15, 16, 17, 19), "Attack": (8, 9, 10), "Proficiency": 4},
    {"CR": "12", "Armor": (15, 16, 17, 19), "Save DC": (15, 16, 17, 19), "Attack": (9, 10, 11), "Proficiency": 4},
    {"CR": "13", "Armor": (15, 16, 17, 19), "Save DC": (15, 16, 17, 19), "Attack": (10, 11, 12), "Proficiency": 5},
    {"CR": "14", "Armor": (16, 17, 18, 19), "Save DC": (16, 17, 18, 19), "Attack": (10, 11, 12), "Proficiency": 5},
    {"CR": "15", "Armor": (16, 17, 18, 19), "Save DC": (16, 17, 18, 19), "Attack": (11, 12, 13), "Proficiency": 5},
    {"CR": "16", "Armor": (16, 17, 18, 19), "Save DC": (16, 17, 18, 19), "Attack": (11, 12, 13), "Proficiency": 5},
    {"CR": "17", "Armor": (17, 18, 19, 20), "Save DC": (17, 18, 19, 20), "Attack": (12, 13, 14), "Proficiency": 6},
    {"CR": "18", "Armor": (17, 18, 19, 20), "Save DC": (17, 18, 19, 20), "Attack": (12, 13, 14), "Proficiency": 6},
    {"CR": "19", "Armor": (17, 18, 19, 20), "Save DC": (17, 18, 19, 20), "Attack": (13, 14, 15), "Proficiency": 6},
    {"CR": "20", "Armor": (17, 18, 19, 20), "Save DC": (17, 18, 19, 20), "Attack": (13, 14, 15), "Proficiency": 6},
    {"CR": "21", "Armor": (18, 19, 20, 21), "Save DC": (18, 19, 20, 21), "Attack": (14, 15, 16), "Proficiency": 7},
    {"CR": "22", "Armor": (18, 19, 20, 21), "Save DC": (18, 19, 20, 21), "Attack": (14, 15, 16), "Proficiency": 7},
    {"CR": "23", "Armor": (18, 19, 20, 21), "Save DC": (18, 19, 20, 21), "Attack": (15, 16, 17), "Proficiency": 7},
    {"CR": "24", "Armor": (18, 19, 20, 21), "Save DC": (18, 19, 20, 21), "Attack": (15, 16, 17), "Proficiency": 7},
    {"CR": "25", "Armor": (19, 20, 21, 22), "Save DC": (19, 20, 21, 22), "Attack": (16, 17, 18), "Proficiency": 8},
    {"CR": "26", "Armor": (19, 20, 21, 22), "Save DC": (19, 20, 21, 22), "Attack": (16, 17, 18), "Proficiency": 8},
    {"CR": "27", "Armor": (19, 20, 21, 22), "Save DC": (19, 20, 21, 22), "Attack": (17, 18, 19), "Proficiency": 8},
    {"CR": "28", "Armor": (19, 20, 21, 22), "Save DC": (19, 20, 21, 22), "Attack": (17, 18, 19), "Proficiency": 8},
    {"CR": "29", "Armor": (20, 21, 22, 23), "Save DC": (20, 21, 22, 23), "Attack": (18, 19, 20), "Proficiency": 9},
    {"CR": "30", "Armor": (21, 22, 23, 24), "Save DC": (21, 22, 23, 24), "Attack": (18, 19, 20), "Proficiency": 10},
]


def resolve(cr_index):
    stats_obj = stats_by_cr[cr_index]
    cr = stats_obj["CR"]
    ac = QuantumMonty(stats_obj["Armor Class"]).middle_linear()
    att = QuantumMonty(stats_obj["Attack Bonus"]).middle_linear()
    prof = stats_obj["Proficiency Bonus"]
    return f"Monster({cr=}, {ac=}, {att=}, {prof=})"


if __name__ == '__main__':
    DataFrame(stats_by_cr).to_csv("monster_stats.csv", index=False)
