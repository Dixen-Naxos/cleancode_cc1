from collections import Counter


def score_chance(dice: list[int]) -> int:
    return sum(dice)


def is_brelan(dice: list[int]) -> bool:
    counts = Counter(dice)
    return 3 in counts.values()
