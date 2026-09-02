# Precompute last index per char, two-pointer greedy scan — Time: O(n), Space: O(1) extra
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {c: i for i, c in enumerate(s)}  # later occurrences overwrite earlier ones

        sizes = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                sizes.append(end - start + 1)
                start = i + 1
        return sizes


if __name__ == "__main__":
    sol = Solution()
    print("expected [9, 7, 8], got", sol.partitionLabels("ababcbacadefegdehijhklij"))
    print("expected [10], got", sol.partitionLabels("eccbbbbdec"))
    print("expected [1, 1, 1], got", sol.partitionLabels("abc"))
