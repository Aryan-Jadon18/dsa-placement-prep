# Plain recursion, try every balloon as the next one to burst — Time: O(n!), Space: O(n)
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        def burst(balloons: tuple[int, ...]) -> int:
            if not balloons:
                return 0
            best = 0
            for i in range(len(balloons)):
                left = balloons[i - 1] if i > 0 else 1
                right = balloons[i + 1] if i < len(balloons) - 1 else 1
                remaining = balloons[:i] + balloons[i + 1:]
                gain = left * balloons[i] * right + burst(remaining)
                best = max(best, gain)
            return best

        return burst(tuple(nums))


if __name__ == "__main__":
    sol = Solution()
    print("expected 167, got", sol.maxCoins([3, 1, 5, 8]))
    print("expected 10, got", sol.maxCoins([1, 5]))
    print("expected 7, got", sol.maxCoins([7]))
