# Brian Kernighan's algorithm: n & (n-1) clears lowest set bit — Time: O(k), Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # clears the lowest set bit
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print("expected 3, got", sol.hammingWeight(0b1011))
    print("expected 1, got", sol.hammingWeight(0b10000000))
    print("expected 31, got", sol.hammingWeight(0b11111111111111111111111111111101))
