# Linear scan forward from each day — Time: O(n^2), Space: O(1) extra
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break
        return answer


if __name__ == "__main__":
    sol = Solution()
    print("expected [1,1,4,2,1,1,0,0], got",
          sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print("expected [1,1,1,0], got", sol.dailyTemperatures([30, 40, 50, 60]))
    print("expected [1,1,0], got", sol.dailyTemperatures([30, 60, 90]))
