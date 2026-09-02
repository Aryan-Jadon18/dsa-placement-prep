# Plain recursion, try every jump length — Time: O(2^n), Space: O(n)
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)

        def dfs(i: int) -> int:
            if i >= n - 1:
                return 0
            best = float("inf")
            for step in range(1, nums[i] + 1):
                best = min(best, 1 + dfs(i + step))
            return best

        return dfs(0)


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.jump([2, 3, 1, 1, 4]))
    print("expected 2, got", sol.jump([2, 3, 0, 1, 4]))
    print("expected 0, got", sol.jump([0]))
