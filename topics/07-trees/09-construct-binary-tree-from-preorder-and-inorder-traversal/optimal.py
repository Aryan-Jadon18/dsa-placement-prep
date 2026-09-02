# Hashmap + index ranges into original arrays, no slicing — Time: O(n), Space: O(n)
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
        self.pre_idx = 0

        def build(in_left, in_right):
            if in_left > in_right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = index_of[root_val]
            root.left = build(in_left, mid - 1)
            root.right = build(mid + 1, in_right)
            return root

        return build(0, len(inorder) - 1)


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
