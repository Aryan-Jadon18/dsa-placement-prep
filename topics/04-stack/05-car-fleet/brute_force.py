# Unmemoized recursion recomputed per car (O(n) chain from each of n starts) — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed))  # ascending by position; last = nearest target
        solo = [(target - p) / s for p, s in cars]

        def arrival(i: int) -> float:
            # recomputes the whole chain ahead of i every single call — no caching
            if i == n - 1:
                return solo[i]
            next_arrival = arrival(i + 1)
            return next_arrival if solo[i] <= next_arrival else solo[i]

        fleets = 0
        for i in range(n):
            is_leader = (i == n - 1) or (solo[i] > arrival(i + 1))
            if is_leader:
                fleets += 1
        return fleets


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print("expected 1, got", sol.carFleet(10, [3], [3]))
    print("expected 1, got", sol.carFleet(100, [0, 2, 4], [4, 2, 1]))
