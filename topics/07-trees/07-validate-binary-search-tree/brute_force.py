# Inorder traversal collect to list, check strictly increasing — Time: O(n), Space: O(n)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return all(values[i] < values[i + 1] for i in range(len(values) - 1))


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
    t1 = build_tree([2, 1, 3])
    print("expected True, got", sol.isValidBST(t1))

    t2 = build_tree([5, 1, 4, None, None, 3, 6])
    print("expected False, got", sol.isValidBST(t2))

    t3 = build_tree([1])
    print("expected True, got", sol.isValidBST(t3))
