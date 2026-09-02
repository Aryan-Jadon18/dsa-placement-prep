# Linear scan over t + BFS reachability check — Time: O(n^4), Space: O(n^2)
from collections import deque
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def reachable(t: int) -> bool:
            if grid[0][0] > t:
                return False
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            q = deque([(0, 0)])
            while q:
                r, c = q.popleft()
                if (r, c) == (n - 1, n - 1):
                    return True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] <= t:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            return False

        for t in range(n * n):
            if reachable(t):
                return t
        return n * n - 1


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.swimInWater([[0, 2], [1, 3]]))
    grid2 = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    print("expected 16, got", sol.swimInWater(grid2))
    print("expected 0, got", sol.swimInWater([[0]]))
