from collections import deque
from typing import Callable, Any


def bfs(graph: dict[Any, list], start, target, function: Callable[Any, Any]) -> int | None:
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()
        if function(node, target):
            return distance
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return None
