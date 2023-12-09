from collections import deque
from typing import Dict, List


def yourcodehere(node, target):
    return node == target

def bfs(graph: Dict[int, List[int]], start: int, target: int, function) -> int | None:
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


if __name__ == '__main__':
    print(bfs({0: [1, 4], 1: [77, 55], 4: [99, 666]}, 0, 666, yourcodehere))  # None
