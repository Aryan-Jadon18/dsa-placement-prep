# Binary search for the row, then linear scan the row — Time: O(log m + n), Space: O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        low, high = 0, m - 1
        candidate_row = -1
        while low <= high:
            mid = (low + high) // 2
            row = matrix[mid]
            if row[0] <= target <= row[-1]:
                candidate_row = mid
                break
            elif target < row[0]:
                high = mid - 1
            else:
                low = mid + 1

        if candidate_row == -1:
            return False
        return target in matrix[candidate_row]


if __name__ == "__main__":
    sol = Solution()
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print("expected True, got", sol.searchMatrix(m, 3))
    print("expected False, got", sol.searchMatrix(m, 13))
    print("expected True, got", sol.searchMatrix([[1]], 1))
