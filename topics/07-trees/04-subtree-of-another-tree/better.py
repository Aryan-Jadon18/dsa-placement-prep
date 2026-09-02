# Serialize both trees, substring search — Time: O(n+m) avg, Space: O(n+m)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if node is None:
                return "^#"
            return f"^{node.val};{serialize(node.left)}{serialize(node.right)}"

        return serialize(subRoot) in serialize(root)


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
    r1, s1 = build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])
    print("expected True, got", sol.isSubtree(r1, s1))

    r2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    s2 = build_tree([4, 1, 2])
    print("expected False, got", sol.isSubtree(r2, s2))

    r3, s3 = build_tree([1, 1]), build_tree([1])
    print("expected True, got", sol.isSubtree(r3, s3))
