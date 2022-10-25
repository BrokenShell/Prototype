from Fortuna import QuantumMonty, FlexCat, TruffleShuffle


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
    "Royal Knight",  "Paladin",
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
    "0": QuantumMonty((10, 11, 12, 13)).middle_linear,
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


class ChallengeRating:

    def __init__(self, value):
        self.value = value


cr = ChallengeRating("1/4")
print(ac_by_cr[cr.value]())
