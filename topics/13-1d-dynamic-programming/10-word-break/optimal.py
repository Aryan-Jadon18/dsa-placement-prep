# Bottom-up tabulation — Time: O(n^2), Space: O(n)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True  # empty prefix is trivially segmentable

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.wordBreak("leetcode", ["leet", "code"]))
    print("expected True, got", sol.wordBreak("applepenapple", ["apple", "pen"]))
    print("expected False, got", sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
