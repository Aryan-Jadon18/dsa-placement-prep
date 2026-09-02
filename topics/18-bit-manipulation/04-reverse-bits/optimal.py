# Shift-and-pull bit reversal, no string/list allocation — Time: O(32), Space: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # push lowest bit of n into result
            n >>= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print("expected 964176192, got", sol.reverseBits(0b00000010100101000001111010011100))
    print("expected 3221225471, got", sol.reverseBits(0b11111111111111111111111111111101))
    print("expected 0, got", sol.reverseBits(0))
