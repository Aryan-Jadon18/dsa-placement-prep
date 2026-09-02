# 125. Valid Palindrome

**Difficulty:** Easy | **Pattern:** Two Pointers | **Tags:** String, Two Pointers
**LeetCode:** https://leetcode.com/problems/valid-palindrome/

## Problem
Given a string, decide whether it reads the same forwards and backwards after we ignore anything that isn't a letter or digit and ignore letter case.

**Input:** a string `s` (may contain letters, digits, spaces, punctuation)
**Output:** a boolean — `true` if the cleaned-up string is a palindrome, `false` otherwise

**Examples:**
1. `s = "A man, a plan, a canal: Panama"` → `true` — stripped down to `amanaplanacanalpanama`, which reads the same both ways.
2. `s = "race a car"` → `false` — stripped down to `raceacar`, which is not a palindrome.
3. `s = " "` → `true` — after removing the space there's nothing left, and an empty string is trivially a palindrome.

**Constraints:** `1 <= s.length <= 2*10^5`, `s` consists of printable ASCII characters.

## Intuition

### 1. Brute Force
- Build a cleaned string by filtering out non-alphanumeric characters and lowercasing the rest, then compare it to its own reverse. Correct because a palindrome is by definition equal to its reverse.
- Time complexity: O(n)  Space complexity: O(n) (cleaned string + its reverse)
- Not actually asymptotically bad, but it does two full passes and allocates two extra strings, which an interviewer will push you to trim down with two pointers and O(1) extra space.

### 2. Better
- Build the cleaned string once (filter + lowercase), then use two pointers starting at both ends of *that* cleaned string, moving inward and comparing characters. Correct for the same reverse-equality reason, just checked incrementally instead of building a second reversed string.
- Time complexity: O(n)  Space complexity: O(n) (still need the cleaned string)
- We've dropped the second reversed copy, but we're still allocating an entirely new string up front instead of working directly on the original.

### 3. Optimal
- Use two pointers directly on the original string, one starting at index 0 and one at the last index. At each step, skip past any non-alphanumeric characters on either side, then compare the two characters (case-insensitively). If they ever differ, it's not a palindrome; if the pointers cross or meet, it is.
- This works because we never need a separate cleaned copy — skipping invalid characters in-place as we move the pointers achieves the same filtering with zero extra allocation.
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: empty string or all-punctuation string (pointers cross immediately, trivially a palindrome), single character (trivially a palindrome), mixed case and digits (`"0P"` vs `"0p"` — case-fold letters but compare digits as-is).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
