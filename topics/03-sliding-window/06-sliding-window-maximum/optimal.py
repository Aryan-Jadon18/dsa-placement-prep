# Monotonic decreasing deque of indices — Time: O(n), Space: O(k)
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # indices, values strictly decreasing front-to-back
        result = []
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected [3,3,5,5,6,7], got", sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("expected [1], got", sol.maxSlidingWindow([1], 1))
    print("expected [11], got", sol.maxSlidingWindow([9, 11], 2))
