# 1D DP: max sum ending at each index, stored explicitly — Time: O(n), Space: O(n)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        best_ending_here = [0] * n
        best_ending_here[0] = nums[0]
        for i in range(1, n):
            best_ending_here[i] = nums[i] + max(0, best_ending_here[i - 1])
        return max(best_ending_here)


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("expected 1, got", sol.maxSubArray([1]))
    print("expected -1, got", sol.maxSubArray([-3, -1, -2]))
