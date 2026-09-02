# Sort in place, single pass with early exit — Time: O(n log n), Space: O(1)
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda iv: iv[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print("Expected: False, Got:", sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
    print("Expected: True, Got:", sol.canAttendMeetings([[7, 10], [2, 4]]))
    print("Expected: True, Got:", sol.canAttendMeetings([[1, 5], [5, 10]]))
    print("Expected: True, Got:", sol.canAttendMeetings([]))
