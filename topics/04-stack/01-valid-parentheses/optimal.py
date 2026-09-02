# Stack with hash-map lookup for matching brackets — Time: O(n), Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        closer_to_opener = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in closer_to_opener:
                if not stack or stack[-1] != closer_to_opener[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.isValid("()[]{}"))
    print("expected False, got", sol.isValid("(]"))
    print("expected False, got", sol.isValid("([)]"))
