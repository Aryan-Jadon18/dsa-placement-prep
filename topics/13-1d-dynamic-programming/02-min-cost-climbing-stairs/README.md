# 746. Min Cost Climbing Stairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Pattern](https://img.shields.io/badge/Pattern-1D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20Array-lightgrey)
**LeetCode:** https://leetcode.com/problems/min-cost-climbing-stairs/

## Problem
Each step `i` of a staircase has a cost `cost[i]` you pay when you step on it. From a step you can move 1 or 2 steps forward. You may start standing on step `0` or step `1` for free. Find the minimum total cost to reach just past the last step (the "top", index `n`).

**Input:** an integer array `cost`
**Output:** an integer — the minimum total cost to reach the top

**Examples:**
1. `cost = [10, 15, 20]` → `15`. Start at index 1 (free), pay 15, jump 2 steps straight to the top.
2. `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]` → `6`. Best path pays indices 0,2,4,6,7,9.
3. `cost = [0, 0, 0, 1]` → `0`. Start at index 1, take free 0-cost steps, then a 2-step jump from index 2 to the top skips index 3 entirely.

**Constraints:** `2 <= cost.length <= 1000`, `0 <= cost[i] <= 999`.

> 🔑 **Pattern Recognition**
> The cheapest way to arrive at any position is defined purely in terms of the cheapest way to arrive at the two positions behind it — an optimal-substructure minimization where each state only needs its two immediate predecessors. That's the signature of a rolling 1D DP.

## Intuition (explained simply)
The "top" is one step past the last index. To land there, your last move came from either the last step or the second-to-last step. So the cheapest way to reach any position is the cheapest way to reach one of the two positions behind it, plus the cost of standing on the position you jumped from.

### 1. Brute Force
- Plain recursion `minCost(i)` = minimum cost to reach the top starting from step `i`. From step `i`, you can pay `cost[i]` and jump 1 or 2 steps: `minCost(i) = cost[i] + min(minCost(i+1), minCost(i+2))`. Base case: once `i >= n` (past the last step) cost to finish is `0`.
- Try starting from both step 0 and step 1 and take the smaller: `min(minCost(0), minCost(1))`.
- Time complexity: O(2^n)  Space complexity: O(n) (recursion stack)
- Each `minCost(i)` gets recomputed many times through different paths — massive overlap for larger `n`.

### 2. Better
- Memoize `minCost(i)` so each step index is only computed once (top-down DP).
- Same recursion, same correctness argument, but every distinct `i` solved exactly once.
- Time complexity: O(n)  Space complexity: O(n) cache + O(n) recursion stack
- Recursion overhead and stack depth are unnecessary — we can compute this iteratively instead.

### 3. Optimal
- **DP state:** let `dp[i]` = minimum cost to *reach* step `i` (i.e. to have your foot land on `i`, cost of `i` included once you leave it — equivalently we can define `dp[i]` as min cost to arrive at position `i` where position `n` is the free top).
- **Transition:** `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])` — to arrive at `i` you came from `i-1` (paying its cost) or `i-2` (paying its cost).
- **Base cases:** `dp[0] = 0`, `dp[1] = 0` (both starting points are free).
- Build up from `dp[0], dp[1]` to `dp[n]`; since each state only needs the previous two, keep two rolling variables.
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: `n = 2` (only two steps, answer is `min(cost[0], cost[1])`), all zero costs (answer 0).

#### 🎯 Visual Walkthrough
Worked example: `cost = [10, 15, 20]` → `15`.

| i | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| dp[i] | 0 | 0 | 10 | 15 |

`dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])` — e.g. `dp[2] = min(dp[1]+cost[1], dp[0]+cost[0]) = min(15, 10) = 10`, then `dp[3] = min(dp[2]+cost[2], dp[1]+cost[1]) = min(30, 15) = 15`, matching the "start at index 1, jump straight to the top" path.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
