# Two pointers with a fixed n-gap, single pass — Time: O(L), Space: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
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

    h1 = build_list([1, 2, 3, 4, 5])
    print("Expected: [1, 2, 3, 5]  Actual:", list_to_values(sol.removeNthFromEnd(h1, 2)))

    h2 = build_list([1])
    print("Expected: []  Actual:", list_to_values(sol.removeNthFromEnd(h2, 1)))

    h3 = build_list([1, 2])
    print("Expected: [1]  Actual:", list_to_values(sol.removeNthFromEnd(h3, 1)))
