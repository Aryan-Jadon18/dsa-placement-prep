# Plain recursion — Time: O(2^n), Space: O(n)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        def canBreak(i: int) -> bool:
            if i == n:
                return True
            for word in wordDict:
                end = i + len(word)
                if end <= n and s[i:end] == word and canBreak(end):
                    return True
            return False

        return canBreak(0)


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.wordBreak("leetcode", ["leet", "code"]))
    print("expected True, got", sol.wordBreak("applepenapple", ["apple", "pen"]))
    print("expected False, got", sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
