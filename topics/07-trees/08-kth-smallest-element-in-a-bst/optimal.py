# Iterative inorder traversal, stop at k-th pop — Time: O(h+k), Space: O(h)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        count = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
        return -1


def build_bst(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


def insert(node, v):
    if node is None:
        return TreeNode(v)
    if v < node.val:
        node.left = insert(node.left, v)
    else:
        node.right = insert(node.right, v)
    return node


if __name__ == "__main__":
    sol = Solution()
    t1 = build_bst([3, 1, 4, 2])
    print("expected 1, got", sol.kthSmallest(t1, 1))

    t2 = build_bst([5, 3, 6, 2, 4, 1])
    print("expected 3, got", sol.kthSmallest(t2, 3))

    t3 = build_bst([1])
    print("expected 1, got", sol.kthSmallest(t3, 1))
