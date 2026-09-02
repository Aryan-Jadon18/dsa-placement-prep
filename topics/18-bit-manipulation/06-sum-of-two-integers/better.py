# Manual digit-by-digit binary addition with explicit carry — Time: O(bits), Space: O(bits)
MASK = 0xFFFFFFFF


def _to_signed_32(x: int) -> int:
    x &= MASK
    return x if x <= 0x7FFFFFFF else x - (MASK + 1)


class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= MASK
        b &= MASK
        result_bits = []
        carry = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            total = bit_a ^ bit_b ^ carry          # sum bit at this position
            carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)  # majority vote -> new carry
            result_bits.append(total)

        result = 0
        for i, bit in enumerate(result_bits):
            if bit:
                result |= (1 << i)
        return _to_signed_32(result)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.getSum(1, 2))
    print("expected 5, got", sol.getSum(2, 3))
    print("expected 1, got", sol.getSum(-2, 3))
