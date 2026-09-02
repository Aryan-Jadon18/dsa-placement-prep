# Interweave copies into the original list, then unweave — Time: O(n), Space: O(1) extra
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

        # 1. interleave: A -> A' -> B -> B' -> ...
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 2. set random pointers on the copies
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3. unweave into two separate lists
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return copy_head


def build_list(vals, random_idx):
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
