# Simulate slot by slot, greedily pick most-frequent available task — Time: O(total_slots * 26), Space: O(26)
from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        cooldown_until = {}  # task -> earliest slot it can run again
        remaining = dict(counts)

        time = 0
        total_remaining = len(tasks)
        while total_remaining > 0:
            # pick the available task (cooldown expired) with highest remaining count
            best = None
            best_count = -1
            for t, cnt in remaining.items():
                if cnt > 0 and cooldown_until.get(t, 0) <= time and cnt > best_count:
                    best = t
                    best_count = cnt

            if best is not None:
                remaining[best] -= 1
                cooldown_until[best] = time + n + 1
                total_remaining -= 1

            time += 1

        return time


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 8  Actual:", sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
    print("Expected: 6  Actual:", sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
    print("Expected: 16  Actual:", sol.leastInterval(
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
