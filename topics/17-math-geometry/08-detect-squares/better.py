# Global point-count hash map, scanning all distinct points per query — Time: O(n) per count(), Space: O(n)
from collections import Counter
from typing import List


class DetectSquares:
    def __init__(self):
        self.point_counts: Counter = Counter()

    def add(self, point: List[int]) -> None:
        self.point_counts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (px, py), cnt2 in self.point_counts.items():
            if px != x or py == y:
                continue
            side = py - y
            for x2 in (x + side, x - side):
                total += cnt2 * self.point_counts.get((x2, y), 0) * self.point_counts.get((x2, py), 0)

        return total


if __name__ == "__main__":
    ds = DetectSquares()
    for p in [[3, 10], [11, 2], [3, 2]]:
        ds.add(p)
    print("Expected: 1, Got:", ds.count([11, 10]))
    print("Expected: 0, Got:", ds.count([14, 8]))
    ds.add([11, 2])
    print("Expected: 2, Got:", ds.count([11, 10]))
