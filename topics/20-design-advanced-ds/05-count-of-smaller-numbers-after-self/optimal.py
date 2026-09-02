# Fenwick Tree (BIT) + coordinate compression, processed right to left — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        # coordinate compression: map each distinct value to a small rank
        sorted_vals = sorted(set(nums))
        rank = {val: i + 1 for i, val in enumerate(sorted_vals)}  # 1-indexed for the Fenwick tree
        size = len(sorted_vals)

        tree = [0] * (size + 1)

        def add(i: int) -> None:
            while i <= size:
                tree[i] += 1
                i += i & (-i)

        def prefix_count(i: int) -> int:
            # count of seen values with rank <= i
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & (-i)
            return total

        counts = [0] * n
        for idx in range(n - 1, -1, -1):
            r = rank[nums[idx]]
            counts[idx] = prefix_count(r - 1)  # strictly smaller: ranks 1..r-1
            add(r)

        return counts


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [2,1,1,0], Got:", sol.countSmaller([5, 2, 6, 1]))
    print("Expected: [0], Got:", sol.countSmaller([-1]))
    print("Expected: [0,0], Got:", sol.countSmaller([-1, -1]))
