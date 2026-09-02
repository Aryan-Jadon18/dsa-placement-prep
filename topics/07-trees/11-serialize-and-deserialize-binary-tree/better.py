# Level-order (BFS) serialize/deserialize with null markers — Time: O(n), Space: O(n)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "#"
        tokens = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                tokens.append("#")
                continue
            tokens.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ",".join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        if tokens[0] == "#":
            return None
        root = TreeNode(int(tokens[0]))
        q = deque([root])
        i = 1
        while q and i < len(tokens):
            node = q.popleft()
            left_tok = tokens[i]
            i += 1
            if left_tok != "#":
                node.left = TreeNode(int(left_tok))
                q.append(node.left)
            if i < len(tokens):
                right_tok = tokens[i]
                i += 1
                if right_tok != "#":
                    node.right = TreeNode(int(right_tok))
                    q.append(node.right)
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
