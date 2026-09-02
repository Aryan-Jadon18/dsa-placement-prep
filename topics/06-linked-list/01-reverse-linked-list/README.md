# 206. Reverse Linked List

**Difficulty:** Easy | **Pattern:** Linked List Basics — Pointer Manipulation | **Tags:** Linked List, Recursion
**LeetCode:** https://leetcode.com/problems/reverse-linked-list/

## Problem
You are given the head of a singly linked list. Reverse the list in place and return
the new head (which was previously the tail).

**Input:** head of a singly linked list, e.g. `1 -> 2 -> 3 -> 4 -> 5`
**Output:** the head of the reversed list, e.g. `5 -> 4 -> 3 -> 2 -> 1`

**Examples**
1. Input: `1 -> 2 -> 3 -> 4 -> 5` → Output: `5 -> 4 -> 3 -> 2 -> 1`. Every `next` pointer
   is flipped to point backward.
2. Input: `1 -> 2` → Output: `2 -> 1`.
3. Input: `[]` (empty list) → Output: `[]`. Nothing to reverse.

**Constraints:** `0 <= number of nodes <= 5000`, `-5000 <= Node.val <= 5000`.

## Intuition (explained simply)
A linked list is a chain of nodes where each node points forward to the next one.
"Reversing" it means making every node point backward instead. The tricky part is that
once you change a node's `next` pointer, you lose the way to the node that used to
follow it — so you must save that reference *before* you overwrite the pointer.

### 1. Brute Force
- Walk the list once, push every node's value onto a list (or stack). Then build a
  brand new linked list from those values in reverse order.
- This "brute force" isn't really wrong, it's just wasteful: it uses an auxiliary
  array and allocates a whole new set of nodes instead of reusing the existing ones.
- Time complexity: O(n)  Space complexity: O(n) (extra array + new nodes)
- Why it's not good enough for an interview: interviewers expect an in-place, O(1)
  extra space solution since the pointer-rewiring trick is the whole point of the
  question.

### 2. Better
- Instead of allocating new nodes, reuse the existing nodes but still use O(n) extra
  space by collecting node references into a list, then relinking `next` pointers by
  walking that list backward.
- Time complexity: O(n)  Space complexity: O(n) (list of node references)
- Still suboptimal: we don't need to store all the nodes at once — a single pass with
  three pointers does the same job in O(1) space.

### 3. Optimal
- Keep three pointers: `prev` (starts as `None`), `curr` (starts at `head`), and a
  temporary `nxt` to remember what comes after `curr` before we overwrite its `next`.
  At each step: save `nxt = curr.next`, then point `curr.next = prev`, then slide
  `prev = curr` and `curr = nxt`. Repeat until `curr` is `None`; `prev` is the new head.
- This works because we never lose track of the rest of the list — `nxt` is saved
  before the pointer that pointed to it is destroyed.
- An equally valid optimal solution is recursive: reverse the rest of the list first,
  then fix up the current node's pointers on the way back up the call stack.
- Time complexity: O(n)  Space complexity: O(1) iterative (O(n) recursion stack if
  done recursively)
- Edge cases: empty list (`head is None`), single node list — both should just return
  unchanged/trivially reversed.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
