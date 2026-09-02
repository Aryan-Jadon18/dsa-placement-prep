# Monotonic decreasing stack of indices — Time: O(n), Space: O(n)
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices with temperatures in decreasing order
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        return answer


if __name__ == "__main__":
    sol = Solution()
    print("expected [1,1,4,2,1,1,0,0], got",
          sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print("expected [1,1,1,0], got", sol.dailyTemperatures([30, 40, 50, 60]))
    print("expected [1,1,0], got", sol.dailyTemperatures([30, 60, 90]))
