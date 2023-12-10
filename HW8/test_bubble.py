import pytest
from HW8.bubble import bubble_sort


@pytest.mark.parametrize("input_list, expected_output", [
    ([3, 2, 1, 5, 4], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
    ([], []),
    ([1], [1]),
    ([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
    ([1, -2, 3, -4, 5], [-4, -2, 1, 3, 5]),
])


def test_bubble_sort(input_list, expected_output):
    assert bubble_sort(input_list) == expected_output
