# Sort by position descending, track current fleet's arrival time with a scalar — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # nearest target first
        fleets = 0
        current_fleet_time = 0.0
        for pos, spd in cars:
            solo_time = (target - pos) / spd
            if solo_time > current_fleet_time:
                fleets += 1
                current_fleet_time = solo_time
            # else: catches up to the fleet ahead, merges (time stays as current_fleet_time)
        return fleets


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print("expected 1, got", sol.carFleet(10, [3], [3]))
    print("expected 1, got", sol.carFleet(100, [0, 2, 4], [4, 2, 1]))
