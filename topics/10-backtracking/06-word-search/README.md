# 79. Word Search

**Difficulty:** Medium | **Pattern:** Backtracking on Grid | **Tags:** Array, Backtracking, DFS
**LeetCode:** https://leetcode.com/problems/word-search/

## Problem
Given an `m x n` grid of characters `board` and a string `word`, determine whether
`word` can be formed by tracing a path through adjacent cells (horizontally or
vertically neighboring, not diagonal), where the same cell may not be reused more
than once within a single word.

**Input:** 2D character grid, target string `word`
**Output:** `True` if `word` can be traced out on the grid, else `False`

**Examples**
1. Input: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`,
   `word = "ABCCED"` → Output: `True`. Path: `A(0,0) -> B(0,1) -> C(0,2) -> C(1,2) ->
   E(2,2) -> D(2,1)`.
2. Input: same board, `word = "SEE"` → Output: `True`. Path: `S(1,3) -> E(2,3) ->
   E(2,2)`.
3. Input: same board, `word = "ABCB"` → Output: `False`. After `A -> B -> C`, the
   only adjacent `B` would require reusing the starting cell `B(0,1)`, which isn't
   allowed.

**Constraints:** `1 <= m, n <= 6`, `1 <= word.length <= 15`, board and word contain
only uppercase/lowercase English letters.

## Intuition (explained simply)
This is a grid-shaped backtracking search: from any cell matching `word`'s first
letter, try extending the path to each of its 4 neighbors, and see if the *next*
letter of `word` matches. If a path dead-ends, backtrack (undo the "visited" mark)
and try a different neighbor or a different starting cell.

### 1. Brute Force
- From every starting cell that matches `word[0]`, enumerate essentially all
  possible paths of length `len(word)` through neighbors — including retracing over
  already-visited cells within the same attempt — using a *separate* `set()` of
  visited coordinates copied fresh into each recursive branch (rather than mutating
  one shared structure), and checking each character along the way.
- Time complexity: O(m * n * 4^L) where L = len(word) — same branching factor as any
  DFS approach, but copying a visited-set at every recursive call adds an extra
  O(L) overhead per node  Space complexity: O(L^2) across the recursion due to each
  level holding its own copy of the visited set
- Why it's not good enough: copying the visited-set on every single recursive call
  is unnecessary overhead — the standard trick of marking/unmarking a cell in place
  (in the board itself, or one shared set) achieves the same correctness far more
  cheaply.

### 2. Better
- Backtracking DFS with a single shared `visited` set of `(row, col)` coordinates:
  mark the current cell visited before recursing into neighbors, and remove it from
  the set immediately after all 4 neighbor attempts return (undoing the mark so
  other paths can reuse that cell). Stop as soon as any path matches the full word.
- Time complexity: O(m * n * 4^L) — no more scanning overhead per call than
  necessary, but still pays for whatever hashing overhead a `set` of tuples adds at
  every step  Space complexity: O(L) for the visited set and recursion depth
- What's still suboptimal: using a hash set for visited-tracking has real constant-
  factor overhead (hashing tuples) compared to directly marking the board itself,
  which is a simple O(1) array write with no hashing at all.

### 3. Optimal
- Backtracking DFS that marks the current board cell in place (temporarily
  overwrite `board[r][c]` with a sentinel character like `'#'` that can never match
  a real letter), recurse into the 4 neighbors, then restore the original character
  before returning — no separate visited structure needed at all.
- This works because temporarily corrupting the cell's value makes it impossible for
  the same cell to be "matched" again during this path's exploration (since it no
  longer equals any real character), and restoring it afterward makes the board
  correct again for exploring other paths/branches.
- Time complexity: O(m * n * 4^L) — same asymptotic bound, but with the smallest
  possible constant factor (no hashing, no extra data structure)  Space complexity:
  O(L) recursion stack only — no auxiliary visited set at all
- Edge cases: `word` longer than the total number of cells → impossible, backtracking
  naturally returns `False` without special-casing; single-cell board matching a
  1-character word → trivially `True`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(m*n*4^L) with extra copy overhead | O(L^2) |
| Better | O(m*n*4^L) | O(L) |
| Optimal | O(m*n*4^L), smallest constants | O(L) |
