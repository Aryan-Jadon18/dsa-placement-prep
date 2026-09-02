# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy | **Pattern:** Sliding Window — Single Pass | **Tags:** Array, DP
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Problem
You're given an array of daily stock prices. You may buy the stock on exactly one day and sell it on a later day, and you want to know the maximum profit you can make. If no profit is possible, return 0.

- **Input:** an array of integers `prices`, where `prices[i]` is the price on day `i`.
- **Output:** a single integer — the maximum achievable profit (buy before you sell).

**Examples**
1. `prices = [7,1,5,3,6,4]` → `5`. Buy on day 1 (price 1), sell on day 4 (price 6): profit `6 - 1 = 5`.
2. `prices = [7,6,4,3,1]` → `0`. Prices only fall, so no transaction is profitable — hold cash, return 0.
3. `prices = [2,4,1]` → `2`. Buy at 2, sell at 4 for profit 2 (buying at 1 later doesn't help since it's the last day).

**Constraints:** `1 <= prices.length <= 10^5`, `0 <= prices[i] <= 10^4`.

## Intuition (explained simply)

### 1. Brute Force
- For every possible buy day, try every possible later sell day, and track the best profit seen. This is literally "try everything."
- Correct because it exhaustively checks every valid (buy, sell) pair with buy before sell.
- Time complexity: O(n²)  Space complexity: O(1)
- Way too slow once `n` approaches `10^5` — a nested loop of that size times out.

### 2. Better
- Instead of two nested loops, precompute the maximum price seen *from each day onward* (a suffix-max array), then for each buy day just look up the best future sell price in O(1).
- Still correct: for each day `i`, the best possible sell is the max price among days after `i`, which we've precomputed.
- Time complexity: O(n)  Space complexity: O(n) for the suffix array.
- We've dropped to linear time, but we're spending extra memory on an array we don't strictly need — an interviewer will ask you to shrink the space.

### 3. Optimal
- Walk through the prices once, keeping track of the **minimum price seen so far** (the cheapest place we could have bought). At each day, ask "if I sold today, what profit would I get given the cheapest buy so far?" and keep the best of those profits.
- This works because the minimum-so-far is always a valid buy day that occurred before the current (sell) day — we never need to look back further than "the cheapest point so far."
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: empty or single-element array → profit 0; strictly decreasing prices → profit 0 (never let profit go negative, just skip an update).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n²) | O(1) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
