# Repeated bitwise +1/-1 stepping, 32-bit safe — Time: O(max(|a|,|b|)), Space: O(1)
MASK = 0xFFFFFFFF
SIGN_BIT = 0x80000000


def _to_signed_32(x: int) -> int:
    x &= MASK
    return x if x <= 0x7FFFFFFF else x - (MASK + 1)


def _bitwise_step(x: int, delta_bits: int) -> int:
    # add a single 32-bit value (1, or -1 represented as MASK) using only ^, &, <<
    x &= MASK
    carry = delta_bits & MASK
    while carry != 0:
        x, carry = (x ^ carry) & MASK, ((x & carry) << 1) & MASK
    return x


class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = a & MASK
        steps = b if b >= 0 else -b
        one = 1
        neg_one = MASK  # two's-complement representation of -1 in 32 bits
        for _ in range(steps):
            result = _bitwise_step(result, one if b >= 0 else neg_one)
        return _to_signed_32(result)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.getSum(1, 2))
    print("expected 5, got", sol.getSum(2, 3))
    print("expected 1, got", sol.getSum(-2, 3))
