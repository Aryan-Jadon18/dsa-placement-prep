# Enumerate all root-to-leaf paths, take max length — Time: O(n^2), Space: O(n^2)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        all_paths = []

        def dfs(node, path):
            if node is None:
                return
            path = path + [node.val]  # copy: O(n) per call in the worst case
            if node.left is None and node.right is None:
                all_paths.append(path)
                return
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, [])
        return max(len(p) for p in all_paths)


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
    t1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("expected 3, got", sol.maxDepth(t1))

    t2 = build_tree([1, None, 2])
    print("expected 2, got", sol.maxDepth(t2))

    t3 = build_tree([])
    print("expected 0, got", sol.maxDepth(t3))
