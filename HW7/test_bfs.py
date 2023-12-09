import pytest
from HW7.bfs import bfs


def yourcodehere(node, target):
    if node == target:
        return True
    else:
        return False
    
@pytest.mark.parametrize("graph, start, target, expected", [
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'A', 0),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'B', 1),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'C', 1),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'D', 2),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'E', 2),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'F', 2),
    ({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}, 'A', 'G', None),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'A', 'D', 2),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'B', 'E', 2),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'C', 'D', 1),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'D', 'E', 1),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'E', 'A', 1),
    ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'A', 'F', None),
    ({}, "A", "F", None)
])
def test_bfs(graph, start, target, expected):
    assert bfs(graph, start, target, yourcodehere) == expected
