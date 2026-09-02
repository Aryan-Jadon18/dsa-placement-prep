# Repeatedly reduce the first operator found — Time: O(n^2), Space: O(n)
from typing import List

OPS = {"+", "-", "*", "/"}


def is_operator(tok: str) -> bool:
    return tok in OPS


def apply(a: int, b: int, op: str) -> int:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    return int(a / b)  # truncate toward zero


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        toks = list(tokens)
        while len(toks) > 1:
            for i, tok in enumerate(toks):
                if is_operator(tok):
                    a, b = int(toks[i - 2]), int(toks[i - 1])
                    result = apply(a, b, tok)
                    toks = toks[:i - 2] + [str(result)] + toks[i + 1:]
                    break
        return int(toks[0])


if __name__ == "__main__":
    sol = Solution()
    print("expected 9, got", sol.evalRPN(["2", "1", "+", "3", "*"]))
    print("expected 6, got", sol.evalRPN(["4", "13", "5", "/", "+"]))
    print("expected 22, got", sol.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
