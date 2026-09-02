# 242. Valid Anagram

**Difficulty:** Easy | **Pattern:** Arrays & Hashing — Hashing/Counting | **Tags:** String, Hash Table, Sorting
**LeetCode:** https://leetcode.com/problems/valid-anagram/

## Problem
Given two strings, decide whether the second is an anagram of the first — meaning it uses exactly the same letters, the same number of times each, just possibly rearranged.

**Input:** two strings `s` and `t`
**Output:** a boolean — `true` if `t` is an anagram of `s`, `false` otherwise

**Examples:**
1. `s = "anagram"`, `t = "nagaram"` → `true` — same letters, same counts, different order.
2. `s = "rat"`, `t = "car"` → `false` — different letter sets.
3. `s = "aacc"`, `t = "ccac"` → `false` — same letters present but counts differ (`t` has three c's, `s` has two).

**Constraints:** `1 <= s.length, t.length <= 5 * 10^4`, lowercase English letters (general solution should still handle full Unicode gracefully).

## Intuition

### 1. Brute Force
- For each character in `s`, search for and remove one matching occurrence from a mutable copy of `t`. If we successfully remove one for every character in `s` and nothing is left over, they're anagrams. Correct because it directly verifies a one-to-one letter matching.
- Time complexity: O(n^2)  Space complexity: O(n) (for the mutable copy)
- The repeated linear "search and remove" inside a loop is wasteful — a beginner's first instinct but not interview-ready.

### 2. Better
- Sort both strings and compare the sorted results directly — two strings are anagrams exactly when their sorted forms are identical.
- Correct because sorting is a canonical form: any rearrangement of the same multiset of characters sorts to the same sequence.
- Time complexity: O(n log n)  Space complexity: O(n) (sorted copies)
- Simple and clean, but we're paying a log factor for something a linear counting pass can do without any comparisons.

### 3. Optimal
- First check lengths match (anagrams must be the same length). Then count character frequencies in `s` using a hash map (or fixed-size array for lowercase letters), and decrement counts while scanning `t`. If any count goes negative or a character is missing, they aren't anagrams; if all counts return to zero, they are.
- This works because tallying frequencies is a direct, single-pass way to compare multisets without sorting overhead.
- Time complexity: O(n)  Space complexity: O(1) for a fixed 26-letter alphabet, O(k) in general for k distinct characters
- Edge cases: different lengths (short-circuit immediately), empty strings (equal length, trivially match), non-lowercase/Unicode input (use a `Counter`/dict instead of a fixed 26-array).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(n) |
| Better | O(n log n) | O(n) |
| Optimal | O(n) | O(1) / O(k) |
