# Convert to int, add, convert back — Time: O(m+n), Space: O(m+n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_int(node):
            digits = []
            while node:
                digits.append(str(node.val))
                node = node.next
            return int("".join(reversed(digits)))

        total = to_int(l1) + to_int(l2)
        digits = str(total)

        dummy = ListNode()
        tail = dummy
        for d in reversed(digits):
            tail.next = ListNode(int(d))
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

    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    print("Expected: [7, 0, 8]  Actual:", list_to_values(sol.addTwoNumbers(l1, l2)))

    l3 = build_list([0])
    l4 = build_list([0])
    print("Expected: [0]  Actual:", list_to_values(sol.addTwoNumbers(l3, l4)))

    l5 = build_list([9, 9, 9, 9])
    l6 = build_list([9, 9])
    print("Expected: [8, 9, 0, 0, 1]  Actual:", list_to_values(sol.addTwoNumbers(l5, l6)))
