# Treat matrix as one virtual sorted 1D array, single binary search — Time: O(log(m*n)), Space: O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print("expected True, got", sol.searchMatrix(m, 3))
    print("expected False, got", sol.searchMatrix(m, 13))
    print("expected True, got", sol.searchMatrix([[1]], 1))
