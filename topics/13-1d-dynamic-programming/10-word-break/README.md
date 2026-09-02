# 139. Word Break

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-1D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20String%2C%20Trie-lightgrey)
**LeetCode:** https://leetcode.com/problems/word-break/

## Problem
Given a string `s` and a dictionary of words `wordDict`, determine whether `s` can be segmented into a sequence of one or more dictionary words placed back-to-back (words may be reused any number of times).

**Input:** a string `s`, a list of strings `wordDict`
**Output:** a boolean — `true` if `s` can be fully segmented using dictionary words

**Examples:**
1. `s = "leetcode"`, `wordDict = ["leet", "code"]` → `true`. `"leet" + "code"`.
2. `s = "applepenapple"`, `wordDict = ["apple", "pen"]` → `true`. `"apple" + "pen" + "apple"` (reusing "apple").
3. `s = "catsandog"`, `wordDict = ["cats", "dog", "sand", "and", "cat"]` → `false`. No combination covers the whole string (`"catsandog"` always leaves a leftover chunk like `"og"` that isn't a word).

**Constraints:** `1 <= s.length <= 300`, `1 <= wordDict.length <= 1000`, all strings consist of lowercase letters, `wordDict` has no duplicates.

> 🔑 **Pattern Recognition**
> Whether a prefix of `s` is segmentable depends on whether some shorter prefix is segmentable AND the remaining chunk is a dictionary word — a boolean reachability recurrence over string prefixes, indexed by a single position → 1D DP.

## Intuition (explained simply)
Think of walking through `s` from the left. At each position you ask: "can I reach here using dictionary words, and if so, is there a dictionary word starting right here that reaches further?" If the prefix up to some point is breakable, and the next chunk is a real word, then the longer prefix is breakable too.

### 1. Brute Force
- Plain recursion `canBreak(i)`: if `i == len(s)`, we've consumed the whole string successfully — return `True`. Otherwise, try every dictionary word `w`; if `s` starts with `w` at position `i`, recurse on `canBreak(i + len(w))`. Return `True` if any branch succeeds.
- Correct because it exhaustively tries every possible way to peel a valid dictionary word off the front of the remaining string.
- Time complexity: O(2^n) in the worst case (each position can branch into multiple word choices)  Space complexity: O(n) recursion stack
- The same starting index `i` gets explored repeatedly through different word-choice paths — classic overlapping subproblems.

### 2. Better
- Memoize `canBreak(i)` so each starting index's answer (breakable or not) is computed once (top-down DP).
- Same correctness argument, but cached.
- Time complexity: O(n^2 * k) where `k` is average word length checked per position (or O(n^2) if using a word set and checking substrings up to max word length) — bounded by trying each of `n` positions against the dictionary  Space complexity: O(n) cache + O(n) recursion stack
- Recursion overhead remains; an iterative bottom-up scan avoids it and is simpler to reason about.

### 3. Optimal
- **DP state:** let `dp[i]` = `True` if the prefix `s[0..i-1]` (the first `i` characters) can be fully segmented into dictionary words, else `False`. `dp[0] = True` (empty prefix is trivially segmentable).
- **Transition:** for each `i` from `1` to `n`, check every `j < i`: if `dp[j]` is `True` and `s[j:i]` is in the dictionary (word set), then `dp[i] = True`.
- Using a hash set for `wordDict` makes each substring lookup O(1) (after O(len) to build/compare the substring). Build `dp` left to right; the final answer is `dp[n]`.
- Time complexity: O(n^2) (n positions × up to n split points, substring slicing costs add a bounded factor)  Space complexity: O(n) for the `dp` array
- Edge cases: empty dictionary → only `s = ""` would work, but constraints guarantee `s` is non-empty so answer is `false`; single-character words covering everything; a word longer than `s` in the dictionary (simply never matches, ignored naturally).

#### 🎯 Visual Walkthrough
Worked example: `s = "leetcode"`, `wordDict = ["leet", "code"]` → `true`.

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| prefix | "" | l | le | lee | leet | leetc | leetco | leetcod | leetcode |
| dp[i] | T | F | F | F | T | F | F | F | T |

`dp[4] = True` because `dp[0]=True` and `s[0:4]="leet"` is in the dictionary. `dp[8] = True` because `dp[4]=True` and `s[4:8]="code"` is in the dictionary — so the whole string breaks as `"leet" + "code"`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n^2) | O(n) |
| Optimal | O(n^2) | O(n) |
