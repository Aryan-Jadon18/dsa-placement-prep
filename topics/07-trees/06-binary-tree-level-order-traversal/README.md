# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium | **Pattern:** BFS | **Tags:** Tree, BFS
**LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal/

## Problem
Given the root of a binary tree, return the values of its nodes grouped level by
level, from top to bottom, left to right within each level.

**Input:** root of a binary tree
**Output:** a list of lists, one inner list per level

**Examples**
1. Input: `[3,9,20,null,null,15,7]` → Output: `[[3],[9,20],[15,7]]`. Level 0 has just
   the root; level 1 has `9` and `20`; level 2 has `15` and `7`.
2. Input: `[1]` → Output: `[[1]]`. A single-node tree has one level.
3. Input: `[]` → Output: `[]`. No levels in an empty tree.

**Constraints:** `0 <= number of nodes <= 2000`, `-1000 <= Node.val <= 1000`.

## Intuition (explained simply)
"Level order" just means visiting the tree row by row, like reading a family tree
generation by generation. The natural tool for "process everything at distance k
before anything at distance k+1" is a queue — that's exactly what BFS is built for.

### 1. Brute Force
- DFS the whole tree while tracking each node's depth, collecting flat
  `(depth, value)` pairs into one big list (not grouped yet). Afterward, do a second
  pass: find the max depth, then build the list-of-lists by scanning the flat list
  once per level (or grouping via a dict and converting to a sorted list at the end).
- Time complexity: O(n) for the DFS pass + O(n) (or O(n log n) if a sort is used) to
  regroup afterward  Space complexity: O(n) for the flat intermediate list plus the
  final output
- Why it's not good enough: it does the grouping work in a separate, disconnected
  pass instead of building the level structure directly as you go — extra
  bookkeeping and an unnecessary intermediate data structure.

### 2. Better
- Recursive DFS that builds the result directly: pass the current depth into the
  recursive call, and if `depth == len(result)` (this is the first node seen at this
  depth), append a new empty list to `result` first. Then append the node's value to
  `result[depth]`. Recurse left then right.
- Time complexity: O(n)  Space complexity: O(h) recursion stack + O(n) output
- What's still suboptimal: this still relies on the call stack, which for a deeply
  skewed tree could approach O(n) depth — an iterative, queue-based approach avoids
  recursion risk and mirrors the level-by-level structure more directly.

### 3. Optimal
- Iterative BFS with a queue: push the root. While the queue isn't empty, record its
  current size (that's exactly how many nodes are in this level), pop that many
  nodes one by one, collect their values into a level list, and push their children
  for the next round. Append the level list to the result after processing it.
- This works because a queue processes nodes in the exact order they were
  discovered, and snapshotting `len(queue)` before popping guarantees you only
  process nodes from the current level before any of the next level's nodes get
  mixed in.
- Time complexity: O(n)  Space complexity: O(w) where w is the max width of the tree
  (for the queue), plus O(n) for the output
- Edge cases: empty tree → return `[]` immediately; single node → returns `[[val]]`;
  fully skewed tree → each level has exactly one node, queue stays small throughout.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n) | O(n) |
| Better | O(n) | O(h) + O(n) |
| Optimal | O(n) | O(w) + O(n) |
