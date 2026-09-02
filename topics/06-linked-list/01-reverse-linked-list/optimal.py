# Iterative three-pointer in-place reversal — Time: O(n), Space: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def list_to_values(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()

    head1 = build_list([1, 2, 3, 4, 5])
    print("Expected: [5, 4, 3, 2, 1]  Actual:", list_to_values(sol.reverseList(head1)))

    head2 = build_list([1, 2])
    print("Expected: [2, 1]  Actual:", list_to_values(sol.reverseList(head2)))

    head3 = build_list([])
    print("Expected: []  Actual:", list_to_values(sol.reverseList(head3)))
