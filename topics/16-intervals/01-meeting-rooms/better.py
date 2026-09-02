# Sort then check consecutive pairs — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        ordered = sorted(intervals, key=lambda iv: iv[0])  # extra sorted copy
        pairs = list(zip(ordered, ordered[1:]))  # adjacent pairs, extra list
        for prev, cur in pairs:
            if cur[0] < prev[1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print("Expected: False, Got:", sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
    print("Expected: True, Got:", sol.canAttendMeetings([[7, 10], [2, 4]]))
    print("Expected: True, Got:", sol.canAttendMeetings([[1, 5], [5, 10]]))
