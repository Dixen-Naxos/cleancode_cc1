import pytest
from src.yams import score_chance, is_brelan, is_square


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
        ([2, 2, 2, 2, 3], True),
        ([1, 1, 2, 2, 3], False),
    ]
)
def test_is_brelan(dice, expected):
    assert is_brelan(dice) is expected

@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1, 1, 1, 2, 3], True),
        ([2, 2, 2, 2, 3], True),
        ([1, 1, 2, 2, 3], False),
    ]
)
def test_is_square(dice, expected):
    assert is_square(dice) is expected
