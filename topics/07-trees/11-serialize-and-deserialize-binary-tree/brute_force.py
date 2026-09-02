# Complete-binary-tree array indexing (2i+1, 2i+2) — Time: O(2^h), Space: O(2^h)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def serialize(self, root: Optional[TreeNode]) -> str:
        h = self._height(root)
        size = (1 << h) - 1 if h > 0 else 0
        arr = [None] * size

        def fill(node, i):
            if node is None or i >= size:
                return
            arr[i] = node.val
            fill(node.left, 2 * i + 1)
            fill(node.right, 2 * i + 2)

        fill(root, 0)
        return ",".join("#" if v is None else str(v) for v in arr)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        arr = [None if tok == "#" else int(tok) for tok in data.split(",")]

        def build(i):
            if i >= len(arr) or arr[i] is None:
                return None
            node = TreeNode(arr[i])
            node.left = build(2 * i + 1)
            node.right = build(2 * i + 2)
            return node

        return build(0)


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
    codec = Codec()
    t1 = build_tree([1, 2, 3, None, None, 4, 5])
    print("expected [1, 2, 3, None, None, 4, 5], got", tree_to_list(codec.deserialize(codec.serialize(t1))))

    t2 = build_tree([])
    print("expected [], got", tree_to_list(codec.deserialize(codec.serialize(t2))))

    t3 = build_tree([1])
    print("expected [1], got", tree_to_list(codec.deserialize(codec.serialize(t3))))
