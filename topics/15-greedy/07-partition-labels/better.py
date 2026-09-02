# Remaining-count tracking with a live "open characters" set — Time: O(n), Space: O(n)
from collections import Counter


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        remaining = Counter(s)
        open_chars = set()
        sizes = []
        chunk_start = 0

        for i, c in enumerate(s):
            remaining[c] -= 1
            if remaining[c] == 0:
                open_chars.discard(c)
            else:
                open_chars.add(c)
            if not open_chars:
                sizes.append(i - chunk_start + 1)
                chunk_start = i + 1
        return sizes


if __name__ == "__main__":
    sol = Solution()
    print("expected [9, 7, 8], got", sol.partitionLabels("ababcbacadefegdehijhklij"))
    print("expected [10], got", sol.partitionLabels("eccbbbbdec"))
    print("expected [1, 1, 1], got", sol.partitionLabels("abc"))
