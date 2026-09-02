# Bottom-up tabulation, O(1) space — Time: O(n), Space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # dp[i-2], dp[i-1] represent ways to decode prefixes of length i-2, i-1
        prev2, prev1 = 1, 1 if s[0] != '0' else 0
        for i in range(2, n + 1):
            current = 0
            if s[i - 1] != '0':
                current += prev1
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                current += prev2
            prev2, prev1 = prev1, current
        return prev1


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.numDecodings("12"))
    print("expected 3, got", sol.numDecodings("226"))
    print("expected 0, got", sol.numDecodings("06"))
