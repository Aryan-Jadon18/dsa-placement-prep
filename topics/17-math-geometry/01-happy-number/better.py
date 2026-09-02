# Bounded iteration cap, relying on the known short non-happy cycle — Time: O(1) practical, Space: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(x: int) -> int:
            total = 0
            while x:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total

        MAX_STEPS = 1000  # far more than needed; the only non-happy cycle is length 8
        for _ in range(MAX_STEPS):
            if n == 1:
                return True
            n = sum_of_squares(n)
        return False


if __name__ == "__main__":
    sol = Solution()
    print("Expected: True, Got:", sol.isHappy(19))
    print("Expected: False, Got:", sol.isHappy(2))
    print("Expected: True, Got:", sol.isHappy(1))
