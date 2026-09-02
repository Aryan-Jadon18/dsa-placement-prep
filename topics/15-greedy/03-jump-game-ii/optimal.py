# Greedy BFS-by-levels — Time: O(n), Space: O(1)
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.jump([2, 3, 1, 1, 4]))
    print("expected 2, got", sol.jump([2, 3, 0, 1, 4]))
    print("expected 0, got", sol.jump([0]))
