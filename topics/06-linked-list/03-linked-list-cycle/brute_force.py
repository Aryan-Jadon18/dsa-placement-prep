# Re-scan visited-so-far list on every step — Time: O(n^2), Space: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        curr = head
        while curr:
            if curr in visited:  # linear membership check
                return True
            visited.append(curr)
            curr = curr.next
        return False


def build_cyclic_list(values, pos):
    """pos = index the tail connects back to, or -1 for no cycle."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()

    head1 = build_cyclic_list([3, 2, 0, -4], 1)
    print("Expected: True  Actual:", sol.hasCycle(head1))

    head2 = build_cyclic_list([1, 2], 0)
    print("Expected: True  Actual:", sol.hasCycle(head2))

    head3 = build_cyclic_list([1], -1)
    print("Expected: False  Actual:", sol.hasCycle(head3))
