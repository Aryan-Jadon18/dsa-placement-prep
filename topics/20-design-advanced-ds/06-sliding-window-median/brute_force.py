# Sort each window from scratch — Time: O(n*k*log k), Space: O(k)
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        for i in range(len(nums) - k + 1):
            window = sorted(nums[i:i + k])
            if k % 2 == 1:
                result.append(float(window[k // 2]))
            else:
                result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0], Got:",
          sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("Expected: [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0], Got:",
          sol.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
    print("Expected: [1.5], Got:", sol.medianSlidingWindow([1, 2], 2))
