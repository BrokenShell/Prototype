from random import randint


def d(sides: int) -> int:
    return randint(1, sides)


def dice(rolls: int, sides: int) -> int:
    return sum(d(sides) for _ in range(rolls))
