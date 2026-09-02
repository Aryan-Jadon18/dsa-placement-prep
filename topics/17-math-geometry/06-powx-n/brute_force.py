# Repeated multiplication in a loop — Time: O(n), Space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        power = abs(n)
        result = 1.0
        for _ in range(power):
            result *= x
        return result if n >= 0 else 1.0 / result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1024.0, Got:", sol.myPow(2.0, 10))
    print("Expected: ~9.261, Got:", sol.myPow(2.1, 3))
    print("Expected: 0.25, Got:", sol.myPow(2.0, -2))
