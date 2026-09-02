# Binary string counting — Time: O(32), Space: O(32)
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]  # strip the "0b" prefix
        return binary.count('1')


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.hammingWeight(0b1011))
    print("expected 1, got", sol.hammingWeight(0b10000000))
    print("expected 31, got", sol.hammingWeight(0b11111111111111111111111111111101))
