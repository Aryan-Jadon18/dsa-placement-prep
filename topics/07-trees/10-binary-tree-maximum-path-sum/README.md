# 124. Binary Tree Maximum Path Sum

**Difficulty:** Hard | **Pattern:** DFS Post-order | **Tags:** Tree, DFS
**LeetCode:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Problem
A "path" in a binary tree is any sequence of nodes connected by edges where no node
appears more than once; it does not need to pass through the root, and does not need
to end at a leaf. Given the root of a binary tree, find the maximum possible sum of
node values along any such path.

**Input:** root of a binary tree (values can be negative)
**Output:** an integer, the maximum path sum

**Examples**
1. Input: `[1,2,3]` → Output: `6`. The path `2 -> 1 -> 3` sums to `2 + 1 + 3 = 6`.
2. Input: `[-10,9,20,null,null,15,7]` → Output: `42`. The path `15 -> 20 -> 7` (which
   does not include the root at all) sums to `15 + 20 + 7 = 42`.
3. Input: `[-3]` → Output: `-3`. A single negative node — the path must contain at
   least one node, so we're forced to take it even though it's negative.

**Constraints:** `1 <= number of nodes <= 3*10^4`, `-1000 <= Node.val <= 1000`.

## Intuition (explained simply)
Think of each node as a potential "peak" of a path shaped like an upside-down V: the
path can go down-left from the peak, through the peak, and down-right — using at most
one downward branch on each side. For any node, the best path *that uses it as the
peak* is `node.val + best_downward_left + best_downward_right` (only counting a
branch if it's positive — a negative branch should just be skipped/treated as 0). The
overall answer is the best "peak" found anywhere in the tree.

### 1. Brute Force
- Define a helper `max_downward(node)` that returns the best single-direction path
  sum starting at `node` and going down (not branching). For *every* node in the
  tree, independently call `max_downward` on its left child and right child (each a
  fresh, non-memoized recursive call), compute `node.val + max(0, left) + max(0,
  right)`, and track the running maximum across all nodes.
- Time complexity: O(n^2) — for a skewed tree, computing `max_downward` from every
  node re-walks large overlapping portions of the tree each time  Space complexity:
  O(h) recursion stack per call, but O(n^2) total work
- Why it's not good enough: massively redundant — `max_downward` for a node's
  children overlaps heavily with `max_downward` computed for nearby nodes, and none
  of that work is reused.

### 2. Better
- First pass: post-order DFS that computes `max_downward(node)` for every node
  *once* and memoizes it in a dictionary (each node's downward value depends only on
  its children's already-computed downward values). Second pass: iterate over every
  node and compute `node.val + max(0, memo[left]) + max(0, memo[right])`, tracking
  the max.
- Time complexity: O(n) — each node's downward value computed once and reused  Space
  complexity: O(n) for the memoization dictionary plus O(h) recursion stack
- What's still suboptimal: there's no need for two separate passes or a memo
  dictionary at all — the "peak" computation at a node only needs its children's
  downward values *at the moment they're computed*, which can be folded into a single
  traversal.

### 3. Optimal
- Single-pass post-order DFS: the recursive helper computes and *returns* the best
  downward path sum for `node` (clamped to at least 0, since a negative branch should
  never be extended), but *before* returning, it also updates a running global
  maximum using `node.val + max(0, left_down) + max(0, right_down)` — capturing the
  "peak at this node" possibility right when the children's values are freshly
  available, with no memo table needed.
- This works because the only path shapes that matter are: (a) a straight line
  through one branch (what gets returned upward to the parent) and (b) a "peak" that
  uses both branches (which can never be extended further up, so it's only ever a
  candidate for the final answer, not something passed to the parent).
- Time complexity: O(n) — one pass, each node visited once  Space complexity: O(h)
  recursion stack, no auxiliary memo structure
- Edge cases: all-negative tree → the answer is simply the least-negative single
  node, since every downward extension is clamped to 0 and never chosen; single node
  → returns that node's value directly.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(h) per call |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(h) |
