# Conditional auxiliary min-stack (push/pop only on min changes) — Time: O(1) amortized, Space: O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # only holds values that were, at push-time, <= current min

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print("expected -3, got", ms.getMin())
    ms.pop()
    print("expected 0, got", ms.top())
    print("expected -2, got", ms.getMin())

    ms2 = MinStack()
    ms2.push(5)
    ms2.push(5)
    ms2.push(5)
    print("expected 5, got", ms2.getMin())
    ms2.pop()
    print("expected 5, got", ms2.getMin())
