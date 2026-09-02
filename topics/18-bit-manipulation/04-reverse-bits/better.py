# Reverse via zero-padded binary string — Time: O(32), Space: O(32)
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = format(n, '032b')  # zero-pad to exactly 32 bits
        return int(binary[::-1], 2)


if __name__ == "__main__":
    sol = Solution()
    print("expected 964176192, got", sol.reverseBits(0b00000010100101000001111010011100))
    print("expected 3221225471, got", sol.reverseBits(0b11111111111111111111111111111101))
    print("expected 0, got", sol.reverseBits(0))
