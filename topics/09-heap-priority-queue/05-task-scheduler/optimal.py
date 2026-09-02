# Math formula from max frequency and its tie count — Time: O(t), Space: O(26)
from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for c in counts.values() if c == max_freq)

        skeleton = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), skeleton)


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 8  Actual:", sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
    print("Expected: 6  Actual:", sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
    print("Expected: 16  Actual:", sol.leastInterval(
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
