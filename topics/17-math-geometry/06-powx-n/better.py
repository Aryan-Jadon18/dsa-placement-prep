# Recursive halving (divide and conquer) — Time: O(log n), Space: O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base: float, power: int) -> float:
            if power == 0:
                return 1.0
            half = helper(base, power // 2)
            if power % 2 == 0:
                return half * half
            return half * half * base

        result = helper(x, abs(n))
        return result if n >= 0 else 1.0 / result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1024.0, Got:", sol.myPow(2.0, 10))
    print("Expected: ~9.261, Got:", sol.myPow(2.1, 3))
    print("Expected: 0.25, Got:", sol.myPow(2.0, -2))
