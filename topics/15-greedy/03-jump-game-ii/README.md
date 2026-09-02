# 45. Jump Game II

**Difficulty:** Medium | **Pattern:** Greedy | **Tags:** Array, Greedy
**LeetCode:** https://leetcode.com/problems/jump-game-ii/

## Problem
Same setup as Jump Game: `nums[i]` is the max steps you can jump forward from index `i`, starting at index 0. This time, the goal is always reachable — return the **minimum number of jumps** needed to reach the last index.

Input: `nums`, a list of non-negative integers.
Output: an integer, the minimum number of jumps to the last index.

**Example 1:** `nums = [2,3,1,1,4]` → `2`. Jump from index 0 to index 1 (using the value 2's reach is optional — a 1-step jump suffices), then from index 1 to index 4 (a jump of 3, within the max of 3). Two jumps total.

**Example 2:** `nums = [2,3,0,1,4]` → `2`. Jump from index 0 to index 1, then index 1 to index 4.

**Example 3:** `nums = [0]` → `0`. Already at the last index — zero jumps needed.

Constraints: `1 <= nums.length <= 10^4`, `0 <= nums[i] <= 1000`. It's guaranteed you can always reach the last index.

## Intuition (explained simply)
Think in terms of "waves" or "levels," like a breadth-first search over reachable positions. From your current jump-count level, there's a whole range of indices reachable with exactly that many jumps; among all of them, the farthest one you could reach determines the reach of the *next* level. You never need to decide "which exact index to jump from" — only "how far can this whole current level collectively reach," because that farthest boundary is all that matters for minimizing jump count.

### 1. Brute Force
- Recurse from each index, trying every possible jump length, and take `1 + min(jumps to reach the end from each of the resulting indices)` over all viable choices.
- Correct because it exhaustively tries every jump sequence and keeps the shortest.
- Time complexity: O(2^n) — branching factor up to `nums[i]` at each of `n` positions in the worst case. Space complexity: O(n) recursion depth.
- Exponential; totally impractical for `n` up to 10,000.

### 2. Better
- DP formulation: `dp[i]` = minimum jumps to reach index `i` from index 0, `dp[0] = 0`. For each index `i` in increasing order, for every `j` reachable from `i` (`i+1` to `i+nums[i]`), update `dp[j] = min(dp[j], dp[i] + 1)`. The answer is `dp[n-1]`.
- Correct because it's a standard shortest-path-on-a-DAG relaxation: every edge `i -> j` (a legal jump) is considered, and we keep the best (fewest-jump) way to reach each node.
- Time complexity: O(n^2) worst case — for each of `n` indices, relaxing up to `nums[i]` outgoing edges. Space complexity: O(n) for the `dp` array.
- Quadratic — we're redoing work that a single forward "wave" scan captures in linear time, since we don't actually need every individual `dp[i]` value, only the boundary of what's reachable at each jump count.

### 3. Optimal
- Greedy BFS-by-levels ("jump ranges"): maintain `current_end` (the farthest index reachable using the jumps taken *so far*) and `farthest` (the farthest index reachable from any position within the current level, looking one jump ahead). Scan `i` from 0 to `n-2`: update `farthest = max(farthest, i + nums[i])`. When `i` reaches `current_end` (we've examined every index in the current level), we're forced to take another jump — increment the jump counter and set `current_end = farthest` (the new level's boundary).
- **Why the greedy choice is safe:** among all indices within the current reachable level, the *only* thing that matters for the next jump's reach is the single farthest index any of them can hit — which specific index achieves that farthest reach is irrelevant, since we're free to choose which index within the current level to actually jump from once we've decided to advance. Committing to "extend the level to the max seen so far, then jump" never does worse than any other strategy, because a smaller within-level reach can never help reach the end sooner, and delaying the jump decision past the level boundary would waste a jump.
- Time complexity: O(n) — one linear pass. Space complexity: O(1) — three scalars (jumps, current_end, farthest).
- Edge cases: `n == 1` → 0 jumps (already there), loop must not run past the last index or it may over-count; guaranteed-reachable input means we never need an "impossible" check here (unlike Jump Game I).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n^2) | O(n) |
| Optimal | O(n) | O(1) |
