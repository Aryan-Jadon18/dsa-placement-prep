# Find middle, reverse second half, merge alternately — Time: O(n), Space: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. find middle (slow ends at middle for both odd/even lengths)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse second half
        second = slow.next
        slow.next = None  # cut the list into two halves
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev  # head of reversed second half

        # 3. merge two halves alternately
        first = head
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next


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

    h1 = build_list([1, 2, 3, 4])
    sol.reorderList(h1)
    print("Expected: [1, 4, 2, 3]  Actual:", list_to_values(h1))

    h2 = build_list([1, 2, 3, 4, 5])
    sol.reorderList(h2)
    print("Expected: [1, 5, 2, 4, 3]  Actual:", list_to_values(h2))

    h3 = build_list([1])
    sol.reorderList(h3)
    print("Expected: [1]  Actual:", list_to_values(h3))
