# 417. Pacific Atlantic Water Flow

**Difficulty:** Medium | **Pattern:** Graphs — Multi-source DFS/BFS | **Tags:** Graph, DFS, BFS, Matrix
**LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/

## Problem
You have a rectangular island represented as a grid of heights. The Pacific Ocean touches the top and left edges; the Atlantic touches the bottom and right edges. Water at a cell can flow to a neighboring cell (up/down/left/right) only if that neighbor's height is **less than or equal to** the current cell's height (water flows downhill or across flat ground). Find every cell from which water can reach *both* oceans.

**Input:** a grid (list of lists) of non-negative integer heights
**Output:** a list of `[row, col]` coordinates that can reach both oceans (order doesn't matter)

**Examples:**
1. A 1x1 grid `[[5]]` → `[[0, 0]]` — a single cell touches every edge, so it reaches both oceans trivially.
2.
```
1 2 2 3 5
3 2 3 4 4
2 4 5 3 1
6 7 1 4 5
5 1 1 2 4
```
→ several cells, including `[0,4]` (top row touches Pacific, and it's high enough to drain rightward/downward to Atlantic) and `[3,0]` (left column touches Pacific, tall enough to reach Atlantic).
3. A flat `2x2` grid of all `1`s → all 4 cells qualify, since every cell touches or can flow (flat, so `<=` allows movement) to a border of both oceans.

**Constraints:** `1 <= rows, cols <= 200`, heights fit in a 32-bit integer.

## Intuition
Checking "can water starting here reach the Pacific" for every cell independently is expensive. The trick: think **backwards** — instead of asking "where can water starting at cell X flow to", ask "which cells can *reach* the ocean if we walk uphill from the ocean's border". Reversing the flow direction turns this into a multi-source search from each ocean's border cells.

### 1. Brute Force
- For every single cell, run a fresh DFS/BFS following the *actual* flow rule (move to a neighbor only if its height `<=` current height) and see if that search ever touches the Pacific border, then separately check if it touches the Atlantic border. Count the cell if both are reachable.
- Correct — it's a direct simulation of the problem statement — but each cell can trigger its own traversal of up to the whole grid.
- Time complexity: O((rows × cols)^2)  Space complexity: O(rows × cols) per traversal (call stack / visited set)
- Extremely slow for the given constraints (200×200 grid → up to 1.6 billion cell-visits); an interviewer will immediately ask for something better.

### 2. Better
- Flip the direction: start a multi-source **BFS** from all Pacific-border cells simultaneously, moving to a neighbor only if the neighbor's height is `>=` current height (this is "reverse flow" — walking uphill from the ocean is equivalent to water flowing downhill into it). Mark every cell reached as "can reach Pacific". Do the same multi-source BFS from Atlantic-border cells. The answer is the intersection of the two reachable sets.
- Correct because reversing both the traversal direction and the height comparison exactly inverts the original flow relation — a cell reaches the ocean by the forward rule iff the ocean's border reaches that cell by the reverse rule.
- Time complexity: O(rows × cols) — each ocean's BFS visits every cell at most once  Space complexity: O(rows × cols) for the two visited sets + queue
- Already good, but recursion-based DFS is arguably more natural here and avoids managing two explicit queues if written with a shared helper.

### 3. Optimal
- Same multi-source reverse-flow idea, but implemented as multi-source **DFS** (recursive flood fill from every border cell of each ocean), which is a few constant-factor lines simpler since we don't need queue bookkeping, and reuses one `dfs(r, c, visited)` helper for both oceans. The answer is still the intersection of the two visited sets.
- Works for the identical reason as the BFS version — flow reachability is symmetric when you reverse direction and comparison. DFS and BFS visit the same O(rows×cols) set of cells, just in different order.
- Time complexity: O(rows × cols)  Space complexity: O(rows × cols) for visited sets + O(rows × cols) worst-case recursion depth
- Edge cases: 1x1 grid (trivially reaches both oceans), a grid with a single row/column (every cell touches both oceans' borders on that line), flat terrain (equal heights still flow due to the `<=`/`>=` rule).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O((rows·cols)^2) | O(rows·cols) |
| Better | O(rows·cols) | O(rows·cols) |
| Optimal | O(rows·cols) | O(rows·cols) |
