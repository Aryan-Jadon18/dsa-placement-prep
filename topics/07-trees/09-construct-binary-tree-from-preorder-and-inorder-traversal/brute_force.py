# Linear search + array slicing at every level — Time: O(n^2), Space: O(n^2)
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)  # linear search each call

        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root


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
