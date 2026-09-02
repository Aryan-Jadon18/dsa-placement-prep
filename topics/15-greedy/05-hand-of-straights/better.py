# Min-heap re-fetches the current minimum each round — Time: O(n log n), Space: O(n)
import heapq
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        heap = list(counts.keys())
        heapq.heapify(heap)

        while heap:
            while heap and counts[heap[0]] == 0:
                heapq.heappop(heap)
            if not heap:
                break
            start = heap[0]
            for offset in range(groupSize):
                v = start + offset
                if counts.get(v, 0) == 0:
                    return False
                counts[v] -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
    print("expected False, got", sol.isNStraightHand([1, 2, 3, 4, 5], 4))
    print("expected True, got", sol.isNStraightHand([1, 2, 2, 3, 3, 4], 2))
