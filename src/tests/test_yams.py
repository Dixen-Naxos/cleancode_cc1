import pytest
from src.yams import score_chance

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
