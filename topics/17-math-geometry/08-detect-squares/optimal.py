# Points grouped by column (x -> Counter of y) — Time: O(1) add, O(k) count(), Space: O(n)
from collections import Counter, defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.cols: dict = defaultdict(Counter)  # x -> Counter(y -> multiplicity)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.cols[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        if x not in self.cols:
            return 0

        total = 0
        for y2, cnt2 in list(self.cols[x].items()):
            if y2 == y:
                continue
            side = y2 - y
            for x2 in (x + side, x - side):
                col = self.cols.get(x2)
                if not col:
                    continue
                total += cnt2 * col.get(y, 0) * col.get(y2, 0)

        return total


if __name__ == "__main__":
    ds = DetectSquares()
    for p in [[3, 10], [11, 2], [3, 2]]:
        ds.add(p)
    print("Expected: 1, Got:", ds.count([11, 10]))
    print("Expected: 0, Got:", ds.count([14, 8]))
    ds.add([11, 2])
    print("Expected: 2, Got:", ds.count([11, 10]))
