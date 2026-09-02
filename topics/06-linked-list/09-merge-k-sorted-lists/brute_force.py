# Collect all values, sort, rebuild — Time: O(N log N), Space: O(N)
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
            curr = head
            while curr:
                values.append(curr.val)
                curr = curr.next
        values.sort()

        dummy = ListNode()
        tail = dummy
        for v in values:
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

    lists1 = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    print("Expected: [1, 1, 2, 3, 4, 4, 5, 6]  Actual:", list_to_values(sol.mergeKLists(lists1)))

    print("Expected: []  Actual:", list_to_values(sol.mergeKLists([])))

    print("Expected: []  Actual:", list_to_values(sol.mergeKLists([None])))
