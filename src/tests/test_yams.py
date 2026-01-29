import pytest

from src.figure import Figure
from src.yams import score_chance, is_brelan, is_square, is_yams, is_full, is_straight, best_figure, score_game


@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1, 2, 3, 4, 5], 15),
        ([6, 6, 6, 6, 6], 30),
        ([1, 1, 1, 2, 2], 7),
    ]
)
def test_chance_score(dice, expected):
    assert score_chance(dice) == expected


@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1, 1, 1, 2, 3], True),
        ([2, 2, 2, 5, 3], True),
        ([1, 1, 2, 2, 3], False),
    ]
)
def test_is_brelan(dice, expected):
    assert is_brelan(dice) is expected


@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1, 1, 1, 2, 1], True),
        ([2, 2, 2, 2, 3], True),
        ([1, 1, 2, 2, 3], False),
    ]
)
def test_is_square(dice, expected):
    assert is_square(dice) is expected


@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1, 1, 1, 1, 1], True),
        ([2, 2, 2, 2, 2], True),
        ([1, 1, 2, 2, 3], False),
    ]
)
def test_is_yams(dice, expected):
    assert is_yams(dice) is expected


@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1, 1, 1, 2, 2], True),
        ([2, 2, 4, 2, 4], True),
        ([1, 1, 2, 2, 3], False),
    ]
)
def test_is_full(dice, expected):
    assert is_full(dice) is expected


@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1, 2, 3, 4, 5], True),
        ([2, 3, 4, 5, 6], True),
        ([1, 2, 3, 4, 6], False),
    ]
)
def test_is_straight(dice, expected):
    assert is_straight(dice) is expected


@pytest.mark.parametrize(
    "dice, available, expected",
    [
        ([1, 1, 1, 1, 1], {Figure.YAMS, Figure.SQUARE, Figure.BRELAN}, Figure.YAMS),
        ([2, 3, 4, 5, 6], {Figure.YAMS, Figure.SQUARE, Figure.STRAIGHT}, Figure.STRAIGHT),
        ([1, 2, 3, 4, 6], {Figure.YAMS, Figure.CHANCE, Figure.STRAIGHT}, Figure.CHANCE),
    ]
)
def test_best_figure_priority_yams(dice, available, expected):
    assert best_figure(dice, available) == expected


@pytest.mark.parametrize(
    "roll, expected",
    [
        ([1, 1, 1, 1, 1], 50),
        ([2, 3, 4, 5, 6], 40),
        ([4, 4, 4, 4, 2], 35),
        ([1, 1, 1, 2, 2], 30),
        ([3, 3, 3, 4, 5], 28),
        ([1, 2, 3, 4, 6], sum([1, 2, 3, 4, 6])),
    ]
)
def test_score_game_single_roll(roll, expected):
    assert score_game([roll]) == expected


@pytest.mark.parametrize(
    "rolls, expected",
    [
        [1, 1, 1, 2, 2],
        [4, 4, 4, 4, 2],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 3, 4],
        [1, 2, 3, 4, 6],
    ], 30 + 35 + 40 + 50 + 28 + 16
)
def test_score_game_multiple_rolls(rolls, expected):
    assert score_game(rolls) == expected
