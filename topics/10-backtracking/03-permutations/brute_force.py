# Filter remaining elements from scratch at every step — Time: O(n! * n^2), Space: O(n! * n)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(remaining, path):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                # Rebuild the "remaining" list by filtering out index i each time.
                next_remaining = remaining[:i] + remaining[i + 1:]
                dfs(next_remaining, path + [remaining[i]])

        dfs(nums, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    r1 = sorted(sol.permute([1, 2, 3]))
    print("expected 6 perms, got", len(r1), r1)

    r2 = sorted(sol.permute([0, 1]))
    print("expected [[0, 1], [1, 0]], got", r2)

    r3 = sol.permute([1])
    print("expected [[1]], got", r3)
