# Sweep line: separate sorted starts/ends, two pointers — Time: O(n log n), Space: O(n)
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        starts = sorted(iv[0] for iv in intervals)
        ends = sorted(iv[1] for iv in intervals)

        s_ptr = e_ptr = 0
        in_use = 0
        max_rooms = 0
        n = len(intervals)

        while s_ptr < n:
            if starts[s_ptr] < ends[e_ptr]:
                in_use += 1
                max_rooms = max(max_rooms, in_use)
                s_ptr += 1
            else:
                in_use -= 1
                e_ptr += 1

        return max_rooms


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 2, Got:", sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print("Expected: 1, Got:", sol.minMeetingRooms([[7, 10], [2, 4]]))
    print("Expected: 3, Got:", sol.minMeetingRooms([[1, 5], [1, 5], [1, 5]]))
