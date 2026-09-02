# Backtracking: try forming a group from any remaining card — Time: O((n/groupSize)!), Space: O(n)
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)

        def backtrack() -> bool:
            if not counts:
                return True
            for start in sorted(counts):  # try any remaining value as a group start
                ok = True
                for offset in range(groupSize):
                    v = start + offset
                    if counts.get(v, 0) <= 0:
                        ok = False
                        break
                if not ok:
                    continue
                for offset in range(groupSize):
                    v = start + offset
                    counts[v] -= 1
                    if counts[v] == 0:
                        del counts[v]
                if backtrack():
                    return True
                for offset in range(groupSize):  # undo and try the next start
                    v = start + offset
                    counts[v] = counts.get(v, 0) + 1
            return False

        return backtrack()


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
    print("expected False, got", sol.isNStraightHand([1, 2, 3, 4, 5], 4))
    print("expected True, got", sol.isNStraightHand([1, 2, 2, 3, 3, 4], 2))
