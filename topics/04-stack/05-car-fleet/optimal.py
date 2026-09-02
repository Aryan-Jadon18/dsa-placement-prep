# Sort by position descending, explicit stack of fleet arrival times — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # nearest target first
        stack = []  # arrival times of confirmed fleets
        for pos, spd in cars:
            solo_time = (target - pos) / spd
            if not stack or solo_time > stack[-1]:
                stack.append(solo_time)
            # else solo_time <= stack[-1]: merges into the fleet ahead, stack unchanged
        return len(stack)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print("expected 1, got", sol.carFleet(10, [3], [3]))
    print("expected 1, got", sol.carFleet(100, [0, 2, 4], [4, 2, 1]))
