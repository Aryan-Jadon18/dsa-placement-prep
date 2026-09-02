# 115. Distinct Subsequences

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Pattern](https://img.shields.io/badge/Pattern-2D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20String-lightgrey)
**LeetCode:** https://leetcode.com/problems/distinct-subsequences/

## Problem
Given two strings `s` and `t`, count how many distinct ways `t` can be formed as a subsequence of `s` (delete zero or more characters of `s`, without reordering, to spell out `t`). Different sets of deleted positions count as different ways, even if the resulting characters look the same.

Input: strings `s` (source), `t` (target).
Output: an integer, the number of distinct subsequences of `s` equal to `t`.

**Example 1:** `s = "rabbbit", t = "rabbit"` → `3`. There are three distinct choices of which of the three `'b'`s to skip (positions of the three `b`s: keep any 2 of the 3, skip 1) that make `s` spell out `"rabbit"`.

**Example 2:** `s = "babgbag", t = "bag"` → `5`. Five distinct index combinations in `s` spell `"bag"`.

**Example 3:** `s = "abc", t = "abcd"` → `0`. `t` is longer than `s`, so it can never be a subsequence.

Constraints: `1 <= s.length, t.length <= 1000`. Both strings consist of English letters (case-sensitive).

> 🔑 **Pattern Recognition**
> Two strings walked together with pointers `(i, j)`, but *counting* ways instead of testing a yes/no match — the same 2D grid shape as LCS/Edit Distance, except transitions add contributions together rather than taking a max or a boolean OR.

## Intuition (explained simply)
Walk `s` and `t` together with two pointers `i` (into `s`) and `j` (into `t`). At each character of `s`, we have a *choice* if it matches the current target character: use it to match `t[j]` and advance both pointers, **or** skip it in `s` and hope a later occurrence of the same character does the matching instead. Because we're counting, both choices (when both are legal) contribute additively — this is why it's a *counting* DP rather than a yes/no DP like Interleaving String.

### 1. Brute Force
- Recurse on `(i, j)`: if `j == len(t)`, we've matched the whole target — count 1 way. If `i == len(s)` (ran out of source before matching t) — count 0 ways. Otherwise, always try "skip `s[i]`" (`dfs(i+1, j)`), and additionally, if `s[i] == t[j]`, also try "use `s[i]` to match `t[j]`" (`dfs(i+1, j+1)`) and add both counts together.
- Correct because every distinct subsequence-match corresponds to exactly one sequence of skip/use decisions as `i` scans left to right, and we sum over all of them.
- Time complexity: O(2^len(s)) worst case (skip-or-use branch at every position of `s`). Space complexity: O(len(s)) recursion depth.
- Exponential — with `s` up to 1000 characters this is nowhere near feasible.

### 2. Better
- The recursion's value depends only on `(i, j)` — memoize on that pair (top-down DP).
- Same recurrence, so correctness is preserved, and now each of the `O(len(s) * len(t))` states is computed once.
- Time complexity: O(len(s) * len(t)). Space complexity: O(len(s) * len(t)) for the memo + O(len(s)) recursion stack.
- Recursion depth up to 1000 plus dictionary/table overhead is more than needed; can be replaced by a clean iterative table.

### 3. Optimal
- Define `dp[i][j]` = number of distinct subsequences of `s[:i]` (first `i` characters of `s`) equal to `t[:j]` (first `j` characters of `t`). Base case: `dp[i][0] = 1` for all `i` (there's exactly one way to match an empty target — delete everything), and `dp[0][j] = 0` for `j > 0` (can't match a non-empty target from an empty source).
- Transition: `dp[i][j] = dp[i-1][j]` (always allowed: don't use `s[i-1]` to match anything) `+ dp[i-1][j-1]` **only if** `s[i-1] == t[j-1]` (additionally allowed: use `s[i-1]` to match `t[j-1]`). This mirrors the brute-force recursion exactly, filled bottom-up in increasing `i, j` order.
- The answer is `dp[len(s)][len(t)]`. Since row `i` only depends on row `i-1`, the space can be compressed to a single rolling 1D array of size `len(t)+1`, updated **right to left** within each row so that `dp[j-1]` still refers to the previous row's value when it's read.
- Time complexity: O(len(s) * len(t)). Space complexity: O(len(t)) with the rolling-row trick (O(len(s)*len(t)) for the plain 2D table).
- Edge cases: `t` longer than `s` → 0 (handled naturally, `dp` stays 0 in the unreachable region); `t` empty → 1 (the "delete everything" way); `s == t` → 1; repeated characters in `s` are exactly what produce counts greater than 1.

#### 🎯 Visual Walkthrough
Worked example: `s = "babgbag"`, `t = "bag"` → `5`.

| s \ t | "" | b | a | g |
|---|---|---|---|---|
| **""** | 1 | 0 | 0 | 0 |
| **b** | 1 | 1 | 0 | 0 |
| **a** | 1 | 1 | 1 | 0 |
| **b** | 1 | 2 | 1 | 0 |
| **g** | 1 | 2 | 1 | 1 |
| **b** | 1 | 3 | 1 | 1 |
| **a** | 1 | 3 | 4 | 1 |
| **g** | 1 | 3 | 4 | 5 |

`dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1]==t[j-1] else 0)`. Each row is `s`'s prefix growing by one character; the count only grows when that character matches the current target character. The bottom-right cell `dp[7][3] = 5` matches the answer.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^len(s)) | O(len(s)) |
| Better | O(len(s) * len(t)) | O(len(s) * len(t)) |
| Optimal | O(len(s) * len(t)) | O(len(t)) |
