# Top-down recursion + memoization — Time: O(n^2), Space: O(n)
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)

        @lru_cache(maxsize=None)
        def canBreak(i: int) -> bool:
            if i == n:
                return True
            for j in range(i + 1, n + 1):
                if s[i:j] in words and canBreak(j):
                    return True
            return False

        result = canBreak(0)
        canBreak.cache_clear()
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.wordBreak("leetcode", ["leet", "code"]))
    print("expected True, got", sol.wordBreak("applepenapple", ["apple", "pen"]))
    print("expected False, got", sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
