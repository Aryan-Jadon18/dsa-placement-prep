# Try every subarray directly — Time: O(n^2), Space: O(1)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        for start in range(len(nums)):
            running = 0
            for end in range(start, len(nums)):
                running += nums[end]
                best = max(best, running)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("expected 1, got", sol.maxSubArray([1]))
    print("expected -1, got", sol.maxSubArray([-3, -1, -2]))
