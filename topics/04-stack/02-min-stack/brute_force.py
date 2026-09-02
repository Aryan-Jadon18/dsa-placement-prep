# Plain stack, scan for min each time — push/pop/top: O(1), getMin: O(n), Space: O(n)
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


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
