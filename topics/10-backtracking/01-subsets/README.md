# 78. Subsets

**Difficulty:** Medium | **Pattern:** Backtracking | **Tags:** Array, Backtracking
**LeetCode:** https://leetcode.com/problems/subsets/

## Problem
Given an array of unique integers, return every possible subset (the power set) —
including the empty subset and the full array itself. The subsets can be returned in
any order.

**Input:** array of unique integers
**Output:** a list of all subsets (each a list of integers)

**Examples**
1. Input: `[1,2,3]` → Output: `[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]` (order may
   vary) — all `2^3 = 8` subsets.
2. Input: `[0]` → Output: `[[],[0]]` — the empty set and the set containing `0`.
3. Input: `[1,2]` → Output: `[[],[1],[2],[1,2]]` — all `2^2 = 4` subsets.

**Constraints:** `1 <= nums.length <= 10`, all values unique, `-10 <= nums[i] <= 10`.

## Intuition (explained simply)
For every element, you make a binary choice: include it in the current subset, or
don't. Making that choice independently for each of the n elements produces every
possible combination — exactly `2^n` outcomes. Backtracking is the natural tool: try
"include", explore everything downstream, undo, then try "exclude" and explore that
branch too.

### 1. Brute Force
- Use bitmasking: for each integer `mask` from `0` to `2^n - 1`, treat the binary
  representation of `mask` as an "include/exclude" decision for each index — if bit
  `i` is set, include `nums[i]` in this subset. Collect one subset per mask value.
- Time complexity: O(n * 2^n) — 2^n masks, O(n) work to build each subset by
  checking every bit  Space complexity: O(n * 2^n) to store all subsets (unavoidable
  for this problem, since that's literally the output size)
- Why it's not good enough: it works and has the same asymptotic output size as any
  correct solution, but it's an unintuitive way to express "choose or don't choose"
  and doesn't generalize well to variants with duplicates or extra constraints
  (unlike backtracking, which extends naturally).

### 2. Better
- Iterative "build up" approach: start with `result = [[]]`. For each number in
  `nums`, take every subset currently in `result` and create a new copy of it with
  the current number appended, adding all those new copies into `result`. After
  processing all numbers, `result` holds every subset.
- Time complexity: O(n * 2^n) — same total output size, and each doubling step
  copies all existing subsets  Space complexity: O(n * 2^n)
- What's still suboptimal: conceptually simple, but it's less flexible for
  interview-style follow-ups (like generating subsets of a specific size, or subsets
  with duplicates), and it builds many intermediate list copies rather than
  incrementally constructing and backtracking on one shared path.

### 3. Optimal
- Classic backtracking / DFS: maintain one mutable `path` list. At index `i`, first
  record the current `path` as a valid subset (every prefix state along the DFS *is*
  a subset), then loop over all indices `j >= i`, append `nums[j]` to `path`, recurse
  with `i = j + 1`, then pop `nums[j]` off `path` (undo) before trying the next `j`.
- This works because it directly enumerates the recursion tree of "which elements do
  we include from here on," and popping after each recursive call ensures the shared
  `path` list is correctly restored to explore sibling branches.
- Time complexity: O(n * 2^n) — same output size, but avoids duplicating list copies
  by mutating and undoing a single shared path (much better constant factor)  Space
  complexity: O(n) for the recursion depth / path, plus O(n * 2^n) for the output
- Edge cases: empty input isn't possible per constraints, but a single-element array
  correctly yields `[[], [nums[0]]]`; the very first recorded subset is always the
  empty list.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n * 2^n) | O(n * 2^n) |
| Better | O(n * 2^n) | O(n * 2^n) |
| Optimal | O(n * 2^n) | O(n) + output |
