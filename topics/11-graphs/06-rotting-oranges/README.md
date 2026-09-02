# 994. Rotting Oranges

**Difficulty:** Medium | **Pattern:** Graphs — Multi-source BFS | **Tags:** Graph, BFS, Matrix
**LeetCode:** https://leetcode.com/problems/rotting-oranges/

## Problem
A grid contains `0` (empty), `1` (fresh orange), or `2` (rotten orange). Every minute, any fresh orange adjacent (up/down/left/right) to a rotten orange also becomes rotten. Find the minimum number of minutes until no fresh orange remains, or `-1` if that's impossible.

**Input:** a grid (list of lists) of integers `0`/`1`/`2`
**Output:** an integer, minutes until all oranges rot (or `-1`)

**Examples:**
1.
```
2 1 1
1 1 0
0 1 1
```
→ `4`. Minute 1: the four oranges adjacent to the initial rotten one rot. It takes 4 minutes for rot to reach the bottom-right corner.
2. `[[0,2]]` → `0` (already no fresh oranges left).
3. `[[2,1,1],[0,1,1],[1,0,1]]` → `-1`. The orange at `(2,0)` is isolated by `0`s on all reachable sides — it can never rot.

**Constraints:** `1 <= rows, cols <= 10`, values are `0`, `1`, or `2`.

## Intuition
Multiple oranges can start rotten at once, and rot spreads outward simultaneously from all of them, level by level, like ripples merging — that's exactly what a **multi-source BFS** models, where "minute" = "BFS layer".

### 1. Brute Force
- Simulate literally minute by minute: each minute, scan the *entire* grid to find all currently-rotten oranges, then scan again to flip every fresh orange adjacent to one of them (using a copy so we don't rot things twice in the same minute). Repeat until a full minute passes with no new rot, then check if any fresh orange remains.
- Correct — it's a direct simulation — but every minute costs a full grid scan, and the number of minutes can itself be proportional to the grid size.
- Time complexity: O((rows × cols)^2)  Space complexity: O(rows × cols) for the grid copy each minute
- Wasteful: most of each scan re-examines oranges that already rotted minutes ago.

### 2. Better
- Multi-source BFS: put *every* initially-rotten orange into a queue at once (this is the key idea — don't BFS from one source at a time, start all sources together so the BFS layers naturally line up with "minutes"). Process the queue level by level, rotting fresh neighbors and enqueueing them, incrementing a minute counter each full level. After BFS completes, scan the grid once more to check if any fresh orange (`1`) is left — if so, return `-1`.
- Time complexity: O(rows × cols)  Space complexity: O(rows × cols) for the queue
- Already asymptotically optimal — the remaining refinement is just avoiding the extra full-grid rescan at the end to check for leftover fresh oranges.

### 3. Optimal
- Same multi-source BFS, but track a running `fresh_count` (total fresh oranges at the start, decremented every time one rots). When the BFS queue empties, if `fresh_count == 0` we know instantly that everything rotted — no need to rescan the grid; if `fresh_count > 0`, some oranges were unreachable, so return `-1` immediately.
- This works because we're maintaining an invariant (remaining fresh count) incrementally instead of re-deriving it with a fresh scan, saving one full O(rows×cols) pass — a small but real win, and often exactly the kind of "can you avoid the extra scan?" follow-up interviewers ask.
- Time complexity: O(rows × cols)  Space complexity: O(rows × cols) for the queue
- Edge cases: no fresh oranges at all → `0` minutes; no rotten oranges but some fresh ones → `-1` immediately; a fresh orange completely walled off by `0`s → `-1`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O((rows·cols)^2) | O(rows·cols) |
| Better | O(rows·cols) | O(rows·cols) |
| Optimal | O(rows·cols) | O(rows·cols) |
