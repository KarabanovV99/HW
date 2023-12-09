from collections import deque
from typing import Dict, List

def bfs(graph: Dict[str, List[str]], start: str, target: str) -> int | None:
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == target:
            return distance
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return None
