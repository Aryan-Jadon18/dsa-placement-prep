# Iterative inorder traversal, track prev value — Time: O(n), Space: O(h)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        node = root
        prev = float("-inf")
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            node = node.right
        return True


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
