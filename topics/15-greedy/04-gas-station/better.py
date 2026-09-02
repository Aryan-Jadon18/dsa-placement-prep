# Explicit prefix-balance array, start after its minimum — Time: O(n), Space: O(n)
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        prefix = [0] * n
        running = 0
        for i in range(n):
            running += gas[i] - cost[i]
            prefix[i] = running

        min_index = min(range(n), key=lambda i: prefix[i])
        return (min_index + 1) % n


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print("expected -1, got", sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
    print("expected 4, got", sol.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))
