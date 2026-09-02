# Check every bit position via shifting — Time: O(32), Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (n >> i) & 1:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.hammingWeight(0b1011))
    print("expected 1, got", sol.hammingWeight(0b10000000))
    print("expected 31, got", sol.hammingWeight(0b11111111111111111111111111111101))
