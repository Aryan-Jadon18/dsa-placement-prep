# Stack with hardcoded if/elif matching — Time: O(n), Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            elif ch == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif ch == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif ch == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isValid("()[]{}"))
    print("expected False, got", sol.isValid("(]"))
    print("expected False, got", sol.isValid("([)]"))
