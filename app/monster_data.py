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
