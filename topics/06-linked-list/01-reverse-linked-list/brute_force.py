# Collect values, build a new list — Time: O(n), Space: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        dummy = ListNode()
        tail = dummy
        for v in reversed(values):
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next


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
