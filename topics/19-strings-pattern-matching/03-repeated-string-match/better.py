# Compute minimal repeat count directly, check with built-in substring search — Time: O(len(a)+len(b)), Space: O(len(a)+len(b))
import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_count = math.ceil(len(b) / len(a))

        candidate = a * min_count
        if b in candidate:
            return min_count

        candidate += a  # one extra copy covers wraparound alignment
        if b in candidate:
            return min_count + 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 3, Got:", sol.repeatedStringMatch("abcd", "cdabcdab"))
    print("Expected: 2, Got:", sol.repeatedStringMatch("a", "aa"))
    print("Expected: -1, Got:", sol.repeatedStringMatch("abc", "wxyz"))
