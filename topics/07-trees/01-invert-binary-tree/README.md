# 226. Invert Binary Tree

**Difficulty:** Easy | **Pattern:** Tree Traversal — DFS/BFS | **Tags:** Tree, DFS, BFS
**LeetCode:** https://leetcode.com/problems/invert-binary-tree/

## Problem
Given the root of a binary tree, flip it into its mirror image: every node's left and
right children are swapped, all the way down the tree. Return the root of the mutated
tree.

**Input:** root of a binary tree
**Output:** root of the same tree with every subtree mirrored

**Examples**
1. Input: `[4,2,7,1,3,6,9]` → Output: `[4,7,2,9,6,3,1]`. At the root, `2` and `7`
   swap places, then their children swap too, recursively.
2. Input: `[2,1,3]` → Output: `[2,3,1]`. A simple 3-node swap.
3. Input: `[]` → Output: `[]`. Nothing to invert.

**Constraints:** `0 <= number of nodes <= 100`, `-100 <= Node.val <= 100`.

## Intuition (explained simply)
"Inverting" a tree means making it a mirror of itself — whatever was on the left is
now on the right, at every level. If you swap a node's two children and then also fix
up the children's children the same way, the whole tree ends up mirrored.

### 1. Brute Force
- Collect every node's value along with its position (e.g. via level-order coordinates
  or by recording left/right paths), build a brand-new tree by mirroring the
  positions, then copy values back — effectively treating it as "rebuild a mirrored
  tree from scratch" rather than mutating in place.
- Time complexity: O(n)  Space complexity: O(n) (extra structure to track positions)
- Why it's not good enough: it's needlessly complicated and wasteful — the problem
  can be solved by simply swapping pointers in place, so building auxiliary
  structures shows you haven't seen the simpler pointer trick.

### 2. Better
- Recursive DFS: at each node, swap its `left` and `right` children, then recurse into
  both (now-swapped) subtrees. This mutates the existing tree in place instead of
  rebuilding it.
- Time complexity: O(n)  Space complexity: O(h) recursion stack (h = height)
- What's still suboptimal: for a very skewed (linked-list-like) tree, the recursion
  depth can hit O(n), risking a stack overflow on huge inputs — an iterative version
  avoids that risk entirely.

### 3. Optimal
- Iterative BFS/DFS with an explicit stack or queue: push the root, and while the
  container isn't empty, pop a node, swap its children, and push the (non-null)
  children for later processing. No recursion needed.
- This works because swapping is a purely local operation per node — order of
  visiting doesn't matter, only that every node gets visited once and its children
  swapped once.
- Time complexity: O(n)  Space complexity: O(w) where w is the max width of the tree
  (up to O(n) in the worst case, but no call-stack risk)
- Edge cases: empty tree (`root is None`) → return `None` immediately; single node →
  swapping two `None` children is a no-op, correctly returns the same node.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n) | O(n) |
| Better | O(n) | O(h) |
| Optimal | O(n) | O(w) |
