# Check every candidate cut by scanning ahead for reappearances — Time: O(n^2), Space: O(n)
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        n = len(s)
        sizes = []
        start = 0
        while start < n:
            end = start
            seen = set()
            i = start
            while i <= end:
                c = s[i]
                seen.add(c)
                last_occurrence = s.rfind(c)  # scan to find how far this char reappears
                end = max(end, last_occurrence)
                i += 1
            sizes.append(end - start + 1)
            start = end + 1
        return sizes


if __name__ == "__main__":
    sol = Solution()
    print("expected [9, 7, 8], got", sol.partitionLabels("ababcbacadefegdehijhklij"))
    print("expected [10], got", sol.partitionLabels("eccbbbbdec"))
    print("expected [1, 1, 1], got", sol.partitionLabels("abc"))
