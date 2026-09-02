# Kadane's algorithm, single rolling sum — Time: O(n), Space: O(1)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = current = nums[0]
        for num in nums[1:]:
            current = num + max(0, current)
            best = max(best, current)
        return best


if __name__ == "__main__":
    sol = Solution()
    print("expected 6, got", sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("expected 1, got", sol.maxSubArray([1]))
    print("expected -1, got", sol.maxSubArray([-3, -1, -2]))
