import pytest
from HW7.bfs import bfs

    
@pytest.mark.parametrize("graph, start, target, expected, f", [
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'A', 0, lambda n, t: n == t),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'B', 1, lambda n, t: n == t),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'C', 1, lambda n, t: n == t),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'D', 2, lambda n, t: n == t),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'E', 2, lambda n, t: n == t),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'F', 2, lambda n, t: n == t),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'G', None, lambda n, t: n == t),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'A', 'D', 2, lambda n, t: n == t),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'B', 'E', 2, lambda n, t: n == t),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'C', 'D', 1, lambda n, t: n == t),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'D', 'E', 1, lambda n, t: n == t),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'E', 'A', 1, lambda n, t: n == t),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'A', 'F', None, lambda n, t: n == t),
    ({}, "A", "F", None, lambda n, t: n == t),
    ({0: [1, 2], 1: [0, 3, 4], 2: [0, 5, 6], 3: [1], 4: [1, 6], 5: [2], 6: [2, 4]}, 0, 0, 0, lambda n, t: n % 2 == t % 2),
    ({}, 0, 1, None, lambda n, t: n % 2 == t % 2),
    ({0: [1, 2], 1: [0, 3, 4], 2: [0, 5, 6], 3: [1], 4: [1, 6], 5: [2], 6: [2, 4]}, 0, 2, 1, lambda n, t: n % 3 == t % 3),
])
def test_bfs(graph, start, target, expected, f):
    assert bfs(graph, start, target, f) == expected
