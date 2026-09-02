# Repeatedly cancel adjacent matched pairs — Time: O(n^2), Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = ("()", "[]", "{}")
        changed = True
        while changed:
            changed = False
            for p in pairs:
                if p in s:
                    idx = s.index(p)
                    s = s[:idx] + s[idx + 2:]
                    changed = True
        return s == ""


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isValid("()[]{}"))
    print("expected False, got", sol.isValid("(]"))
    print("expected False, got", sol.isValid("([)]"))
