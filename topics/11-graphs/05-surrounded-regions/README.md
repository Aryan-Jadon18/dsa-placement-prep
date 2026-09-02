# 130. Surrounded Regions

**Difficulty:** Medium | **Pattern:** Graphs — Boundary DFS/BFS | **Tags:** Graph, DFS, BFS, Matrix, Union Find
**LeetCode:** https://leetcode.com/problems/surrounded-regions/

## Problem
Given a grid of `'X'` and `'O'` characters, flip every `'O'` to `'X'` **unless** it's part of a group of `'O'`s that touches the border of the grid (directly or through a chain of connected `'O'`s). Modify the grid in place.

**Input:** a grid (list of lists) of characters `'X'`/`'O'`
**Output:** none — mutate `board` in place

**Examples:**
1.
```
X X X X
X O O X
X X O X
X O X X
```
→ the `O`s at `(1,1),(1,2),(2,2)` are surrounded (don't touch the border) and become `X`; the `O` at `(3,1)` touches the bottom border, so it (and anything chained to it) stays `O`. Result:
```
X X X X
X X X X
X X X X
X O X X
```
2. `board = [["X"]]` → stays `[["X"]]` (no `O` at all).
3. `board = [["O","O"],["O","O"]]` → every `O` touches the border (it's a 2x2 grid, so all 4 cells are on the border) → stays unchanged.

**Constraints:** `1 <= rows, cols <= 200`, grid contains only `'X'`/`'O'`.

## Intuition
A region of `O`s only survives if it's connected to the border. So instead of checking "is this region surrounded" for every region separately, flip the question: start from the border `O`s and mark everything *reachable* from them as "safe". Anything not marked safe gets flipped.

### 1. Brute Force
- For every `'O'` cell not already known to be safe, run a DFS/BFS to find its whole connected component *and simultaneously check whether that component touches any border cell*, **without caching results between cells** — meaning if two different starting cells belong to the same component, we redundantly re-explore that entire component again.
- Correct, since each component is checked against the border condition properly, just wastefully.
- Time complexity: O((rows × cols)^2) worst case (e.g. one huge component gets fully re-traversed from many starting points before we get to a global visited check)  Space complexity: O(rows × cols)
- Way too slow for a 200×200 grid in the worst case; doesn't scale.

### 2. Better
- Multi-source DFS from every `'O'` cell sitting on the border, marking every cell reachable through other `'O'`s as **safe** (temporarily relabel them, e.g. to `'S'`). One single pass handles all border-connected regions together — no redundant re-exploration. Afterward, sweep the grid once: anything still `'O'` (never marked safe) becomes `'X'`, and every `'S'` reverts to `'O'`.
- Correct because a region is unsurrounded *iff* some cell in it touches the border, and DFS from all border `O`s together discovers exactly that set of regions in one traversal.
- Time complexity: O(rows × cols)  Space complexity: O(rows × cols) worst-case recursion stack
- Works well, but recursion depth is a real risk (a snake-shaped region spanning the whole grid), and it needs two full grid sweeps (mark, then flip) plus a third implicit relabeling pass.

### 3. Optimal
- Union-Find (DSU): create one node per grid cell plus one extra **virtual "border" node**. Union every `'O'` cell with its `'O'` neighbors, and union any *border* `'O'` cell with the virtual border node. At the end, any `'O'` cell whose root differs from the border node's root gets flipped to `'X'`; everything else stays `'O'`.
- This works because "connected to the border" is exactly "same DSU component as the virtual border node" — Union-Find gives us that answer with one linear pass and no recursion, and it's the natural technique if this problem were extended to online updates (cells added/removed over time).
- Time complexity: O(rows × cols × α(rows × cols)) ≈ O(rows × cols)  Space complexity: O(rows × cols) for parent/rank arrays
- Edge cases: no `O`s at all (grid unchanged); every `O` touches the border (grid unchanged); a single-row or single-column grid (every cell is a border cell, so nothing is ever flipped).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O((rows·cols)^2) | O(rows·cols) |
| Better | O(rows·cols) | O(rows·cols) |
| Optimal | O(rows·cols·α) | O(rows·cols) |
