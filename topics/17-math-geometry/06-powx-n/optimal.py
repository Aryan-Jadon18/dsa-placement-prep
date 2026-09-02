# Iterative binary exponentiation — Time: O(log n), Space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        result = 1.0
        current = x

        while power > 0:
            if power & 1:
                result *= current
            current *= current
            power >>= 1

        return result if n >= 0 else 1.0 / result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 1024.0, Got:", sol.myPow(2.0, 10))
    print("Expected: ~9.261, Got:", sol.myPow(2.1, 3))
    print("Expected: 0.25, Got:", sol.myPow(2.0, -2))
    print("Expected: 1.0, Got:", sol.myPow(5.0, 0))
