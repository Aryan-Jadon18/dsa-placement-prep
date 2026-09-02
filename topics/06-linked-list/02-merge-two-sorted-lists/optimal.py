# In-place splice with dummy head — Time: O(m+n), Space: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2  # attach the sorted remainder directly
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

    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    print("Expected: [1, 1, 2, 3, 4, 4]  Actual:", list_to_values(sol.mergeTwoLists(l1, l2)))

    l3 = build_list([])
    l4 = build_list([])
    print("Expected: []  Actual:", list_to_values(sol.mergeTwoLists(l3, l4)))

    l5 = build_list([])
    l6 = build_list([0])
    print("Expected: [0]  Actual:", list_to_values(sol.mergeTwoLists(l5, l6)))
