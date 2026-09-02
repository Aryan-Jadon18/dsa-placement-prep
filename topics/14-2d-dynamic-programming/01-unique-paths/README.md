# 62. Unique Paths

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-2D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20Combinatorics-lightgrey)
**LeetCode:** https://leetcode.com/problems/unique-paths/

## Problem
A robot sits at the top-left corner of an `m x n` grid. It can only move **right** or **down** one cell at a time, and it wants to reach the bottom-right corner. Count how many distinct paths exist.

Input: two integers `m` (rows) and `n` (columns).
Output: an integer, the number of distinct paths.

**Example 1:** `m = 3, n = 7` → `28`. There are 28 different sequences of right/down moves that walk from (0,0) to (2,6).

**Example 2:** `m = 3, n = 2` → `3`. The robot needs 2 downs and 1 right in some order: DDR, DRD, RDD.

**Example 3:** `m = 1, n = 1` → `1`. The robot is already at the destination — one (empty) path.

Constraints: `1 <= m, n <= 100`. The answer fits comfortably inside a 32-bit integer for this range.

> 🔑 **Pattern Recognition**
> The number of ways to reach any grid cell is the sum of the ways to reach its two neighbors (above and left) — a value at position `(row, col)` built from two other positions in a 2D grid is the defining shape of grid-path 2D DP.

## Intuition (explained simply)
To reach any cell, the robot must have come either from the cell directly above it or the cell directly to its left (those are the only two legal moves). So the number of ways to reach a cell is just the sum of the ways to reach its two neighbors. This "sum of ways from neighbors" is the classic signature of a grid DP problem.

### 1. Brute Force
- Recurse from `(0, 0)`: at each cell, branch into "move right" and "move down", and count how many of those branches eventually land exactly on `(m-1, n-1)`. Base case: out of bounds → 0 paths; reached the target → 1 path.
- This is correct because every legal path is exactly one right/down sequence, and the recursion tries every sequence.
- Time complexity: O(2^(m+n)) — exponential branching. Space complexity: O(m+n) for the recursion stack.
- Way too slow for a 100x100 grid (2^200-ish branches); massive redundant recomputation since the same cell is visited by many different paths.

### 2. Better
- Notice the brute force recomputes the same `(row, col)` sub-problem over and over. Cache the result of each `(row, col)` with memoization (top-down DP using a dictionary or 2D array of `None`).
- Correctness is unchanged — we're computing the exact same recurrence, just not repeating work.
- Time complexity: O(m*n) — each of the `m*n` states is computed once. Space complexity: O(m*n) for the memo table plus O(m+n) recursion stack.
- Still uses recursion (call-stack overhead, risk of hitting Python's recursion limit on large grids) and an extra full 2D cache when we don't strictly need one.

### 3. Optimal
- Define `dp[j]` as "number of ways to reach the current row at column `j`". Build the grid row by row, bottom-up (iterative), where `dp[j] = dp[j] (from the row above, still sitting in the array) + dp[j-1] (from the left in the current row)`.
- This works because we only ever need the row directly above and the value just to the left — we don't need the whole 2D table, just a single rolling 1D array reused across rows.
- Walk-through: initialize `dp = [1, 1, ..., 1]` (first row — only one way to reach any cell in row 0, by moving right the whole time). Then for each subsequent row, `dp[j] += dp[j-1]` turns the "value from above" (still stored in `dp[j]`) into "above + left".
- Time complexity: O(m*n) — one pass over every cell. Space complexity: O(n) — a single row of extra memory, no recursion stack.
- Edge cases: `m == 1` or `n == 1` should return `1` (a single straight line, no choices) — the 1D array handles this automatically since the loop body simply never fires additional updates.

#### 🎯 Visual Walkthrough
Worked example: `m = 3, n = 2` → `3`.

| row \ col | 0 | 1 |
|---|---|---|
| **0** | 1 | 1 |
| **1** | 1 | 2 |
| **2** | 1 | 3 |

`dp[r][c] = dp[r-1][c] + dp[r][c-1]`. Row 0 and column 0 are all `1` (only one straight-line path). `dp[2][1] = dp[1][1] + dp[2][0] = 2 + 1 = 3`, matching the three orderings of 2 downs and 1 right (DDR, DRD, RDD).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^(m+n)) | O(m+n) |
| Better | O(m*n) | O(m*n) |
| Optimal | O(m*n) | O(n) |
