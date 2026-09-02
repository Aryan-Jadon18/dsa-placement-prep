# 53. Maximum Subarray

**Difficulty:** Medium | **Pattern:** Kadane's Algorithm | **Tags:** Array, DP, Greedy
**LeetCode:** https://leetcode.com/problems/maximum-subarray/

## Problem
Given an integer array, find the contiguous subarray (containing at least one number) with the largest sum, and return that sum.

Input: `nums`, a list of integers (can include negatives).
Output: an integer, the maximum subarray sum.

**Example 1:** `nums = [-2,1,-3,4,-1,2,1,-5,4]` → `6`. The subarray `[4,-1,2,1]` sums to 6, the best possible.

**Example 2:** `nums = [1]` → `1`. Only one element, so it's the answer by itself.

**Example 3:** `nums = [-3,-1,-2]` → `-1`. All negative — the best "subarray" is just the single largest element, since you must pick at least one number.

Constraints: `1 <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`.

## Intuition (explained simply)
As we scan left to right, we track "the best sum of a subarray that *ends right here*." If that running sum ever drops below zero, it's dragging down anything we'd add next — so it's better to start a fresh subarray from the current element than to keep carrying a negative prefix along. This "should I extend or restart" decision at each step, chosen locally without needing to look ahead, is the greedy core of Kadane's algorithm (and it's also a 1D DP in disguise, which is why this problem sits at the boundary of both patterns).

### 1. Brute Force
- Try every pair of start and end indices, sum each subarray directly, and track the maximum.
- Correct because it's a literal exhaustive check of every possible contiguous subarray.
- Time complexity: O(n^2) with a running sum per start index (O(n^3) if resumming from scratch each time). Space complexity: O(1).
- Quadratic — too slow for `n` up to 100,000 (10 billion operations).

### 2. Better
- Define `best_ending_here[i]` = the max sum of a subarray ending exactly at index `i`. Recurrence: `best_ending_here[i] = nums[i] + max(0, best_ending_here[i-1])` — either extend the best subarray ending at `i-1` (if that's a net positive contribution) or start fresh at `i`. The answer is `max` over all `i` of `best_ending_here[i]`. This is a genuine 1D DP formulation.
- Correct because the max subarray ending at `i` can only be built by either standing alone or appending to the best subarray ending at `i-1` — nothing else is possible for a *contiguous* subarray ending at `i`.
- Time complexity: O(n) — one pass, O(1) work per index. Space complexity: O(n) if the whole `best_ending_here` array is stored explicitly.
- Storing the entire array is unnecessary — each entry only ever depends on the immediately previous one.

### 3. Optimal
- Collapse the DP array to a single rolling variable `current_sum`, exactly Kadane's algorithm: `current_sum = nums[i] + max(0, current_sum)` (equivalently: `if current_sum < 0: current_sum = nums[i] else: current_sum += nums[i]`), and track `best = max(best, current_sum)` as we go.
- **Why the greedy "reset when negative" choice is safe:** if the running sum ever goes negative, no future subarray sum can be improved by including that negative prefix — dropping it and starting over at the current element strictly dominates (or ties) keeping it, for every possible extension length. There's no scenario where carrying a negative prefix forward ever helps, so discarding it the moment it turns negative loses nothing and can only help.
- Time complexity: O(n) — single pass. Space complexity: O(1) — two scalars.
- Edge cases: all-negative array → the answer is the single largest (least negative) element, not 0 — initialize `best` to `nums[0]` (not 0) so an all-negative array still returns a real element rather than incorrectly reporting an "empty subarray" sum of 0; single-element array → that element itself.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(1) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
