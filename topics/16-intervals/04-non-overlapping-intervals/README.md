# 435. Non-overlapping Intervals

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Pattern](https://img.shields.io/badge/Pattern-Interval%20Scheduling-blue)
![Tags](https://img.shields.io/badge/Tags-Array%2C%20Sorting%2C%20Greedy%2C%20Intervals-lightgrey)

**LeetCode:** https://leetcode.com/problems/non-overlapping-intervals/

## Problem
Given a list of intervals, find the minimum number of intervals you must remove so that none of the remaining intervals overlap each other.

**Input:** `intervals: List[List[int]]`, each `[start, end]`.
**Output:** an integer — the minimum removals needed.

**Example 1:**
`intervals = [[1,2],[2,3],[3,4],[1,3]]` → `1`
Remove `[1,3]` and the rest (`[1,2],[2,3],[3,4]`) don't overlap (touching endpoints are fine).

**Example 2:**
`intervals = [[1,2],[1,2],[1,2]]` → `2`
All three are identical and pairwise overlap, so you must remove two of them, keeping just one.

**Example 3:**
`intervals = [[1,2],[2,3]]` → `0`
They only touch at `2`, which doesn't count as overlapping — nothing needs removing.

**Constraints:** `1 <= intervals.length <= 10^5`, `-5*10^4 <= start < end <= 5*10^4`.

> **🔑 Pattern Recognition:** Overlapping ranges + "minimize removals" → classic activity-selection greedy: sort by **end** time, always keep whichever candidate finishes earliest to leave the most room for the rest.

## Intuition (explained simply)
This is really "keep the maximum number of non-overlapping intervals" in disguise — if you keep `k` intervals out of `n`, you removed `n - k`. To keep as many as possible, a classic greedy trick works: always keep whichever interval **ends earliest** among the candidates, because ending early leaves the most room for future intervals.

### 1. Brute Force
- For each interval, recursively try both "keep it" and "remove it," making sure kept intervals never overlap, and take whichever branch keeps the most intervals. This explores every possible subset.
- Correct because it literally checks all possibilities.
- Time complexity: O(2ⁿ)  Space complexity: O(n) recursion depth
- Why it's not good enough: exponential blow-up — completely infeasible once n gets past ~20, let alone 10⁵.

### 2. Better
- Sort intervals by start time. Use dynamic programming: `dp[i]` = the maximum number of non-overlapping intervals achievable using only intervals `0..i` and ending the chain at interval `i`. For each `i`, look back at every `j < i` whose interval doesn't overlap interval `i`, and take `dp[i] = max(dp[j]) + 1`. The answer is `n - max(dp)`.
- This is correct (a cleaner reformulation of "longest chain of compatible intervals," similar to Longest Increasing Subsequence) and avoids trying every subset, but it still checks each pair of intervals.
- Time complexity: O(n²)  Space complexity: O(n)
- Still too slow for n = 10⁵.

### 3. Optimal
- Sort intervals by **end** time (not start!). Walk through greedily, keeping a `last_end` pointer initialized to -infinity. For each interval: if its start is `>= last_end`, it's compatible — keep it and update `last_end` to its end. Otherwise it overlaps the last kept interval — count it as a removal and skip it (don't update `last_end`, since we want to keep the earliest-ending option available).
- Why it works: this is the classic "activity selection" greedy — always preferring the interval that frees up the earliest end time is provably optimal (an exchange argument: any optimal solution can be transformed to also pick the earliest-ending compatible interval without doing worse).
- Time complexity: O(n log n) (sort dominates; the greedy pass is O(n))  Space complexity: O(1) extra (O(n) or O(log n) for the sort itself, depending on implementation)
- Edge cases: single interval → 0 removals; all identical intervals → keep 1, remove the rest; already non-overlapping → 0 removals; touching endpoints (`end == next start`) do **not** count as overlap.

#### 🎯 Visual Walkthrough
Tracing `intervals = [[1,2],[2,3],[3,4],[1,3]]` (Example 1, answer `1`), sorted by **end** time:

| Interval | Start | End | `last_end` before | Decision |
|---|---|---|---|---|
| `[1,2]` | 1 | 2 | -∞ | `1 >= -∞` → keep, `last_end=2` |
| `[2,3]` | 2 | 3 | 2 | `2 >= 2` → keep, `last_end=3` |
| `[1,3]` | 1 | 3 | 3 | `1 < 3` → **overlap, remove** (count=1) |
| `[3,4]` | 3 | 4 | 3 | `3 >= 3` → keep, `last_end=4` |

Only `[1,3]` needs removing → answer `1`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2ⁿ) | O(n) |
| Better | O(n²) | O(n) |
| Optimal | O(n log n) | O(1) |
