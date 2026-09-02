# 518. Coin Change II

**Difficulty:** Medium | **Pattern:** Unbounded Knapsack DP | **Tags:** DP
**LeetCode:** https://leetcode.com/problems/coin-change-ii/

## Problem
You have an unlimited supply of coins in a few denominations and a target amount. Count how many *distinct combinations* of coins add up exactly to that amount. Order doesn't matter — using a nickel then a dime is the same combination as a dime then a nickel.

Input: `amount` (target integer), `coins` (list of distinct positive coin denominations).
Output: an integer, the number of combinations that sum to `amount`.

**Example 1:** `amount = 5, coins = [1,2,5]` → `4`. The combinations are `5=5`, `5=2+2+1`, `5=2+1+1+1`, `5=1+1+1+1+1`.

**Example 2:** `amount = 3, coins = [2]` → `0`. No combination of 2's sums to 3.

**Example 3:** `amount = 0, coins = [1,2,3]` → `1`. The empty combination (use no coins) is the one way to make 0.

Constraints: `1 <= coins.length <= 300`, `1 <= coins[i] <= 5000`, coins are all unique, `0 <= amount <= 5000`.

## Intuition (explained simply)
This is a *counting* knapsack problem, not an optimization one: instead of minimizing coins used, we count how many distinct ways to build the target. Because each coin type is unlimited, this is an "unbounded knapsack" — each coin can be reused any number of times. The tricky part that trips people up: we must count *combinations* (unordered), not *permutations* (ordered) — `[1,2]` and `[2,1]` should count once, not twice — and that constrains how we structure the loop.

### 1. Brute Force
- Recurse over `(coin_index, remaining_amount)`: for the current coin, decide how many copies of it to use (0, 1, 2, ... as long as it doesn't exceed `remaining_amount`), then move to the next coin index. Summing the results of all these choices, restricted to strictly increasing coin index between "groups," naturally avoids double-counting reordered combinations.
- A simpler equivalent recursion: `ways(i, remaining) = ways(i+1, remaining) [skip coin i entirely] + ways(i, remaining - coins[i]) [use one more of coin i]`, with base cases `remaining == 0 → 1 way`, `remaining < 0` or `i == len(coins) → 0 ways`. This is correct because every combination either uses zero of coin `i` (handled by "skip") or at least one (handled by "use one more, still allowed to use coin `i` again").
- Time complexity: O(2^amount) in the worst case (each call branches in two, depth roughly `amount`). Space complexity: O(amount) recursion depth.
- Exponential — far too slow once `amount` is more than a few dozen.

### 2. Better
- The recursion's value depends only on `(i, remaining)`, and there are only `len(coins) * (amount+1)` such pairs — memoize on that pair (top-down DP).
- Correctness is unchanged, same recurrence, cached.
- Time complexity: O(len(coins) * amount). Space complexity: O(len(coins) * amount) for the memo + O(amount) recursion stack.
- Recursion depth can get large (up to `amount`), and the explicit 2D cache uses more memory than necessary.

### 3. Optimal
- Define `dp[x]` = number of combinations that sum exactly to `x`, using only coins considered *so far*. Initialize `dp[0] = 1` (one way to make 0: use nothing), all else 0.
- The critical trick for combinations-not-permutations: loop over **coins in the outer loop**, and amounts in the inner loop, ascending. For each coin, update `dp[x] += dp[x - coin]` for `x` from `coin` up to `amount`. Because a whole coin is "settled" (its outer loop fully finishes) before moving to the next coin, every combination gets built in one fixed canonical coin order (smallest-index coins introduced first), so each distinct multiset of coins is counted exactly once. (If the loops were swapped — amount outside, coins inside — the same multiset could be reached via different orderings and get double-counted, which instead solves the *permutations* version of this problem.)
- This is the standard unbounded-knapsack counting DP, computed iteratively bottom-up with a single 1D array, reused for every coin.
- Time complexity: O(len(coins) * amount). Space complexity: O(amount) — a single 1D array.
- Edge cases: `amount == 0` → answer is 1 (the empty combination); `coins` empty → answer is 1 if `amount == 0` else 0; no coin combination reaches `amount` → answer is 0.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^amount) | O(amount) |
| Better | O(len(coins) * amount) | O(len(coins) * amount) |
| Optimal | O(len(coins) * amount) | O(amount) |
