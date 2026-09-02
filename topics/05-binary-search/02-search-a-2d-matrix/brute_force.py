# Scan every cell — Time: O(m*n), Space: O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for val in row:
                if val == target:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print("expected True, got", sol.searchMatrix(m, 3))
    print("expected False, got", sol.searchMatrix(m, 13))
    print("expected True, got", sol.searchMatrix([[1]], 1))
