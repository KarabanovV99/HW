import pytest
from HW8.quick import quick_sort

@pytest.mark.parametrize('input_list, expected_output', [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([-5, -2, 0, 1, 5], [-5, -2, 0, 1, 5]),
    ([1, -2, 0, -5, 5], [-5, -2, 0, 1, 5]),
    ([1, 4, 2, 5, -3], [-3, 1, 2, 4, 5]),
])


def test_quick_sort(input_list, expected_output):
    assert quick_sort(input_list) == expected_output
