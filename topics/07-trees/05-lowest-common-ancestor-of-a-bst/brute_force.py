# Find root-to-node paths, compare (ignores BST property) — Time: O(n), Space: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        def find_path(node, target):
            if node is None:
                return None
            if node.val == target.val:
                return [node]
            left = find_path(node.left, target)
            if left is not None:
                return [node] + left
            right = find_path(node.right, target)
            if right is not None:
                return [node] + right
            return None

        path_p = find_path(root, p)
        path_q = find_path(root, q)

        lca = None
        for a, b in zip(path_p, path_q):
            if a.val == b.val:
                lca = a
            else:
                break
        return lca


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


def find_node(root, val):
    node = root
    while node:
        if val == node.val:
            return node
        node = node.left if val < node.val else node.right
    return None


if __name__ == "__main__":
    sol = Solution()
    root = build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5])
    p, q = find_node(root, 2), find_node(root, 8)
    print("expected 6, got", sol.lowestCommonAncestor(root, p, q).val)

    p, q = find_node(root, 2), find_node(root, 4)
    print("expected 2, got", sol.lowestCommonAncestor(root, p, q).val)

    root2 = build_bst([2, 1])
    p, q = find_node(root2, 2), find_node(root2, 1)
    print("expected 2, got", sol.lowestCommonAncestor(root2, p, q).val)
