# 70. Climbing Stairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Pattern](https://img.shields.io/badge/Pattern-1D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20Math-lightgrey)
**LeetCode:** https://leetcode.com/problems/climbing-stairs/

## Problem
You're climbing a staircase with `n` steps. Each move you can go up either 1 step or 2 steps. Count how many distinct sequences of moves get you to the top.

**Input:** an integer `n` (number of steps)
**Output:** an integer — the number of distinct ways to reach step `n`

**Examples:**
1. `n = 2` → `2`. Ways: `[1,1]`, `[2]`.
2. `n = 3` → `3`. Ways: `[1,1,1]`, `[1,2]`, `[2,1]`.
3. `n = 5` → `8`. Follows the pattern `ways(n) = ways(n-1) + ways(n-2)`.

**Constraints:** `1 <= n <= 45`.

> 🔑 **Pattern Recognition**
> The answer at step `n` is built entirely from the answers at `n-1` and `n-2` — a choice today depends only on results already computed for smaller subproblems, with those subproblems overlapping heavily as `n` grows. That "current state = combination of a fixed number of prior states" shape is the classic Fibonacci-style 1D DP cue.

## Intuition (explained simply)
To reach step `n`, your very last move was either a single step from step `n-1`, or a double step from step `n-2`. So the total ways to reach `n` is the sum of ways to reach those two earlier steps. That recursive idea is the whole problem.

### 1. Brute Force
- Plain recursion: `climb(n) = climb(n-1) + climb(n-2)`, with base cases `climb(0) = 1` (one way to "stay put") and `climb(1) = 1`.
- Correct because every path to `n` decomposes into a path to `n-1` plus a final 1-step, or a path to `n-2` plus a final 2-step, and these two cases never overlap.
- Time complexity: O(2^n)  Space complexity: O(n) (recursion stack)
- The same subproblems (e.g. `climb(5)`) get recomputed many times from different branches — this is the classic overlapping-subproblems blowup, exponential and useless past `n ≈ 35`.

### 2. Better
- Add memoization: cache the result of `climb(k)` the first time it's computed, and return the cached value on repeat calls (top-down DP).
- Still correct — same recursion, just computed once per distinct `k`.
- Time complexity: O(n)  Space complexity: O(n) for the cache + O(n) recursion stack
- Still pays for function-call overhead and stack depth; we don't actually need the whole cache, just the last two values.

### 3. Optimal
- **DP state:** let `dp[i]` = number of distinct ways to reach step `i`.
- **Transition:** `dp[i] = dp[i-1] + dp[i-2]`, since the last move into step `i` was either a 1-step (from `i-1`) or a 2-step (from `i-2`).
- Build it bottom-up from `dp[0]=1, dp[1]=1` up to `dp[n]`. Since each `dp[i]` only needs the previous two values, keep just two rolling variables instead of a full array.
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: `n = 1` → answer `1`; `n = 0` isn't in the constraint range but the two-variable base case handles it gracefully as `1`.

#### 🎯 Visual Walkthrough
Worked example: `n = 5` → `8` ways.

| i | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| dp[i] | 1 | 1 | 2 | 3 | 5 | 8 |

Recurrence: `dp[i] = dp[i-1] + dp[i-2]` — e.g. `dp[5] = dp[4] + dp[3] = 5 + 3 = 8`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
