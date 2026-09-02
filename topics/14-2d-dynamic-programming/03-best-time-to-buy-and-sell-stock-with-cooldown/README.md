# 309. Best Time to Buy and Sell Stock with Cooldown

**Difficulty:** Medium | **Pattern:** State Machine DP | **Tags:** DP
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

## Problem
You're given the price of one stock on each of `n` days. You may buy and sell as many times as you like (one share at a time — you must sell before buying again), but after you sell, you must wait one full day of "cooldown" before you're allowed to buy again. Maximize total profit.

Input: `prices`, a list of integers (price per day).
Output: an integer, the maximum achievable profit.

**Example 1:** `prices = [1,2,3,0,2]` → `3`. Buy on day 0 (price 1), sell on day 1 (price 2, profit 1), cooldown on day 2, buy on day 3 (price 0), sell on day 4 (price 2, profit 2). Total: 3.

**Example 2:** `prices = [1]` → `0`. Can't sell what you never bought and sold in the same single day; no transaction is possible.

**Example 3:** `prices = [1,4,2]` → `3`. Buy at 1, sell at 4.

Constraints: `1 <= prices.length <= 5000`, `0 <= prices[i] <= 1000`.

## Intuition (explained simply)
At any moment you are in exactly one of a few "states": holding a share, or not holding one (and if you just sold, you're forced into cooldown before you can buy again). Each day you choose an action that's legal for your current state, and that choice moves you to a new state. This "state + transition" shape is exactly what a state-machine DP models — at each day, track the best profit achievable while ending the day in each possible state.

### 1. Brute Force
- Recurse on `(day, holding)`: if not holding, you may either skip the day, or buy (pay `prices[day]`, move to `holding=True`, advance one day). If holding, you may either skip, or sell (gain `prices[day]`, but then the *next* day is forced cooldown, so you jump ahead two days before you're free to act again). Take the best of the available options at each call.
- Correct because it enumerates literally every legal sequence of buy/sell/cooldown/skip decisions.
- Time complexity: O(2^n) — branches on each day. Space complexity: O(n) recursion depth.
- Exponential; way too slow for `n` up to 5000.

### 2. Better
- The recursion's result only depends on `(day, holding)`, and there are only `2n` such pairs, so memoize on that pair (top-down DP).
- Same recurrence, so correctness is preserved; now each state is computed once.
- Time complexity: O(n). Space complexity: O(n) for the memo table + O(n) recursion stack.
- Recursion overhead and an explicit cache are unnecessary — the same answer can be built iteratively with a handful of variables.

### 3. Optimal
- Track three running values as we scan left to right, one per day:
  - `hold` = best profit ending today while holding a share.
  - `sold` = best profit ending today having just sold a share today (so tomorrow is forced cooldown).
  - `rest` = best profit ending today while not holding and not in a forced cooldown (free to buy tomorrow).
- Transitions per day using **yesterday's** values: `new_hold = max(hold, rest - price)` (keep holding, or buy today from a resting state); `new_sold = hold + price` (sell what we were holding); `new_rest = max(rest, sold)` (stay resting, or yesterday's cooldown just ended).
- This works because `rest` already encodes "either never bought, or finished cooldown," so `rest - price` is always a legal buy, and `sold` feeding into tomorrow's `rest` is exactly what enforces the one-day cooldown rule.
- Time complexity: O(n) — single pass. Space complexity: O(1) — three scalars.
- Edge cases: `n == 1` → no transaction possible, answer 0 (all values stay 0/-price and the max lands on 0); strictly decreasing prices → never buy, answer 0; all identical prices → 0 profit either way.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
