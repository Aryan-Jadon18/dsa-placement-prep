# String reversal, then 32-bit bounds check — Time: O(d), Space: O(d)
INT_MIN, INT_MAX = -2**31, 2**31 - 1


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        digits = str(abs(x))[::-1]
        result = sign * int(digits)
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 321, got", sol.reverse(123))
    print("expected -321, got", sol.reverse(-123))
    print("expected 0, got", sol.reverse(1534236469))
