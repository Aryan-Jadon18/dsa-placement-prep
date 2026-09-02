# Repeatedly merge any overlapping pair until stable — Time: O(n^3), Space: O(n)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        current = [iv[:] for iv in intervals]
        changed = True
        while changed:
            changed = False
            for i in range(len(current)):
                for j in range(i + 1, len(current)):
                    a, b = current[i], current[j]
                    if a[0] <= b[1] and b[0] <= a[1]:  # overlap or touch
                        merged_iv = [min(a[0], b[0]), max(a[1], b[1])]
                        current = [current[k] for k in range(len(current)) if k != i and k != j]
                        current.append(merged_iv)
                        changed = True
                        break
                if changed:
                    break
        return sorted(current, key=lambda iv: iv[0])


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [[1,6],[8,10],[15,18]], Got:",
          sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print("Expected: [[1,5]], Got:", sol.merge([[1, 4], [4, 5]]))
    print("Expected: [[0,4]], Got:", sol.merge([[1, 4], [0, 4]]))
