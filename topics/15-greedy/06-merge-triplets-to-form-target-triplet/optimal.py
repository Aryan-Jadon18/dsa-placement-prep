# Single pass, running elementwise-max accumulator — Time: O(n), Space: O(1)
class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        best = [0, 0, 0]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            best[0] = max(best[0], t[0])
            best[1] = max(best[1], t[1])
            best[2] = max(best[2], t[2])
        return best == target


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))
    print("expected False, got", sol.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]))
    print("expected True, got", sol.mergeTriplets([[1, 2, 3]], [1, 2, 3]))
