# Serialize both trees to strings, then compare — Time: O(n), Space: O(n)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def serialize(node):
            if node is None:
                return "#"
            return f"{node.val}({serialize(node.left)},{serialize(node.right)})"

        return serialize(p) == serialize(q)


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
    return root


if __name__ == "__main__":
    sol = Solution()
    p1, q1 = build_tree([1, 2, 3]), build_tree([1, 2, 3])
    print("expected True, got", sol.isSameTree(p1, q1))

    p2, q2 = build_tree([1, 2]), build_tree([1, None, 2])
    print("expected False, got", sol.isSameTree(p2, q2))

    p3, q3 = build_tree([1, 2, 1]), build_tree([1, 1, 2])
    print("expected False, got", sol.isSameTree(p3, q3))
