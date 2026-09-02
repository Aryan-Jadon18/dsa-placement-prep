# Plain list, repeated list.count() scans — Time: O(n^2) per count(), Space: O(n)
from typing import List


class DetectSquares:
    def __init__(self):
        self.points: List[tuple] = []

    def add(self, point: List[int]) -> None:
        self.points.append(tuple(point))

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0
        same_col_ys = {p[1] for p in self.points if p[0] == x and p[1] != y}

        for y2 in same_col_ys:
            cnt2 = self.points.count((x, y2))
            side = y2 - y
            for x2 in (x + side, x - side):
                cnt_c1 = self.points.count((x2, y))
                cnt_c2 = self.points.count((x2, y2))
                total += cnt2 * cnt_c1 * cnt_c2

        return total


if __name__ == "__main__":
    ds = DetectSquares()
    for p in [[3, 10], [11, 2], [3, 2]]:
        ds.add(p)
    print("Expected: 1, Got:", ds.count([11, 10]))
    print("Expected: 0, Got:", ds.count([14, 8]))
    ds.add([11, 2])
    print("Expected: 2, Got:", ds.count([11, 10]))
