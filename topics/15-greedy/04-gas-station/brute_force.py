# Simulate the full loop from every candidate start — Time: O(n^2), Space: O(1)
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        for start in range(n):
            tank = 0
            completed = True
            for step in range(n):
                i = (start + step) % n
                tank += gas[i] - cost[i]
                if tank < 0:
                    completed = False
                    break
            if completed:
                return start
        return -1


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print("expected -1, got", sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
    print("expected 4, got", sol.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))
