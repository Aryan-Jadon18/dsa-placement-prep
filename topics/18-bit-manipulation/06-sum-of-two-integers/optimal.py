# XOR/AND carry-propagation loop, 32-bit safe — Time: O(1) (<=32 iters), Space: O(1)
MASK = 0xFFFFFFFF


class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= MASK
        b &= MASK
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        # reinterpret as signed 32-bit
        return a if a <= 0x7FFFFFFF else a - (MASK + 1)


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.getSum(1, 2))
    print("expected 5, got", sol.getSum(2, 3))
    print("expected 1, got", sol.getSum(-2, 3))
