import pytest
from HW5.BIPOISK import binary_search


@pytest.mark.parametrize("sequence, target, expected", [
    ([], 42, None),
    ([0], 0, 0),
    ([0], 1, None),
    ([-1, 0, 42], 0, 1),
    ([-42, 0, 42], 42, 2),
    ([-6, -5, -4, -3, -2, -1], -4, 2),
    ([1, 2, 3, 4, 5, 6], 4, 3),
    ([1, 2, 3, 4, 5, 6, 7], 4, 3),
    ([1, 2, 3, 4, 5], 7, None),
    ([1, 2, 3, 4, 5, 6], 7, None),
    ([42, 42, 42, 42, 42], 42, 0),
    ([-42, -42, -42, -42, -42], -42, 0),
    ([42, 42, 42, 42, 43], 43, 4),
    ([41, 42, 42, 42, 42], 41, 0),
    ([-2, -2, -1, 0, 1, 2, 2, 2], -1, 2),
    ([-2, -2, -1, 0, 1, 1, 2, 2], 1, 4),
    ([56, 230, 234, 747, 83274, 823573723], 823573723, 5),
    ([1, 2, 3, 4, 5], 3, 2),  # target is present in the middle of the sequence
    ([1, 2, 3, 4, 5], 6, None),  # target is not present in the sequence
    ([1, 2, 3, 3, 4, 5], 3, 2),  # target is present multiple times
    ([1, 2, 3, 4, 5], 1, 0),  # target is present at the beginning of the sequence
    ([1, 2, 3, 4, 5], 5, 4),  # target is present at the end of the sequence
    ([], 3, None)  # empty sequence
])
def test_binary_search(sequence, target, expected):
    assert binary_search(sequence, target) == expected
