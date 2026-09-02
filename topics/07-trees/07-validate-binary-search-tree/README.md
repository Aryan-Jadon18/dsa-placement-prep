# 98. Validate Binary Search Tree

**Difficulty:** Medium | **Pattern:** BST Property | **Tags:** Tree, BST, DFS
**LeetCode:** https://leetcode.com/problems/validate-binary-search-tree/

## Problem
Given the root of a binary tree, determine whether it is a valid binary search tree
(BST): for every node, all values in its left subtree must be strictly less than the
node's value, and all values in its right subtree must be strictly greater — and this
must hold for *every* node, not just its immediate children.

**Input:** root of a binary tree
**Output:** `True` if it's a valid BST, else `False`

**Examples**
1. Input: `[2,1,3]` → Output: `True`. Left child `1 < 2`, right child `3 > 2`, both
   subtrees are trivially valid.
2. Input: `[5,1,4,null,null,3,6]` → Output: `False`. `4` sits as the right child of
   `5`, which requires every value in that subtree to be greater than `5` — but
   `4 < 5`, so the BST property is already broken at that edge.
3. Input: `[1]` → Output: `True`. A single node has no ordering constraints to
   violate.

**Constraints:** `1 <= number of nodes <= 10^4`, `-2^31 <= Node.val <= 2^31 - 1`.

## Intuition (explained simply)
It's tempting to just check "is each node bigger than its left child and smaller than
its right child" — but that's not enough! A node can locally look fine compared to
its parent, yet still violate an *ancestor's* bound further up. The fix: each node
must satisfy a valid `(low, high)` range inherited from *all* its ancestors, not just
its immediate parent.

### 1. Brute Force
- Do a full inorder traversal (left, node, right), collecting every value into a
  list in order. A BST's inorder traversal is always strictly increasing, so after
  collecting the whole list, just scan it once and check `list[i] < list[i+1]` for
  every consecutive pair.
- Time complexity: O(n)  Space complexity: O(n) to store the full inorder list
- Why it's not good enough: it always visits the entire tree and materializes every
  value, even though you could bail out the moment an out-of-order pair is found,
  without ever storing the whole sequence.

### 2. Better
- Recursive DFS carrying a valid `(low, high)` range: start with `(-inf, +inf)` at
  the root. When recursing into `node.left`, tighten the range to `(low, node.val)`;
  when recursing into `node.right`, tighten it to `(node.val, high)`. At each node,
  first check `low < node.val < high` — if not, return `False` immediately.
- Time complexity: O(n), but with early exit on the first violation  Space
  complexity: O(h) recursion stack
- What's still suboptimal: nothing algorithmically wrong here — this is close to
  optimal already — but recursion still carries call-stack overhead and risk for
  deeply skewed trees; an iterative traversal removes that risk.

### 3. Optimal
- Iterative inorder traversal with an explicit stack, tracking only the previously
  visited value (`prev`, initialized to `None`/`-infinity`): push all left children
  onto the stack, pop a node, compare its value to `prev` (fail if not strictly
  greater), update `prev = node.val`, then move to the right child and repeat. No
  full list is ever stored — just one running "previous value" pointer.
- This works for the same reason the brute force list-check does (inorder traversal
  of a valid BST is strictly increasing), but never buffers the whole sequence and
  exits the moment a violation is seen.
- Time complexity: O(n)  Space complexity: O(h) for the explicit stack, O(1) extra
  beyond that (just the `prev` pointer)
- Edge cases: single node → always valid; duplicate values anywhere in the tree →
  invalid, since the BST property is *strict* inequality; using `float('-inf')` /
  `float('inf')` as sentinel bounds correctly handles the full range of `Node.val`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n) | O(n) |
| Better | O(n) | O(h) |
| Optimal | O(n) | O(h) |
