# Collect nodes in array, two-pointer weave — Time: O(n), Space: O(n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1
        nodes[left].next = None  # terminate the list


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
