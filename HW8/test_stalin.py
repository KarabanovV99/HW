import pytest
from HW8.stalin import stalin_sort


@pytest.mark.parametrize('input_list, expected_output', [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [5]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([1, 2, 1, 3, 2, 4, 3, 5], [1, 2, 3, 4, 5]),
    ([-5, -2, 0, 1, 5], [-5, -2, 0, 1, 5]),
    ([1, -2, 0, -5, 5], [1, 5]),
    ([1, 4, 2, 5, -3], [1, 4, 5]),
])


def test_stalin_sort(input_list, expected_output):
    assert stalin_sort(input_list) == expected_output
