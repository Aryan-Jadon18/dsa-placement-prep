# Min-heap of room end times, sorted by start — Time: O(n log n), Space: O(n)
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        ordered = sorted(intervals, key=lambda iv: iv[0])
        room_end_heap: List[int] = []  # min-heap of currently-occupied rooms' end times

        for start, end in ordered:
            if room_end_heap and room_end_heap[0] <= start:
                heapq.heapreplace(room_end_heap, end)  # reuse the earliest-freeing room
            else:
                heapq.heappush(room_end_heap, end)  # need a brand new room

        return len(room_end_heap)


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 2, Got:", sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print("Expected: 1, Got:", sol.minMeetingRooms([[7, 10], [2, 4]]))
    print("Expected: 3, Got:", sol.minMeetingRooms([[1, 5], [1, 5], [1, 5]]))
