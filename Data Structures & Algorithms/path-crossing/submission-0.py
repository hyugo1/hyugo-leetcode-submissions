class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set()
        x, y = 0, 0
        direction = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0]
        }
        for p in path:
            visit.add((x, y))
            dx, dy = direction[p]
            x, y = x + dx, y + dy
            if (x, y) in visit:
                return True
        return False
