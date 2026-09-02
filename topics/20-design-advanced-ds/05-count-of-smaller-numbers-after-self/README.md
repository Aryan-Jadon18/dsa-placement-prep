# 315. Count of Smaller Numbers After Self

**Difficulty:** Hard | **Pattern:** BIT / Merge Sort — Inversion Counting | **Tags:** Binary Indexed Tree, Segment Tree, Merge Sort, Divide and Conquer
**LeetCode:** https://leetcode.com/problems/count-of-smaller-numbers-after-self/

## Problem
Given an integer array, for every element return how many elements **to its right** are strictly smaller than it.

**Input:** `nums: List[int]`.
**Output:** `List[int]` `counts` where `counts[i]` = number of `j > i` with `nums[j] < nums[i]`.

**Example 1:**
`nums = [5,2,6,1]` → `[2,1,1,0]`
For `5` (index 0): `2` and `1` (to its right) are smaller → count 2. For `2` (index 1): only `1` is smaller → count 1. For `6` (index 2): only `1` is smaller → count 1. For `1` (index 3): nothing to its right → count 0.

**Example 2:**
`nums = [-1]` → `[0]`
No elements to the right at all.

**Example 3:**
`nums = [-1,-1]` → `[0,0]`
They're equal, not strictly smaller, so neither counts toward the other.

**Constraints:** `1 <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`.

## Intuition (explained simply)
This is the classic **"counting inversions"** problem in disguise (an inversion is a pair `(i, j)` with `i < j` but `nums[i] > nums[j]`), just asking for the per-element breakdown instead of one grand total. Two classical techniques solve counting inversions in O(n log n): merge sort (count cross-inversions during the merge step) and a Fenwick Tree processed right-to-left (count how many smaller values have already been "seen").

### 1. Brute Force
- For every index `i`, scan every index `j > i` and count how many satisfy `nums[j] < nums[i]`.
- Correct — it's the literal definition, checked exhaustively for every pair.
- Time complexity: O(n²)  Space complexity: O(1) extra (besides output)
- Why it's not good enough: with n up to 10⁵, O(n²) is ~10¹⁰ operations — much too slow.

### 2. Better — Merge Sort (counting cross-inversions)
- Pair every value with its original index, then merge-sort those pairs by value. During the **merge step** of merge sort, whenever an element from the right half is placed into the merged result *before* an element from the left half (meaning it's smaller and originally came after), that means **every remaining element in the left half** is bigger than it — add to those specific left-half elements' counts (using their original indices) the number of right-half elements already merged in before them (or symmetrically, tally how many right-half elements have been placed so far whenever a left-half element gets placed).
- Why it works: merge sort already visits every pair of elements exactly once across all its merge steps (that's the definition of a comparison-based sort), and the merge step is precisely where you can detect "how many later, smaller elements" cross past each element, in bulk, using the fact both halves are already internally sorted.
- Time complexity: O(n log n) (standard merge sort recurrence)  Space complexity: O(n) (auxiliary arrays for merging + tracking original indices)
- Correct and efficient — included as "better" mainly to contrast with the Fenwick Tree technique below, which is simpler to reason about once you understand the data structure and generalizes more easily to online/streaming variants.

### 3. Optimal — Fenwick Tree (Binary Indexed Tree) with Coordinate Compression
- **Why a Fenwick Tree here?** We need to process `nums` from right to left, and for each value, ask "how many values I've already seen (to my right) are smaller than me?" — then record that value as "seen." A Fenwick Tree (see the deep-dive intuition in the "Range Sum Query - Mutable" writeup if you haven't used one before) supports exactly two operations in O(log n): incrementing a counter at some position (`add 1 at value v` — marking "we've seen value v"), and querying a prefix count (`how many seen values are <= v` — a running total up to a point). Since values can be negative and can range up to ±10⁴, we first **coordinate-compress**: sort the distinct values and map each to a small rank `0..k-1`, so the Fenwick Tree's positions correspond to those ranks instead of the raw (possibly negative) values.
- Algorithm: build the compressed rank mapping. Walk `nums` from **right to left**. For each `nums[i]`, look up its rank `r`; query the Fenwick Tree for the prefix count of ranks `0..r-1` (this tells you how many already-seen values are strictly smaller — exactly what we want); record that as `counts[i]`; then add 1 at rank `r` in the tree (mark this value as seen for future, i.e. earlier, elements to query against).
- Why it works: processing right-to-left means "already seen" always means "somewhere to the right of the current index" — exactly matching the problem's definition. The Fenwick Tree turns "how many smaller values have I seen so far" into an O(log n) prefix-count query instead of a linear scan.
- Time complexity: O(n log n) (n elements, O(log n) per Fenwick Tree update/query, plus O(n log n) for the initial sort during coordinate compression)  Space complexity: O(n) (the Fenwick Tree array + rank mapping)
- Edge cases: all elements equal (every count is 0, since "smaller" is strict); already sorted ascending (every count is 0); already sorted descending (`counts[i] = n-1-i`); duplicate values (coordinate compression must map duplicates to the same rank, and the Fenwick prefix query up to `r-1` — not `r` — correctly excludes equal values).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n²) | O(1) |
| Better (Merge Sort) | O(n log n) | O(n) |
| Optimal (Fenwick Tree) | O(n log n) | O(n) |
