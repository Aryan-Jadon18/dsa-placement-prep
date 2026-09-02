# Digit-peeling with pre-emptive overflow check — Time: O(d), Space: O(1)
INT_MIN, INT_MAX = -2**31, 2**31 - 1


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        n = abs(x)
        result = 0
        limit = INT_MAX  # both bounds have the same magnitude threshold when working with abs()
        while n != 0:
            digit = n % 10
            n //= 10
            # check BEFORE multiplying, as a fixed-width language would have to
            if result > (limit - digit) // 10:
                return 0
            result = result * 10 + digit
        return sign * result


if __name__ == "__main__":
    sol = Solution()
    print("expected 321, got", sol.reverse(123))
    print("expected -321, got", sol.reverse(-123))
    print("expected 0, got", sol.reverse(1534236469))
