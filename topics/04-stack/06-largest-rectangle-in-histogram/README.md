# 84. Largest Rectangle in Histogram

**Difficulty:** Hard | **Pattern:** Monotonic Stack | **Tags:** Array, Stack, Monotonic Stack
**LeetCode:** https://leetcode.com/problems/largest-rectangle-in-histogram/

## Problem
Given an array of bar heights forming a histogram (each bar has width 1, standing side by side), find the area of the largest rectangle that can be formed using contiguous bars, where the rectangle's height is limited by the shortest bar it spans.

- **Input:** an integer array `heights`, where `heights[i]` is the height of the `i`-th bar.
- **Output:** an integer — the maximum rectangular area achievable.

**Examples**
1. `heights = [2,1,5,6,2,3]` → `10`. The rectangle spans bars at indices 2-3 (heights 5 and 6), using height 5 and width 2 → area 10.
2. `heights = [2,4]` → `4`. Either a single bar of height 4 (width 1, area 4) or both bars limited to height 2 (width 2, area 4) — both give 4.
3. `heights = [6,7,5,2,4,5,9,3]` → `16`. The bar at index 3 (height 2) is short enough that every other bar in the array is at least as tall, so a rectangle of height 2 can stretch across all 8 bars: `2 * 8 = 16` — the widest possible rectangle, even though its height is modest.

**Constraints:** `1 <= heights.length <= 10^5`, `0 <= heights[i] <= 10^4`.

## Intuition (explained simply)

### 1. Brute Force
- For every pair of left and right boundaries (every contiguous subarray), find the minimum height in that range and multiply by the width, tracking the best area.
- Correct because it's the direct definition — every possible rectangle spanning contiguous bars is considered.
- Time complexity: O(n²) if the minimum is tracked incrementally while expanding the right boundary (O(n³) if recomputed from scratch every time).  Space complexity: O(1) extra.
- With `n` up to 100,000, O(n²) (10^10 operations) is far too slow for an interview-quality solution.

### 2. Better
- For each bar `i`, expand left and right from `i` independently (two separate scans) to find how far a rectangle of height `heights[i]` could extend before hitting a shorter bar — this gives, for each bar, "how wide could a rectangle at this exact height be." Track the best `height * width` over all bars.
- Correct because the maximum rectangle must have some height equal to one of the bars (the shortest bar within its span), so checking every bar as "the limiting height" and finding its maximal width covers all candidates.
- Time complexity: O(n²) worst case (e.g., strictly increasing heights make the left/right expansion for the last bar scan the whole array) — same asymptotic complexity as brute force, but with a much smaller constant and it's a genuinely different technique (a stepping stone toward the stack idea, since we're now computing "nearest shorter bar" style boundaries, just inefficiently).  Space complexity: O(1) extra.
- Independently expanding left/right per bar redoes a lot of comparison work — a monotonic stack lets us compute "nearest smaller bar to the left/right" for *all* bars in one linear pass instead.

### 3. Optimal
- Use a monotonic increasing stack of indices. Walk through the bars (plus one sentinel bar of height 0 appended at the end to flush the stack): while the current bar is shorter than the bar at the top of the stack, pop the top — that popped bar's rectangle can't extend any further right, so compute its area using its height, with its width spanning from *just after the new stack top* (its nearest smaller bar to the left) to the current index (its nearest smaller bar to the right, exclusive).
- This works because the stack always holds bars in increasing height order with "still-open" rectangles; the moment a shorter bar appears, every taller bar that can't extend further gets finalized with its exact left/right boundary determined by its stack neighbors — each bar is pushed and popped exactly once.
- Time complexity: O(n) — each index is pushed once and popped once.  Space complexity: O(n) for the stack.
- Edge cases: all bars the same height (one giant rectangle, width n); strictly increasing or strictly decreasing heights (stress-tests the stack push/pop pattern); a height-0 bar acts as a natural barrier splitting the histogram.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(1) |
| Better | O(n^2) worst case, smaller constant | O(1) |
| Optimal | O(n) | O(n) |
