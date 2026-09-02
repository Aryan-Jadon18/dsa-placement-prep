# Two passes with a hash map (create nodes, then wire pointers) — Time: O(n), Space: O(n)
from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        mapping = {}
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = mapping[curr]
            copy.next = mapping[curr.next] if curr.next else None
            copy.random = mapping[curr.random] if curr.random else None
            curr = curr.next

        return mapping[head]


def build_list(vals, random_idx):
    """vals: list of values. random_idx[i] = index the i-th node's random points to, or None."""
    if not vals:
        return None
    nodes = [Node(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, ridx in enumerate(random_idx):
        nodes[i].random = nodes[ridx] if ridx is not None else None
    return nodes[0]


def list_to_pairs(head):
    out = []
    node_list = []
    curr = head
    while curr:
        node_list.append(curr)
        curr = curr.next
    for n in node_list:
        r = node_list.index(n.random) if n.random else None
        out.append((n.val, r))
    return out


if __name__ == "__main__":
    sol = Solution()

    h1 = build_list([1, 2], [1, 1])
    print("Expected: [(1, 1), (2, 1)]  Actual:", list_to_pairs(sol.copyRandomList(h1)))

    h2 = build_list([1], [None])
    print("Expected: [(1, None)]  Actual:", list_to_pairs(sol.copyRandomList(h2)))

    h3 = build_list([1], [0])
    print("Expected: [(1, 0)]  Actual:", list_to_pairs(sol.copyRandomList(h3)))
