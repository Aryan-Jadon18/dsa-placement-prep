# 1392. Longest Happy Prefix

**Difficulty:** Hard | **Pattern:** KMP Failure Function | **Tags:** String, String Matching
**LeetCode:** https://leetcode.com/problems/longest-happy-prefix/

## Problem
A "happy prefix" of a string is a non-empty prefix that is **also** a suffix of the same string, and it must not be the entire string itself. Given a string, return its longest happy prefix, or an empty string if none exists.

**Input:** `s: str`.
**Output:** `str` — the longest proper prefix that's also a suffix, or `""`.

**Example 1:**
`s = "level"` → `"l"`
The prefix `"l"` equals the suffix `"l"`. Longer candidates (`"le"` vs `"el"`, `"lev"` vs `"vel"`, etc.) don't match, so `"l"` is the longest happy prefix.

**Example 2:**
`s = "ababab"` → `"abab"`
Prefix `"abab"` (first 4 chars) equals suffix `"abab"` (last 4 chars). It can't be the full string (`"ababab"` itself doesn't count), and `"abab"` is longer than the next candidate `"ab"`.

**Example 3:**
`s = "leetcodeleet"` → `"leet"`
Prefix `"leet"` (first 4 chars) matches the suffix `"leet"` (last 4 chars, positions 8-11).

**Constraints:** `1 <= s.length <= 10^5`, lowercase English letters.

## Intuition (explained simply)
This problem is *literally* asking for the value that KMP's failure function computes for the very last position of the string — the failure function at index `i` already tells you "the length of the longest proper prefix of `s[0..i]` that's also a suffix of `s[0..i]`." So the answer to this whole problem is just: build the standard KMP failure/LPS array for `s`, and read off its last entry.

### 1. Brute Force
- For every possible prefix length `L` from `len(s) - 1` down to `1` (must be a proper prefix, so at most `len(s)-1`), check if `s[0:L] == s[len(s)-L:]` (directly comparing the prefix substring to the equal-length suffix substring). Return the first (longest) length that matches; if none match, return `""`.
- Correct because it directly checks the definition of "happy prefix" for every candidate length, starting from the longest.
- Time complexity: O(n²) (up to n candidate lengths, each comparison costs up to O(n))  Space complexity: O(n) (for the substring slices being compared)
- Why it's not good enough: for `n` up to 10⁵, O(n²) is around 10¹⁰ operations — much too slow.

### 2. Better
- Instead of comparing full substrings character-range by character-range, use **string hashing**: precompute a rolling hash for every prefix and every suffix of `s` (polynomial hashing with a fixed base/modulus lets you compute the hash of any prefix or suffix in O(1) after O(n) preprocessing). For each candidate length `L` from `n-1` down to `1`, compare the prefix-hash and suffix-hash in O(1); only if the hashes match, do you optionally verify with a direct character comparison (to guard against hash collisions).
- This turns each candidate check into O(1) (or O(1) amortized with rare full verifications), a big speedup over the O(n) brute-force comparison per candidate.
- Time complexity: O(n) (average case; a pathological hash collision could force an O(n) verification, but this is rare with a good modulus)  Space complexity: O(n) (prefix/suffix hash arrays)
- Depends on the hash function being well-chosen to avoid collisions — not as airtight a guarantee as a purpose-built combinatorial algorithm.

### 3. Optimal
- Build the **KMP failure function (LPS array)** for `s` directly: `lps[i]` = the length of the longest proper prefix of `s[0..i]` that's also a suffix of `s[0..i]`. This is built with the standard two-pointer technique: maintain a `length` counter (current matched prefix-length) and, for each new character, either extend the match (`s[i] == s[length]` → `length += 1`) or fall back using the failure function itself (`length = lps[length-1]`) until it either matches or hits 0. The final answer is simply `s[:lps[-1]]` (the prefix of that length) — or `""` if `lps[-1] == 0`.
- Why it works: the LPS array is *defined* to be exactly the answer to this question, computed incrementally for every prefix of the string in one linear pass — no separate hashing or comparison step needed at all; it's baked into the DP-like recurrence of the KMP preprocessing itself.
- Time complexity: O(n) worst case, no reliance on hash luck.  Space complexity: O(n) for the LPS array.
- Edge cases: single character string → no proper prefix/suffix possible, return `""`; all-identical characters (e.g. `"aaaa"` → `"aaa"`, longest proper prefix/suffix); string with no repeating structure at all (e.g. `"abcde"` → `""`).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n²) | O(n) |
| Better | O(n) average | O(n) |
| Optimal | O(n) | O(n) |
