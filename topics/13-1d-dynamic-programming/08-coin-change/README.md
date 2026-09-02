# 322. Coin Change

**Difficulty:** Medium | **Pattern:** Unbounded Knapsack DP — 1D DP | **Tags:** DP
**LeetCode:** https://leetcode.com/problems/coin-change/

## Problem
Given coin denominations `coins` (unlimited supply of each) and a target `amount`, find the minimum number of coins needed to make exactly `amount`. If it can't be made, return `-1`.

**Input:** an integer array `coins`, an integer `amount`
**Output:** an integer — the fewest coins to reach `amount` exactly, or `-1` if impossible

**Examples:**
1. `coins = [1, 2, 5]`, `amount = 11` → `3`. `5 + 5 + 1 = 11`.
2. `coins = [2]`, `amount = 3` → `-1`. Odd target, only even coin — impossible.
3. `coins = [1]`, `amount = 0` → `0`. Zero coins needed for zero target.

**Constraints:** `1 <= coins.length <= 12`, `1 <= coins[i] <= 2^31 - 1`, `0 <= amount <= 10^4`.

## Intuition (explained simply)
To make a target amount, you must have used some coin last. Whatever that last coin's value `c` was, the rest of the coins had to sum to `amount - c`. So the best way to make `amount` is: try every coin as the "last coin used," and take `1 + (best way to make amount - c)`.

### 1. Brute Force
- Plain recursion `minCoins(remaining)`: if `remaining == 0`, need 0 more coins. Otherwise, try every coin `c <= remaining` as the last one used and recurse on `remaining - c`, taking `1 + minCoins(remaining - c)`; take the minimum over all valid coins. If no coin fits or all recursive branches fail, that state is "impossible" (represented with infinity).
- Correct because it exhaustively considers every possible sequence of coins that could sum to `remaining`, via the "what was the last coin" decomposition.
- Time complexity: O(coins^amount) in the worst case (a branching recursion tree amount levels deep)  Space complexity: O(amount) (recursion depth)
- The same `remaining` value gets recomputed from many different coin-choice paths — massive overlapping-subproblem waste, effectively exponential.

### 2. Better
- Memoize `minCoins(remaining)` so each distinct remaining amount is only solved once (top-down DP).
- Same recursive logic and correctness argument, but cached.
- Time complexity: O(amount * len(coins))  Space complexity: O(amount) cache + O(amount) recursion stack
- Recursion overhead and stack depth (up to `amount` deep) are avoidable with an iterative bottom-up sweep.

### 3. Optimal
- **DP state:** let `dp[i]` = the minimum number of coins needed to make amount `i` exactly. Initialize `dp[0] = 0` (zero coins for zero amount) and every other `dp[i] = infinity` (not yet known reachable).
- **Transition:** for each amount `i` from `1` to `amount`, for each coin `c` in `coins` where `c <= i`: `dp[i] = min(dp[i], dp[i - c] + 1)` — "if I can make `i - c` with `dp[i-c]` coins, adding one more coin of value `c` makes `i`."
- Fill `dp` bottom-up from `0` to `amount`; each `dp[i]` only needs previously-computed smaller indices, so ordinary array iteration (no full table beyond 1D) suffices. Since each `coins[i]` can be reused any number of times, this is "unbounded knapsack" — we don't restrict how many times a coin index can be picked, unlike 0/1 knapsack.
- Time complexity: O(amount * len(coins))  Space complexity: O(amount)
- Edge cases: `amount = 0` → answer 0 immediately; no combination of coins reaches `amount` → `dp[amount]` stays infinity, return `-1`; a coin value larger than `amount` is simply skipped (never applicable).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(coins^amount) | O(amount) |
| Better | O(amount · coins) | O(amount) |
| Optimal | O(amount · coins) | O(amount) |
