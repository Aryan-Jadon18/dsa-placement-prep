# Rebuild mirrored tree from level-order snapshot — Time: O(n), Space: O(n)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Snapshot the tree as parallel BFS queues of (old_node, new_parent, is_left_of_new_parent).
        new_root = TreeNode(root.val)
        old_q = deque([root])
        new_q = deque([new_root])
        while old_q:
            old_node = old_q.popleft()
            new_node = new_q.popleft()
            # Build children on the NEW node in swapped order: old.left -> new.right, old.right -> new.left.
            if old_node.left is not None:
                new_node.right = TreeNode(old_node.left.val)
                old_q.append(old_node.left)
                new_q.append(new_node.right)
            if old_node.right is not None:
                new_node.left = TreeNode(old_node.right.val)
                old_q.append(old_node.right)
                new_q.append(new_node.left)
        return new_root


def tree_to_list(root):
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


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
    t1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    print("expected [4, 7, 2, 9, 6, 3, 1], got", tree_to_list(sol.invertTree(t1)))

    t2 = build_tree([2, 1, 3])
    print("expected [2, 3, 1], got", tree_to_list(sol.invertTree(t2)))

    t3 = build_tree([])
    print("expected [], got", tree_to_list(sol.invertTree(t3)))
