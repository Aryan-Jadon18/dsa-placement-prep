# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy | **Pattern:** Tree Traversal — DFS/BFS | **Tags:** Tree, DFS, BFS
**LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Problem
Given the root of a binary tree, find its maximum depth — the number of nodes along
the longest path from the root down to the farthest leaf.

**Input:** root of a binary tree
**Output:** an integer, the max depth

**Examples**
1. Input: `[3,9,20,null,null,15,7]` → Output: `3`. Path `3 -> 20 -> 15` (or `3 -> 20 ->
   7`) has 3 nodes.
2. Input: `[1,null,2]` → Output: `2`. Path `1 -> 2`.
3. Input: `[]` → Output: `0`. An empty tree has depth 0.

**Constraints:** `0 <= number of nodes <= 10^4`, `-100 <= Node.val <= 100`.

## Intuition (explained simply)
Depth means "how many nodes deep does this tree go." A leaf by itself has depth 1. For
any node, its depth is 1 (itself) plus the deeper of its two children's depths.

### 1. Brute Force
- Explicitly enumerate every root-to-leaf path (e.g. via DFS that appends the current
  node to a running path list, and records a full copy of the path whenever a leaf is
  hit), then take the length of the longest recorded path.
- Time complexity: O(n^2) in the worst case (each of up to n leaves can produce a path
  copy of length O(n))  Space complexity: O(n^2) to store all paths
- Why it's not good enough: we only need a single number (the max length), not every
  path — storing all paths wastes huge amounts of memory and time for no benefit.

### 2. Better
- Recursive DFS: `depth(node) = 0` if `node` is `None`, else
  `1 + max(depth(node.left), depth(node.right))`. No need to materialize any paths.
- Time complexity: O(n)  Space complexity: O(h) recursion stack (h = height, up to
  O(n) for a skewed tree)
- What's still suboptimal: deep/skewed trees risk hitting Python's recursion limit or
  stack overflow; an iterative approach avoids that.

### 3. Optimal
- Iterative BFS level-by-level: use a queue, and for each level pop all nodes
  currently in the queue, push their children, and increment a depth counter once per
  level. When the queue empties, the counter holds the answer.
- This works because level-order traversal naturally groups nodes by depth, so
  counting levels directly gives the max depth without ever recursing.
- Time complexity: O(n)  Space complexity: O(w) where w is the max width of the tree
- Edge cases: empty tree → return 0 immediately; single node → returns 1; a completely
  skewed (linked-list-like) tree → BFS avoids the recursion-depth issue entirely.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(n^2) |
| Better | O(n) | O(h) |
| Optimal | O(n) | O(w) |
