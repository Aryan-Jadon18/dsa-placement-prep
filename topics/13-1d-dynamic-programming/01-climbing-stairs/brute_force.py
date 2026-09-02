# Plain recursion — Time: O(2^n), Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i: int) -> int:
            if i <= 1:
                return 1
            return climb(i - 1) + climb(i - 2)

        return climb(n)


if __name__ == "__main__":
    sol = Solution()
    print("expected 2, got", sol.climbStairs(2))
    print("expected 3, got", sol.climbStairs(3))
    print("expected 8, got", sol.climbStairs(5))
