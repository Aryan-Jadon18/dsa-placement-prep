# Collect digits into arrays, then add with carry — Time: O(m+n), Space: O(m+n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_digits(node):
            digits = []
            while node:
                digits.append(node.val)
                node = node.next
            return digits

        d1, d2 = to_digits(l1), to_digits(l2)
        n = max(len(d1), len(d2))
        d1 += [0] * (n - len(d1))
        d2 += [0] * (n - len(d2))

        result_digits = []
        carry = 0
        for i in range(n):
            total = d1[i] + d2[i] + carry
            result_digits.append(total % 10)
            carry = total // 10
        if carry:
            result_digits.append(carry)

        dummy = ListNode()
        tail = dummy
        for d in result_digits:
            tail.next = ListNode(d)
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
