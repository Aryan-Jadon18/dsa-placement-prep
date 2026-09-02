# 57. Insert Interval

**Difficulty:** Medium | **Pattern:** Intervals — Merge on Insert | **Tags:** Array, Intervals
**LeetCode:** https://leetcode.com/problems/insert-interval/

## Problem
You're given a list of intervals that is already sorted by start time, and no two of them overlap. Insert one new interval into this list, merging with any existing intervals it overlaps, and return the resulting list — still sorted, still non-overlapping.

**Input:** `intervals: List[List[int]]` (sorted, disjoint), `newInterval: List[int]`.
**Output:** the updated list of disjoint intervals, sorted by start.

**Example 1:**
`intervals = [[1,3],[6,9]]`, `newInterval = [2,5]` → `[[1,5],[6,9]]`
`[2,5]` overlaps `[1,3]` (they share 2-3), so they merge into `[1,5]`. It doesn't touch `[6,9]`, so that stays as-is.

**Example 2:**
`intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]` → `[[1,2],[3,10],[12,16]]`
`[4,8]` overlaps `[3,5]`, `[6,7]`, and `[8,10]` (touching counts as overlap here since `8` is shared), so all four merge into one `[3,10]`.

**Example 3:**
`intervals = []`, `newInterval = [5,7]` → `[[5,7]]`
Nothing to merge with — just insert it.

**Constraints:** `0 <= intervals.length <= 10^4`, intervals sorted and non-overlapping.

## Intuition (explained simply)
Since the input is already sorted, you don't need to re-sort everything from scratch. Walk left to right: intervals that end before the new one starts are untouched and go straight to the answer; intervals that start after the new one ends are also untouched and go straight to the answer; everything in between overlaps the new interval and gets merged into one big interval.

### 1. Brute Force
- Pretend we don't know the input is sorted: append `newInterval` to the list, sort everything by start, then run the standard "merge overlapping intervals" sweep (like LC 56) over the whole thing.
- Correct because it reduces the problem to a problem we already know how to solve, but it throws away the fact that the input was already sorted.
- Time complexity: O(n log n)  Space complexity: O(n)
- Why it's not good enough: re-sorting an already-sorted list is wasted work, and interviewers will ask "can you avoid the sort?"

### 2. Better
- Use `bisect.insort` to insert `newInterval` into the list at the correct sorted position in one step (this still costs O(n) to shift elements, but skips a full re-sort), then run one merge sweep over the whole array.
- Correct for the same reason as the merge sweep, just cheaper than sorting from scratch.
- Time complexity: O(n) (insort shift + one merge pass)  Space complexity: O(n)
- Still touches every interval even ones far away from the merge region, and mutates/copies more than necessary.

### 3. Optimal
- Single pass, three phases, no insertion into the middle of a list at all:
  1. Copy every interval that ends strictly before `newInterval` starts (no overlap, comes before).
  2. While the current interval overlaps `newInterval` (`start <= newInterval.end`), absorb it by expanding `newInterval`'s bounds (`min` of starts, `max` of ends). Then append the fully-merged interval.
  3. Copy every remaining interval (they all start after `newInterval` now ends).
- Why it works: because the input is sorted, once we see an interval that starts after the merged interval ends, no later interval can overlap it either — we're done merging.
- Time complexity: O(n)  Space complexity: O(n) (output list)
- Edge cases: empty `intervals`; `newInterval` overlapping everything (collapses to one interval); `newInterval` overlapping nothing (just gets inserted in the right slot); touching endpoints (`[1,2]` and `[2,3]`) count as overlapping and should merge.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n log n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(n) |
