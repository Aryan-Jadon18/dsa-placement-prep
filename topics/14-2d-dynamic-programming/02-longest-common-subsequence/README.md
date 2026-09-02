# 1143. Longest Common Subsequence

**Difficulty:** Medium | **Pattern:** 2D DP — String Matching | **Tags:** DP, String
**LeetCode:** https://leetcode.com/problems/longest-common-subsequence/

## Problem
Given two strings, find the length of their longest common subsequence (LCS) — a sequence that appears in both strings in the same relative order, but not necessarily contiguously. If there is no common subsequence, return 0.

Input: two strings `text1`, `text2`.
Output: an integer, the length of the LCS.

**Example 1:** `text1 = "abcde"`, `text2 = "ace"` → `3`. `"ace"` is a subsequence of both.

**Example 2:** `text1 = "abc"`, `text2 = "abc"` → `3`. The whole string matches.

**Example 3:** `text1 = "abc"`, `text2 = "def"` → `0`. No characters overlap in order.

Constraints: `1 <= text1.length, text2.length <= 1000`. Strings contain only lowercase English letters.

## Intuition (explained simply)
A "subsequence" means you can delete characters (keeping order) but can't reorder. To compare two strings character by character, walk both from the end (or start): if the last characters match, that character is definitely part of some LCS — extend the answer for the rest of both strings by 1. If they don't match, the LCS must skip the last character of *one* of the two strings, so try both and take the max.

### 1. Brute Force
- Recurse with two pointers `i`, `j` (positions in `text1`, `text2`). If `text1[i] == text2[j]`, add 1 and recurse on `(i+1, j+1)`. Otherwise, try skipping a character from either string: `max(lcs(i+1, j), lcs(i, j+1))`.
- Correct because it explores every possible way of aligning subsequences of the two strings.
- Time complexity: O(2^(m+n)) in the worst case (two branches per mismatched call). Space complexity: O(m+n) recursion depth.
- Exponential blowup — completely impractical once strings are more than ~20 characters.

### 2. Better
- The recursion only ever depends on the pair `(i, j)`, and there are only `m*n` distinct pairs — so memoize on `(i, j)` to avoid recomputation.
- Correctness carries over directly since it's the same recurrence, just cached.
- Time complexity: O(m*n). Space complexity: O(m*n) for the memo table + O(m+n) recursion stack.
- Recursion overhead and a full 2D cache are more than needed; deep recursion can also hit Python's recursion limit for long strings.

### 3. Optimal
- Define `dp[i][j]` = length of the LCS of `text1[0:i]` and `text2[0:j]` (the first `i` characters of `text1` and the first `j` characters of `text2`). Build it bottom-up with a 2D table sized `(m+1) x (n+1)`, where row/col 0 represent empty prefixes (base case `dp[0][*] = dp[*][0] = 0`).
- Transition: if `text1[i-1] == text2[j-1]`, then `dp[i][j] = dp[i-1][j-1] + 1` (extend the match found in the smaller prefixes). Otherwise `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (drop the last character of whichever string doesn't help).
- This is exactly the brute-force recurrence, just filled iteratively in order of increasing `i, j` so every value it depends on already exists. The answer is `dp[m][n]`. Space can be trimmed to two rolling rows since row `i` only needs row `i-1`.
- Time complexity: O(m*n). Space complexity: O(min(m, n)) with the rolling-row trick (O(m*n) if using the full table).
- Edge cases: one string empty → LCS is 0; no overlap → 0; identical strings → length of the string.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^(m+n)) | O(m+n) |
| Better | O(m*n) | O(m*n) |
| Optimal | O(m*n) | O(min(m,n)) |
