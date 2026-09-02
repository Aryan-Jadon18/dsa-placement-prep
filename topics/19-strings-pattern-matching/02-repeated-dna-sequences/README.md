# 187. Repeated DNA Sequences

**Difficulty:** Medium | **Pattern:** Rolling Hash / Sliding Window | **Tags:** String, Hash Table, Bit Manipulation, Sliding Window
**LeetCode:** https://leetcode.com/problems/repeated-dna-sequences/

## Problem
DNA sequences are made only of the letters `A`, `C`, `G`, `T`. Given a DNA string, find all 10-letter-long substrings that occur **more than once** in the string. Return them without duplicates, in any order.

**Input:** `s: str` (only characters `A`, `C`, `G`, `T`).
**Output:** `List[str]` — the repeated 10-letter substrings, each listed once.

**Example 1:**
`s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"` → `["AAAAACCCCC","CCCCCAAAAA"]`
`"AAAAACCCCC"` appears at index 0 and index 10; `"CCCCCAAAAA"` appears at index 5 and index 15.

**Example 2:**
`s = "AAAAAAAAAAAAA"` → `["AAAAAAAAAA"]`
Every 10-letter window here is the same string `"AAAAAAAAAA"`, and it appears many times (indices 0-3), but we only report it once.

**Example 3:**
`s = "AAAAAAAAAAA"` (11 chars) → `["AAAAAAAAAA"]`
Windows at index 0 and index 1 are both `"AAAAAAAAAA"` — one repeat, one reported string.

**Constraints:** `1 <= s.length <= 10^5`, characters are only `A/C/G/T`.

## Intuition (explained simply)
We need to slide a window of length 10 across the string and remember every window we've seen, flagging any that repeat. The naive part is that comparing/storing full 10-character strings over and over is wasteful — we can instead compress each window into a small number (a hash) so comparisons become O(1) integer/string-hash comparisons instead of O(10) character comparisons, and update that number incrementally as the window slides.

### 1. Brute Force
- Extract every 10-character substring using slicing (`s[i:i+10]` for each valid `i`), and count how many times each exact substring appears using a hash map keyed by the substring itself. At the end, collect every key with count `>= 2`.
- Correct because it directly counts occurrences of every window.
- Time complexity: O(n · L) where `L = 10` (each slice/hash costs O(L))  Space complexity: O(n · L) for storing all the substrings
- Why it's not great: for very large `n` (up to 10⁵), building and hashing 10-character string slices repeatedly adds unnecessary constant-factor overhead — we can avoid re-scanning all 10 characters at every shift.

### 2. Better
- Encode each of the 4 DNA letters as a 2-bit code (`A=00, C=01, G=10, T=11`). Represent each 10-letter window as a 20-bit integer built once, then update it incrementally as the window slides: drop the oldest 2 bits (shift and mask) and append the new letter's 2 bits. Use this integer as the hash-map key instead of a raw string, giving O(1) window updates and O(1) average-case hash map operations, avoiding recomputing the whole window's hash from scratch every time.
- This removes the O(L) per-step string slicing/hashing of the brute-force approach.
- Time complexity: O(n) (amortized O(1) per position after the first window)  Space complexity: O(n) (storing up to n integer keys and n/L-ish repeated-substring strings for output)
- Nearly optimal already — mentioned as "better" mainly because a plain Python string-hashing approach (using `s[i:i+10]` directly as a dict key, letting Python's built-in string hashing do the work) achieves the same asymptotic complexity with less manual bit-twiddling, which is what "optimal" below does instead, trading manual bit tricks for simplicity while keeping the same guarantees.
- Edge cases handled the same way as brute force.

### 3. Optimal
- Slide a window of length 10 across the string using plain string slicing, but track occurrence counts with a **hash map from substring → count**, and only add a substring to the answer set the **first time its count reaches exactly 2** (not on later occurrences), avoiding both duplicate entries in the answer and any extra "seen" set. Rely on Python's already-efficient built-in string hashing (O(L) to hash a length-L string, but L=10 is a small constant) rather than manual bit-packing, keeping the code simple and just as fast in practice for this constant window size.
- Why it works: a hash map naturally deduplicates identical windows into the same bucket; checking `count == 2` (not `>= 2`) at the moment of insertion guarantees we add each repeated substring to the result exactly once, no matter how many times it recurs afterward.
- Time complexity: O(n) (n - 9 windows, O(L)=O(10)=O(1) work each since L is a fixed constant)  Space complexity: O(n) (hash map entries + result list)
- Edge cases: string shorter than 10 characters → return `[]` immediately; overlapping repeats (e.g. `"AAAAAAAAAAA"`); a substring appearing 3+ times still only reported once.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n·L) | O(n·L) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(n) |
