# 10. Regular Expression Matching

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Pattern](https://img.shields.io/badge/Pattern-2D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20String%2C%20Recursion-lightgrey)
**LeetCode:** https://leetcode.com/problems/regular-expression-matching/

## Problem
Given a string `s` and a pattern `p` containing lowercase letters, `.` (matches any single character), and `*` (matches zero or more of the character *immediately preceding it* in the pattern), determine whether `p` matches the **entire** string `s`.

Input: strings `s`, `p`.
Output: a boolean.

**Example 1:** `s = "aa", p = "a*"` → `true`. `a*` means "zero or more `a`s," and it consumes both.

**Example 2:** `s = "ab", p = ".*"` → `true`. `.*` means "zero or more of any character," matching the whole string.

**Example 3:** `s = "mississippi", p = "mis*is*p*."` → `false`. No way to stretch the `*`-repeated groups to align the rest of the pattern with the full string.

Constraints: `1 <= s.length <= 20`, `1 <= p.length <= 30`. `s` contains only lowercase letters; `p` contains lowercase letters, `.`, and `*`; every `*` is preceded by a valid letter or `.` (no leading/dangling `*`).

> 🔑 **Pattern Recognition**
> Two sequences (string and pattern) walked together with pointers `(i, j)`, where whether `s[:i]` matches `p[:j]` depends on smaller `(i,j)` states — the same 2D grid shape as LCS/Edit Distance, complicated only by `*` letting a state reach back to `dp[i][j-2]` (skip) or `dp[i-1][j]` (repeat) instead of just the diagonal.

## Intuition (explained simply)
Walk `s` and `p` together with two pointers `i`, `j`. At each step there are only two shapes to consider: either the *next* pattern token is a plain character or `.` (no `*` following it), in which case it must match the current `s` character one-to-one and both pointers advance by one; or the next pattern token is followed by a `*`, which means that "character-then-star" unit can be used **zero times** (skip both pattern tokens, don't advance `s`) or **one-or-more times** (if it matches the current `s` character, consume one character of `s` and try the same pattern position again, since `*` allows repetition).

### 1. Brute Force
- Recurse on `(i, j)`: base case `j == len(p)` → match succeeds only if `i == len(s)` too (both fully consumed). Check if the *first* character currently matches: `first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')`. If the character *after* `p[j]` is `*`: try `dfs(i, j+2)` (use the starred group zero times) **or**, if `first_match`, `dfs(i+1, j)` (consume one `s` character, stay on the same starred pattern group to allow more repeats). Otherwise (no `*` follows): require `first_match` and recurse `dfs(i+1, j+1)`.
- Correct because it tries every legal way of consuming `*`-groups (any repeat count from 0 upward) and every plain character match, exactly matching the semantics of the regex operators given.
- Time complexity: O(2^(m+n)) worst case — repeated branching on whether to consume via the starred group. Space complexity: O(m+n) recursion depth.
- Exponential; even with the small constraints here (`s` up to 20, `p` up to 30) it can be slow without caching due to overlapping subproblems, and it's the wrong approach to present in an interview.

### 2. Better
- The recursion's outcome depends only on `(i, j)` — memoize on that pair (top-down DP).
- Correctness preserved, same recurrence, now only `O(m*n)` distinct states are computed.
- Time complexity: O(m*n). Space complexity: O(m*n) for the memo + O(m+n) recursion stack.
- Recursion depth and dictionary overhead are avoidable; an iterative table handles the same recurrence more predictably (no Python recursion-limit risk on pathological patterns).

### 3. Optimal
- Define `dp[i][j]` = `True` if `s[:i]` (first `i` characters of `s`) matches `p[:j]` (first `j` characters of `p`) **completely**. Base case `dp[0][0] = True` (empty matches empty). Precompute the first row (`i == 0`): `dp[0][j] = True` only if `p[:j]` can match empty, which happens exactly when `p[j-1] == '*'` and `dp[0][j-2]` was already `True` (a starred group can vanish).
- Transition for `dp[i][j]` (`i, j >= 1`): let `pc = p[j-1]`. If `pc != '*'`: `dp[i][j] = dp[i-1][j-1] and (pc == s[i-1] or pc == '.')`. If `pc == '*'` (so it applies to `p[j-2]`): `dp[i][j] = dp[i][j-2]` (zero occurrences) `or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'))` (one more occurrence, reusing the same starred pattern position against the previous `s` character).
- This is exactly the brute-force recurrence, filled iteratively for increasing `i, j` so every dependency is ready. The answer is `dp[m][n]`. Space can be compressed to two rolling rows since row `i` only needs row `i-1` and the current row.
- Time complexity: O(m*n). Space complexity: O(n) with the rolling-row trick (O(m*n) for the plain 2D table).
- Edge cases: empty pattern with non-empty `s` → false; pattern that's entirely `x*y*z*`-style (can match empty `s`) → check row 0 carefully; `.*` at the end matches any suffix; a `*` can only ever apply to the single token right before it, never chain.

#### 🎯 Visual Walkthrough
Worked example: `s = "aa"`, `p = "a*"` → `true`.

| s \ p | "" | a | a* |
|---|---|---|---|
| **""** | T | F | T |
| **a** | F | T | T |
| **aa** | F | F | T |

Row 0: `dp[0][2] = True` because `p[1]='*'` lets `"a*"` vanish (zero occurrences) and `dp[0][0]=True`. For `dp[2][2]` (`pc='*'` applying to `'a'`): `dp[2][2] = dp[2][0] (False, zero occurrences)` OR `dp[1][2] (True) and p[0]='a'==s[1]='a'` → `True` — one more `'a'` consumed by the starred group, matching both characters of `s`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^(m+n)) | O(m+n) |
| Better | O(m*n) | O(m*n) |
| Optimal | O(m*n) | O(n) |
