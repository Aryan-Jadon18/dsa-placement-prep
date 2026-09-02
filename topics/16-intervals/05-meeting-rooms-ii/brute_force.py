# Simulate rooms with a list of end times, linear scan per meeting — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        ordered = sorted(intervals, key=lambda iv: iv[0])
        room_ends: List[int] = []

        for start, end in ordered:
            reused = False
            for i in range(len(room_ends)):
                if room_ends[i] <= start:
                    room_ends[i] = end
                    reused = True
                    break
            if not reused:
                room_ends.append(end)

        return len(room_ends)


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 2, Got:", sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print("Expected: 1, Got:", sol.minMeetingRooms([[7, 10], [2, 4]]))
    print("Expected: 3, Got:", sol.minMeetingRooms([[1, 5], [1, 5], [1, 5]]))
