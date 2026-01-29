from collections import Counter


def score_chance(dice: list[int]) -> int:
    return sum(dice)


def is_brelan(dice: list[int]) -> bool:
    counts = Counter(dice)
    return 3 in counts.values()

def is_square(dice: list[int]) -> bool:
    counts = Counter(dice)
    return 4 in counts.values()

def is_yams(dice: list[int]) -> bool:
    counts = Counter(dice)
    return 5 in counts.values()
