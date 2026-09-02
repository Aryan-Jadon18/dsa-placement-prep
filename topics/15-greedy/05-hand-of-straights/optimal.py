# Sort distinct values once, greedily consume runs by count — Time: O(n log n), Space: O(n)
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        for value in sorted(counts):
            need = counts[value]
            if need == 0:
                continue
            for offset in range(groupSize):
                v = value + offset
                if counts.get(v, 0) < need:
                    return False
                counts[v] -= need
        return True


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
    print("expected False, got", sol.isNStraightHand([1, 2, 3, 4, 5], 4))
    print("expected True, got", sol.isNStraightHand([1, 2, 2, 3, 3, 4], 2))
