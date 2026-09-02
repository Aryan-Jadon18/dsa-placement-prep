# Greedy single pass, reset start after any deficit — Time: O(n), Space: O(1)
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_tank = 0
        current_tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        return start if total_tank >= 0 else -1


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print("expected -1, got", sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
    print("expected 4, got", sol.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))
