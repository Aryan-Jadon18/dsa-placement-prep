# Pairwise overlap check — Time: O(n^2), Space: O(1)
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        for i in range(n):
            s1, e1 = intervals[i]
            for j in range(i + 1, n):
                s2, e2 = intervals[j]
                if s1 < e2 and s2 < e1:  # true overlap, touching endpoints are fine
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print("Expected: False, Got:", sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
    print("Expected: True, Got:", sol.canAttendMeetings([[7, 10], [2, 4]]))
    print("Expected: True, Got:", sol.canAttendMeetings([[1, 5], [5, 10]]))
