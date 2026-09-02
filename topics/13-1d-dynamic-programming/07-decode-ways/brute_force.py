# Plain recursion — Time: O(2^n), Space: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def ways(i: int) -> int:
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            total = ways(i + 1)
            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                total += ways(i + 2)
            return total

        return ways(0)


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.numDecodings("12"))
    print("expected 3, got", sol.numDecodings("226"))
    print("expected 0, got", sol.numDecodings("06"))
