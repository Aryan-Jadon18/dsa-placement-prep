# Sort + fix one element + two pointers, skipping duplicates — Time: O(n^2), Space: O(1) extra
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []

        for i in range(n - 2):
            if nums[i] > 0:
                break  # smallest element positive => no triplet can sum to 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate first element

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.threeSum([-1, 0, 1, 2, -1, -4])))
    print("expected [], got", sol.threeSum([0, 1, 1]))
    print("expected [[0, 0, 0]], got", sol.threeSum([0, 0, 0]))
