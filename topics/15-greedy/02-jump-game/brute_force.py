# Plain recursion/backtracking over all jump choices — Time: O(2^n), Space: O(n)
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        def dfs(i: int) -> bool:
            if i >= n - 1:
                return True
            for step in range(1, nums[i] + 1):
                if dfs(i + step):
                    return True
            return False

        return dfs(0)


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.canJump([2, 3, 1, 1, 4]))
    print("expected False, got", sol.canJump([3, 2, 1, 0, 4]))
    print("expected True, got", sol.canJump([0]))
