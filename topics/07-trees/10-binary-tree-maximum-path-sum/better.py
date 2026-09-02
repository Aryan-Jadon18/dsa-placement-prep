# Two-pass: memoize downward sums, then scan for best peak — Time: O(n), Space: O(n)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        memo = {None: 0}

        def compute_downward(node):
            if node is None:
                return 0
            left = compute_downward(node.left)
            right = compute_downward(node.right)
            memo[node] = node.val + max(0, left, right)
            return memo[node]

        compute_downward(root)

        best_overall = float("-inf")

        def scan(node):
            nonlocal best_overall
            if node is None:
                return
            left_down = memo.get(node.left, 0)
            right_down = memo.get(node.right, 0)
            best_overall = max(best_overall, node.val + max(0, left_down) + max(0, right_down))
            scan(node.left)
            scan(node.right)

        scan(root)
        return best_overall


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
    t1 = build_tree([1, 2, 3])
    print("expected 6, got", sol.maxPathSum(t1))

    t2 = build_tree([-10, 9, 20, None, None, 15, 7])
    print("expected 42, got", sol.maxPathSum(t2))

    t3 = build_tree([-3])
    print("expected -3, got", sol.maxPathSum(t3))
