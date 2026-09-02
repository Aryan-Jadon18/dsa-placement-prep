# Stack, integer ops with direct truncating division — Time: O(n), Space: O(n)
from typing import List

OPS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),  # truncate toward zero, not floor
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in OPS:
                b = stack.pop()
                a = stack.pop()
                stack.append(OPS[tok](a, b))
            else:
                stack.append(int(tok))
        return stack[-1]


if __name__ == "__main__":
    sol = Solution()
    print("expected 9, got", sol.evalRPN(["2", "1", "+", "3", "*"]))
    print("expected 6, got", sol.evalRPN(["4", "13", "5", "/", "+"]))
    print("expected 22, got", sol.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
