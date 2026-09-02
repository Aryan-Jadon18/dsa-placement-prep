# 72. Edit Distance

**Difficulty:** Hard | **Pattern:** 2D DP — String Matching | **Tags:** DP, String
**LeetCode:** https://leetcode.com/problems/edit-distance/

## Problem
Given two strings `word1` and `word2`, find the minimum number of single-character edits (insert one character, delete one character, or replace one character) needed to turn `word1` into `word2`.

Input: strings `word1`, `word2`.
Output: an integer, the minimum edit count.

**Example 1:** `word1 = "horse", word2 = "ros"` → `3`. Replace `'h'`→`'r'` (`rorse`), delete `'r'` (`rose`), delete `'e'` (`ros`).

**Example 2:** `word1 = "intention", word2 = "execution"` → `5`. A known optimal sequence of 5 edits transforms one into the other.

**Example 3:** `word1 = "", word2 = "abc"` → `3`. Insert all 3 characters — there's no cheaper way to build a string from nothing.

Constraints: `0 <= word1.length, word2.length <= 500`. Both strings consist of lowercase English letters.

## Intuition (explained simply)
Compare the two strings from the end (or start) inward. Look at the last character of each: if they match, they don't need an edit — just solve the smaller problem of the strings without their last character. If they don't match, we must spend exactly one edit, and we have 3 choices for what that edit is, each of which reduces the problem to a smaller sub-problem: replace the last character (shrink both strings by 1), delete the last character of `word1` (shrink `word1` by 1, keep `word2`), or insert a character into `word1` to match `word2`'s last character (shrink `word2` by 1, keep `word1`). Take whichever of the 3 choices leads to the fewest total edits.

### 1. Brute Force
- Recurse on `(i, j)` = "remaining suffix problem for `word1[i:]` vs `word2[j:]`". If `word1[i] == word2[j]`, no edit needed here: `dfs(i+1, j+1)`. Otherwise, take `1 + min(dfs(i+1, j+1) [replace], dfs(i+1, j) [delete from word1], dfs(i, j+1) [insert into word1])`. Base cases: if one string is exhausted, the cost is however many characters remain in the other (all inserts or all deletes).
- Correct because it tries all 3 possible edit types at every point of divergence and takes the cheapest resulting path — this exactly mirrors how edit distance is defined.
- Time complexity: O(3^(m+n)) worst case (3-way branch at every mismatch). Space complexity: O(m+n) recursion depth.
- Exponential — completely infeasible for strings up to 500 characters.

### 2. Better
- The recursion's value depends only on `(i, j)` — memoize (top-down DP).
- Correctness is preserved (same recurrence), and now only `O(m*n)` distinct states are ever computed.
- Time complexity: O(m*n). Space complexity: O(m*n) for the memo + O(m+n) recursion stack.
- Recursion overhead and dictionary-based caching add constant-factor cost; an iterative table is simpler and avoids recursion-depth concerns for long strings.

### 3. Optimal
- Define `dp[i][j]` = minimum edits to convert `word1[:i]` (first `i` chars) into `word2[:j]` (first `j` chars). Base cases: `dp[i][0] = i` (delete all `i` characters to reach empty), `dp[0][j] = j` (insert all `j` characters to build the target from empty).
- Transition: if `word1[i-1] == word2[j-1]`, `dp[i][j] = dp[i-1][j-1]` (characters already match, no cost). Otherwise `dp[i][j] = 1 + min(dp[i-1][j-1] [replace], dp[i-1][j] [delete], dp[i][j-1] [insert])`. This is exactly the brute-force recurrence, filled bottom-up in increasing `i, j` order so all three dependencies are always ready.
- The answer is `dp[m][n]`. Since row `i` only depends on row `i-1` and the current row so far, space compresses to two rolling 1D rows (or one row updated carefully with a saved "top-left" scalar).
- Time complexity: O(m*n). Space complexity: O(min(m, n)) with the rolling-row trick (O(m*n) for the plain 2D table).
- Edge cases: one string empty → answer is the length of the other (all inserts or all deletes); identical strings → 0; completely disjoint characters → answer equals `max(m, n)` (replace up to the shorter length, then insert/delete the rest).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(3^(m+n)) | O(m+n) |
| Better | O(m*n) | O(m*n) |
| Optimal | O(m*n) | O(min(m,n)) |
