# 128. Longest Consecutive Sequence

**Difficulty:** Medium | **Pattern:** Arrays & Hashing — Hashing | **Tags:** Array, Hash Table, Union Find
**LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence/

## Problem
Given an unsorted array of integers, find the length of the longest run of consecutive integers that can be formed using the values present in the array (the run doesn't need to appear contiguously in the array itself, just the values need to be consecutive integers).

**Input:** an integer array `nums`
**Output:** an integer — the length of the longest consecutive-values run

**Examples:**
1. `nums = [100,4,200,1,3,2]` → `4` — the values `1,2,3,4` form a consecutive run of length 4.
2. `nums = [0,3,7,2,5,8,4,6,0,1]` → `9` — `0` through `8` are all present.
3. `nums = [1,1,1,1]` → `1` — duplicates collapse to a single value, so the longest run is just `[1]`.

**Constraints:** `0 <= nums.length <= 10^5`, values can be negative, must run in O(n) time to be accepted as optimal (this rules out simply sorting for full credit, though sorting is a valid "better" solution).

## Intuition

### 1. Brute Force
- For each number in the array, repeatedly check if `number + 1`, `number + 2`, ... exist in the array (using a linear `in` search each time) and count how far the chain goes. Correct because it directly extends every possible starting point as far as it will go.
- Time complexity: O(n^3) (n starting points, each doing up to n steps, each step an O(n) linear search) — commonly described as O(n^2) if we're generous about the search cost being amortized, but a truly naive version is cubic.
- Wildly too slow — this is the "I haven't thought about data structures yet" approach.

### 2. Better
- Sort the array first, then walk through it once, tracking the current streak length and resetting it whenever the next value isn't exactly one more than the previous (skipping over duplicates). Correct because after sorting, consecutive values are adjacent, so a single linear scan finds every run.
- Time complexity: O(n log n) (dominated by the sort)  Space complexity: O(1) extra if sorting in place, O(n) if we can't mutate input
- Fast and simple, but the sort is unnecessary work — a hash set can find the same answer in true linear time.

### 3. Optimal
- Put every number into a hash set. Then, for each number, only start counting a new sequence if `number - 1` is **not** in the set (meaning this number is the start of a run). From each such start, keep checking `number + 1`, `number + 2`, ... in the set and count the length.
- This works because the "only start if no predecessor" check guarantees each consecutive run is expanded from its start exactly once — every number is visited a constant number of times in total across the whole algorithm, giving true O(n) amortized time.
- Time complexity: O(n)  Space complexity: O(n)
- Edge cases: empty array (return 0), all duplicates (longest run is length 1), negative numbers (hashing handles them the same as positive), array already fully consecutive (whole array is one run).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) – O(n^3) | O(1) |
| Better | O(n log n) | O(1) / O(n) |
| Optimal | O(n) | O(n) |
