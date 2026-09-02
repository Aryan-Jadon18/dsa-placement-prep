# Min-heap over the k list fronts — Time: O(N log k), Space: O(k)
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, head in enumerate(lists):
            if head:
                # tie-break with index i since ListNode isn't comparable
                heapq.heappush(heap, (head.val, i, head))

        dummy = ListNode()
        tail = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

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
