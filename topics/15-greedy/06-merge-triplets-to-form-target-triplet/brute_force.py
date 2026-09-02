# Try every subset of triplets, merge and compare — Time: O(2^n * n), Space: O(n)
from itertools import combinations


class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        n = len(triplets)
        for size in range(1, n + 1):
            for combo in combinations(triplets, size):
                merged = [0, 0, 0]
                for t in combo:
                    for k in range(3):
                        merged[k] = max(merged[k], t[k])
                if merged == target:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))
    print("expected False, got", sol.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]))
    print("expected True, got", sol.mergeTriplets([[1, 2, 3]], [1, 2, 3]))
