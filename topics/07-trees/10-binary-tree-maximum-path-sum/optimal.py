# Single-pass post-order DFS, track global max in place — Time: O(n), Space: O(h)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")

        def max_downward(node):
            if node is None:
                return 0
            left = max(0, max_downward(node.left))
            right = max(0, max_downward(node.right))
            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)

        max_downward(root)
        return self.best


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
    t1 = build_tree([1, 2, 3])
    print("expected 6, got", sol.maxPathSum(t1))

    t2 = build_tree([-10, 9, 20, None, None, 15, 7])
    print("expected 42, got", sol.maxPathSum(t2))

    t3 = build_tree([-3])
    print("expected -3, got", sol.maxPathSum(t3))
