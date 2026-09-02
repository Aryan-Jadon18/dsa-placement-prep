# Grow the repeated string one copy at a time, check "in" after each — Time: O((len(a)+len(b)) * len(b)), Space: O(len(a)+len(b))
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1
        limit = len(a) + len(b)

        while len(repeated) < limit:
            if b in repeated:
                return count
            repeated += a
            count += 1

        return count if b in repeated else -1


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 3, Got:", sol.repeatedStringMatch("abcd", "cdabcdab"))
    print("Expected: 2, Got:", sol.repeatedStringMatch("a", "aa"))
    print("Expected: -1, Got:", sol.repeatedStringMatch("abc", "wxyz"))
