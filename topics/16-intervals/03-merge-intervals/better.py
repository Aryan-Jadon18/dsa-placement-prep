# Sort, then check new interval against every merged interval so far — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ordered = sorted(intervals, key=lambda iv: iv[0])
        result: List[List[int]] = []

        for iv in ordered:
            merged_into_existing = False
            for existing in result:
                if iv[0] <= existing[1] and existing[0] <= iv[1]:
                    existing[0] = min(existing[0], iv[0])
                    existing[1] = max(existing[1], iv[1])
                    merged_into_existing = True
                    break
            if not merged_into_existing:
                result.append(iv[:])

        return sorted(result, key=lambda iv: iv[0])


if __name__ == "__main__":
    sol = Solution()
    print("Expected: [[1,6],[8,10],[15,18]], Got:",
          sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print("Expected: [[1,5]], Got:", sol.merge([[1, 4], [4, 5]]))
    print("Expected: [[0,4]], Got:", sol.merge([[1, 4], [0, 4]]))
