from collections import Counter

from src.figure import Figure


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


def is_full(dice: list[int]) -> bool:
    counts = sorted(Counter(dice).values())
    return counts == [2, 3]


def is_straight(dice: list[int]) -> bool:
    return sorted(dice) in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])


def best_figure(dice: list[int], available: set[Figure]) -> Figure:
    if Figure.YAMS in available and is_yams(dice):
        return Figure.YAMS

    if Figure.STRAIGHT in available and is_straight(dice):
        return Figure.STRAIGHT

    if Figure.SQUARE in available and is_square(dice):
        return Figure.SQUARE

    if Figure.FULL in available and is_full(dice):
        return Figure.FULL

    if Figure.BRELAN in available and is_brelan(dice):
        return Figure.BRELAN

    return Figure.CHANCE


def score_game(rolls: list[list[int]]) -> int:
    available_figures = set(Figure)
    total = 0

    for roll in rolls:
        figure = best_figure(roll, available_figures)
        if figure is Figure.CHANCE:
            total += score_chance(roll)
        else:
            total += figure.value
            available_figures.discard(figure)

    return total
