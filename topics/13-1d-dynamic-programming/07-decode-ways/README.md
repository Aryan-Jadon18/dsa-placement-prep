# 91. Decode Ways

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-1D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20String-lightgrey)
**LeetCode:** https://leetcode.com/problems/decode-ways/

## Problem
A message of digits was encoded from letters using `'A' -> "1"`, `'B' -> "2"`, ..., `'Z' -> "26"`. Given the encoded digit string `s`, count how many distinct ways it could have been decoded back into letters.

**Input:** a string `s` of digits
**Output:** an integer — the number of valid decodings

**Examples:**
1. `s = "12"` → `2`. Decodes as `"AB"` (1, 2) or `"L"` (12).
2. `s = "226"` → `3`. Decodes as `"BZ"` (2, 26), `"VF"` (22, 6), or `"BBF"` (2, 2, 6).
3. `s = "06"` → `0`. A leading zero in any group is never a valid letter code (no letter maps to "0" or has a leading zero), so this string can't be decoded at all.

**Constraints:** `1 <= s.length <= 100`, `s` contains digits and may include `'0'`.

> 🔑 **Pattern Recognition**
> The number of decodings of a prefix depends only on the number of decodings of the one- and two-character-shorter prefixes before it (subject to validity checks) — a counting recurrence over prefix length, same rolling-two-state shape as Climbing Stairs but gated by digit-validity rules.

## Intuition (explained simply)
Reading left to right, at each position you decide: "do I decode the current digit alone, or pair it with the next digit?" A single digit is valid only if it's `1`-`9` (not `0`). A pair is valid only if it forms `10`-`26`. Every valid decoding is built from a sequence of these 1-digit or 2-digit choices.

### 1. Brute Force
- Plain recursion `ways(i)` = number of ways to decode `s[i:]`. If `s[i] != '0'`, add `ways(i+1)` (decode single digit). If `s[i:i+2]` forms a number between 10 and 26, add `ways(i+2)` (decode as a pair). Base case: `ways(n) = 1` (empty remainder means one valid — the "do nothing" — decoding).
- Correct because it tries every legal split of the remaining string at each position, recursively covering all decodings.
- Time complexity: O(2^n)  Space complexity: O(n) (recursion stack)
- Overlapping subproblems: `ways(k)` for the same `k` gets recomputed repeatedly from different earlier positions, causing exponential blowup.

### 2. Better
- Memoize `ways(i)` so each starting index is computed once (top-down DP).
- Same recursive logic and correctness, but cached.
- Time complexity: O(n)  Space complexity: O(n) cache + O(n) recursion stack
- Recursion overhead and stack depth are avoidable with an iterative bottom-up pass.

### 3. Optimal
- **DP state:** let `dp[i]` = the number of ways to decode the prefix `s[0..i-1]` (the first `i` characters). `dp[0] = 1` represents the empty prefix having exactly one (trivial) decoding.
- **Transition:** `dp[i] = dp[i-1]` (if `s[i-1] != '0'`, the last character stands alone) `+ dp[i-2]` (if `s[i-2:i]` forms a valid 10-26, the last two characters pair up). If neither condition holds, `dp[i] = 0` — that prefix has no valid decoding.
- Build up left to right from `dp[0], dp[1]` to `dp[n]`; since each state only needs the previous two, keep two rolling variables.
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: string starts with `'0'` → `dp[1] = 0`, and that zero propagates forward correctly, eventually making `dp[n] = 0` unless a later pairing rescues a segment; string with `"00"` anywhere → 0 ways since neither the single `'0'` nor a pair starting with `'0'` (`"0X"` is never 10-26) is valid.

#### 🎯 Visual Walkthrough
Worked example: `s = "226"` → `3`.

| i | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| prefix | "" | "2" | "22" | "226" |
| dp[i] | 1 | 1 | 2 | 3 |

`dp[i] = dp[i-1]` (if `s[i-1]!='0'`) `+ dp[i-2]` (if `s[i-2:i]` is 10-26). E.g. `dp[2] = dp[1] (single '2') + dp[0] (pair "22") = 1 + 1 = 2`, and `dp[3] = dp[2] (single '6') + dp[1] (pair "26") = 2 + 1 = 3`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
