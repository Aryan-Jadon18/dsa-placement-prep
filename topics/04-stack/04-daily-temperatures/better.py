# Per-value index lists + binary search over the small temperature range — Time: O(n * R log n), Space: O(n)
import bisect
from collections import defaultdict
from typing import List

MIN_TEMP, MAX_TEMP = 30, 100


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        indices_by_value = defaultdict(list)
        for idx, t in enumerate(temperatures):
            indices_by_value[t].append(idx)

        answer = [0] * n
        for i, t in enumerate(temperatures):
            best_next = None
            for v in range(t + 1, MAX_TEMP + 1):
                idx_list = indices_by_value.get(v)
                if not idx_list:
                    continue
                pos = bisect.bisect_right(idx_list, i)
                if pos < len(idx_list):
                    candidate = idx_list[pos]
                    if best_next is None or candidate < best_next:
                        best_next = candidate
            if best_next is not None:
                answer[i] = best_next - i
        return answer


if __name__ == "__main__":
    sol = Solution()
    print("expected [1,1,4,2,1,1,0,0], got",
          sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print("expected [1,1,1,0], got", sol.dailyTemperatures([30, 40, 50, 60]))
    print("expected [1,1,0], got", sol.dailyTemperatures([30, 60, 90]))
