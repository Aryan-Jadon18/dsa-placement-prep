# Plain recursion, try +/- for every number — Time: O(2^n), Space: O(n)
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)

        def dfs(i: int, total: int) -> int:
            if i == n:
                return 1 if total == target else 0
            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print("expected 5, got", sol.findTargetSumWays([1, 1, 1, 1, 1], 3))
    print("expected 1, got", sol.findTargetSumWays([1], 1))
    print("expected 2, got", sol.findTargetSumWays([1, 0], 1))
