# 329. Longest Increasing Path in a Matrix

**Difficulty:** Hard | **Pattern:** DFS + Memoization | **Tags:** DP, DFS, Matrix
**LeetCode:** https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

## Problem
Given an `m x n` integer matrix, find the length of the longest path where each step moves to a horizontally or vertically adjacent cell whose value is strictly greater than the current cell's value (no diagonal moves, no revisiting needed since values must strictly increase).

Input: a 2D list of integers `matrix`.
Output: an integer, the length (number of cells) of the longest strictly increasing path.

**Example 1:** `matrix = [[9,9,4],[6,6,8],[2,1,1]]` → `4`. The path `1 → 2 → 6 → 9` (bottom row up the left column) has length 4.

**Example 2:** `matrix = [[3,4,5],[3,2,6],[2,2,1]]` → `4`. The path `3 → 4 → 5 → 6` has length 4.

**Example 3:** `matrix = [[1]]` → `1`. A single cell is a path of length 1 by itself.

Constraints: `1 <= m, n <= 200`, `0 <= matrix[i][j] <= 2^31 - 1`.

## Intuition (explained simply)
Because the path must be *strictly increasing*, it can never revisit a cell (a cell can't be greater than itself), so there's no cycle-detection issue like in general graph DFS. Each cell has 4 potential neighbors; from any starting cell, the longest increasing path is `1 + the best result among neighbors that are strictly larger`. That "1 + best of subproblems" shape is what makes memoized DFS the natural fit — same cell can be the shared endpoint of many different paths that start elsewhere, so caching each cell's answer avoids massive recomputation.

### 1. Brute Force
- From every cell, run a DFS that tries all 4 directions, only stepping into a neighbor with a strictly larger value, and tracks the length of the longest such chain reachable from that starting cell. Take the max over all starting cells.
- Correct because it directly searches every strictly increasing path starting from every cell.
- Time complexity: O(4^(m*n)) in the worst case — at each of up to `m*n` cells along a path, up to 4 branches, with no caching to cut off repeated sub-searches. Space complexity: O(m*n) recursion depth for the longest possible path.
- Wildly redundant: the sub-path starting at a given cell is recomputed every single time some other path reaches that cell, and there can be exponentially many such paths.

### 2. Better
- Notice the DFS launched from a given cell always returns the *same* answer no matter which earlier path led to it (it only depends on the matrix values from that cell onward). Memoize the result of `longest_from(row, col)` the first time it's computed (top-down DP / "DFS + memo").
- Correctness holds because the sub-problem "longest increasing path starting at `(row, col)`" truly is independent of history — it only depends on `(row, col)` and the fixed matrix.
- Time complexity: O(m*n) — each of the `m*n` cells' DFS runs its 4-way branch exactly once and is cached thereafter, and each edge (adjacent cell pair) is inspected O(1) times amortized. Space complexity: O(m*n) for the memo table + O(m*n) recursion stack worst case (a strictly increasing path can snake through every cell).
- This is already close to optimal — the "better" and "optimal" solutions for this specific problem share the same asymptotic complexity; the difference here is implementation style (recursive DFS+memo vs. an iterative topological order), which is worth knowing as an alternative.

### 3. Optimal
- Treat the matrix as a DAG: draw a directed edge from every cell to each strictly-larger neighbor. Because edges always point from smaller to larger values, this graph has no cycles, so it has a valid topological order. Process cells in increasing order of value (equivalent to Kahn's algorithm using in-degree = "number of larger neighbors", or simply sorting all cells by value) and compute `dp[cell] = 1 + max(dp[neighbor] for smaller neighbors already processed)` — or symmetrically, process from *largest* value down to smallest so that by the time we reach a cell, all its strictly-larger neighbors are already finalized.
- `dp[row][col]` here means: the length of the longest strictly increasing path starting at `(row, col)`. Processing cells from largest matrix value to smallest guarantees every neighbor that could extend the path (a larger value) has already been finalized when we compute the current cell.
- This avoids recursion entirely (iterative, no call-stack risk) while achieving the identical O(m*n) work, by exploiting that a strictly-increasing constraint always defines a DAG with a natural value-based topological order.
- Time complexity: O(m*n log(m*n)) for the sort-by-value variant (or O(m*n) with a counting/bucket sort by value, or true Kahn's BFS by in-degree). Space complexity: O(m*n) for the `dp` table and the sorted-order structure.
- Edge cases: `1x1` matrix → answer 1; a matrix that is entirely one repeated value → answer 1 (no strict increase is possible anywhere); a fully strictly increasing snake path through every cell → answer `m*n`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(4^(m*n)) | O(m*n) |
| Better | O(m*n) | O(m*n) |
| Optimal | O(m*n log(m*n)) | O(m*n) |
