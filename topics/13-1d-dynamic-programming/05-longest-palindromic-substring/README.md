# 5. Longest Palindromic Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-String%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20Two%20Pointers%2C%20String-lightgrey)
**LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/

## Problem
Given a string `s`, find the longest contiguous substring of `s` that reads the same forwards and backwards.

**Input:** a string `s`
**Output:** a string — the longest palindromic substring (if there's a tie, any one of them is accepted)

**Examples:**
1. `s = "babad"` → `"bab"` (or `"aba"`, both length 3 and both valid).
2. `s = "cbbd"` → `"bb"`.
3. `s = "a"` → `"a"` (a single character is trivially a palindrome).

**Constraints:** `1 <= s.length <= 1000`, `s` consists of digits and English letters.

> 🔑 **Pattern Recognition**
> Whether `s[i..j]` is a palindrome depends only on whether `s[i]==s[j]` and whether the smaller inner substring `s[i+1..j-1]` is itself a palindrome — a range-shrinking recurrence over pairs of indices in a single string, the hallmark of string interval DP.

## Intuition (explained simply)
A palindrome mirrors around its center. A center can either be a single character (odd-length palindrome, like `"aba"`) or the gap between two characters (even-length palindrome, like `"abba"`). If we know whether a smaller substring inside `s` is a palindrome, we can often decide a bigger one is a palindrome too just by checking its two new outer characters match.

### 1. Brute Force
- Check every possible substring `s[i:j]` and test if it's a palindrome by comparing it to its reverse; track the longest one found.
- Correct because it's an exhaustive search over all O(n^2) substrings, and each is verified directly.
- Time complexity: O(n^3) (O(n^2) substrings, O(n) to check each)  Space complexity: O(1) extra (excluding output)
- Way too slow for `n = 1000` — a lot of redundant re-checking of palindrome-ness for overlapping substrings.

### 2. Better
- **DP state:** `dp[i][j]` = `True` if `s[i..j]` (inclusive) is a palindrome, else `False`.
- **Transition:** `dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]` (with the inner substring being empty or a single char treated as automatically `True`). This is memoized recursion (top-down): we ask "is `s[i..j]` a palindrome?" which recursively asks about the smaller inner range, and cache each `(i, j)` pair's answer.
- Correct because a substring is a palindrome exactly when its two ends match *and* the part strictly inside is also a palindrome — this is the natural recursive definition of a palindrome.
- Time complexity: O(n^2) states, each O(1) work after caching  Space complexity: O(n^2) for the memo table + recursion stack
- The 2D memo table costs real memory, and recursion has call overhead; we can compute this bottom-up instead, and there's an even simpler linear-space technique specific to this problem (expand around center).

### 3. Optimal
- **Core insight:** instead of filling a full 2D DP table, exploit that every palindrome has a center. There are `2n - 1` possible centers (n single-character centers + n-1 between-character centers). For each center, expand outward one step at a time while the two sides keep matching — the moment they stop matching, you've found the longest palindrome for that center.
- **Why it works:** this is really the same DP recurrence (`dp[i][j]` depends on `dp[i+1][j-1]`) but computed "outward" from small palindromes to large ones instead of filling a table — expansion IS the base-case-to-general-case direction of the DP, we just don't need to store all `(i,j)` pairs, only track the best-so-far.
- Try both odd centers (`center = i`) and even centers (`center = i, i+1`) for every index `i`, expanding as far as possible each time, and keep the longest span seen.
- Time complexity: O(n^2) (n centers, each expansion up to O(n))  Space complexity: O(1) extra (excluding output)
- Edge cases: single character string (answer is that character), all identical characters (whole string is the answer), no palindrome longer than 1 (any single character is still a valid length-1 answer).

#### 🎯 Visual Walkthrough
The `dp[i][j]` table (from approach 2) makes the underlying recurrence easiest to see. Worked example: `s = "cbbd"` → `"bb"`.

| i \ j | 0: c | 1: b | 2: b | 3: d |
|---|---|---|---|---|
| **0: c** | T | F | F | F |
| **1: b** |  | T | T | F |
| **2: b** |  |  | T | F |
| **3: d** |  |  |  | T |

`dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]`. The only `True` cell spanning more than one character is `dp[1][2]` (`s[1..2] = "bb"`), since `s[1]==s[2]=='b'`. The optimal (expand-around-center) approach finds this same span without materializing the full table — by expanding outward from center `(1,2)` until the characters stop matching.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^3) | O(1) |
| Better | O(n^2) | O(n^2) |
| Optimal | O(n^2) | O(1) |
