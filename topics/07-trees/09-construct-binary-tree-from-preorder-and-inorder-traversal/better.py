# Hashmap for O(1) index lookup, still slices arrays — Time: O(n^2), Space: O(n^2)
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_of = {val: i for i, val in enumerate(inorder)}

        def build(pre, ino):
            if not pre:
                return None
            root_val = pre[0]
            root = TreeNode(root_val)
            root_idx = index_of[root_val] - index_of[ino[0]] if ino else 0
            left_inorder = ino[:root_idx]
            right_inorder = ino[root_idx + 1:]
            left_preorder = pre[1:1 + len(left_inorder)]
            right_preorder = pre[1 + len(left_inorder):]
            root.left = build(left_preorder, left_inorder)
            root.right = build(right_preorder, right_inorder)
            return root

        return build(preorder, inorder)


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


if __name__ == "__main__":
    sol = Solution()
    t1 = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print("expected [3, 9, 20, None, None, 15, 7], got", tree_to_list(t1))

    t2 = sol.buildTree([1, 2], [2, 1])
    print("expected [1, 2], got", tree_to_list(t2))

    t3 = sol.buildTree([1], [1])
    print("expected [1], got", tree_to_list(t3))
