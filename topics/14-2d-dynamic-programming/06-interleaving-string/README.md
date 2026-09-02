# 97. Interleaving String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-2D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20String-lightgrey)
**LeetCode:** https://leetcode.com/problems/interleaving-string/

## Problem
Given three strings `s1`, `s2`, `s3`, determine whether `s3` can be formed by interleaving `s1` and `s2`. "Interleaving" means: merge the characters of `s1` and `s2` together, keeping the internal order of each string intact, to produce `s3` (you can pick the next character from either string at each step, but never reorder within a string).

Input: three strings `s1`, `s2`, `s3`.
Output: a boolean.

**Example 1:** `s1 = "aab", s2 = "axy", s3 = "aaaxby"` → `true`. Weave it as: `s1[0]='a'`, `s1[1]='a'`, `s2[0]='a'`, `s2[1]='x'`, `s1[2]='b'`, `s2[2]='y'` — reading off the picked characters in order gives exactly `"aaaxby"`, and both `s1` and `s2` were consumed left-to-right without skipping.

**Example 2:** `s1 = "abc", s2 = "xyz", s3 = "abcxzy"` → `false`. After consuming all of `s1` (`a,b,c`) and then `x` from `s2`, the next character of `s3` is `z` — but `s2`'s next required character is `y` (its own internal order is `x,y,z`), and `s1` is already exhausted, so no source can supply a `z` here.

**Example 3:** `s1 = "", s2 = "abc", s3 = "abc"` → `true`. `s3` is just `s2` alone.

Constraints: `0 <= s1.length, s2.length <= 100`, `s3.length == s1.length + s2.length`, all strings consist of lowercase English letters. (If `s3.length != s1.length + s2.length`, the answer is trivially `false`.)

> 🔑 **Pattern Recognition**
> Two sequences being merged/matched against a third, where position is fully described by how many characters have been consumed from each source (`i`, `j`) → a 2D DP grid indexed by both consumption pointers, since `i+j` always fixes the position in `s3`.

## Intuition (explained simply)
Think of building `s3` one character at a time. At each step, `s3`'s next character must come from either the next unused character of `s1` or the next unused character of `s2`. So the whole problem reduces to a "two-pointer" state: how many characters have we consumed from `s1` (`i`) and from `s2` (`j`)? Since `i + j` always equals how many characters of `s3` we've built so far, that pair `(i, j)` fully determines our position — this is a 2D DP over the grid of `(i, j)` pairs.

### 1. Brute Force
- Recurse on `(i, j)`: we've used `s1[:i]` and `s2[:j]`, which together must equal `s3[:i+j]`. Try consuming the next character from `s1` (if `s1[i] == s3[i+j]`) and/or from `s2` (if `s2[j] == s3[i+j]`), recursing into whichever is valid. Base case: `i == len(s1)` and `j == len(s2)` → success (`True`) if we've consumed everything.
- Correct because it explores every possible way of choosing, at each position of `s3`, which source string contributed that character.
- Time complexity: O(2^(m+n)) in the worst case — up to two branches at each of the `m+n` steps. Space complexity: O(m+n) recursion depth.
- Exponential blowup for the given constraints (100+100 characters) is intractable without caching.

### 2. Better
- The recursion's outcome depends only on `(i, j)` — memoize on that pair to avoid recomputing the same sub-problem via different call paths (top-down DP).
- Same correctness argument, now with each of the `(m+1)*(n+1)` states computed once.
- Time complexity: O(m*n). Space complexity: O(m*n) for the memo + O(m+n) recursion stack.
- Recursion overhead and a full memo dictionary/table are heavier than necessary; an iterative bottom-up table is both simpler and faster in practice.

### 3. Optimal
- Define `dp[i][j]` = `True` if `s3[:i+j]` can be formed by interleaving `s1[:i]` and `s2[:j]`. Base case `dp[0][0] = True` (two empty prefixes trivially interleave to an empty string).
- Fill the first row and first column first (using only one source string), then the rest of the table via the recurrence: `dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])` — "the last character of `s3[:i+j]` came from `s1` and the rest before it interleaved correctly, OR it came from `s2` and the rest before it interleaved correctly."
- This is exactly the brute-force recurrence evaluated iteratively in increasing `(i, j)` order so all dependencies are ready. The answer is `dp[m][n]`. Since row `i` only depends on row `i-1` and the current row, space can be compressed to a single rolling 1D boolean array.
- Time complexity: O(m*n). Space complexity: O(min(m, n)) with the rolling-row trick (O(m*n) for the plain 2D table).
- Edge cases: `len(s3) != len(s1) + len(s2)` → immediately `False` (a length mismatch can never interleave); either `s1` or `s2` empty → answer is just whether the other equals `s3`; repeated characters (e.g. all `'a'`s) are exactly where naive greedy "always prefer `s1`" fails and DP's exhaustive-but-cached check is required.

#### 🎯 Visual Walkthrough
Worked example: `s1 = "aab"`, `s2 = "axy"`, `s3 = "aaaxby"` → `true`.

| i \ j | "" | a | ax | axy |
|---|---|---|---|---|
| **""** | T | T | F | F |
| **a** | T | T | F | F |
| **aa** | T | T | T | F |
| **aab** | F | F | T | T |

`dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])`. The bottom-right cell `dp[3][3] = True` traces back through `dp[2][2]` (both `"aa"` from `s1` and `"a"` from `s2` consumed, matching `s3[:4]="aaax"`) — confirming `s3` can be woven from `s1` and `s2`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^(m+n)) | O(m+n) |
| Better | O(m*n) | O(m*n) |
| Optimal | O(m*n) | O(min(m,n)) |
