# 217. Contains Duplicate

**Difficulty:** Easy | **Pattern:** Arrays & Hashing — Hashing | **Tags:** Array, Hash Table
**LeetCode:** https://leetcode.com/problems/contains-duplicate/

## Problem
Given an array of integers, determine whether any value appears at least twice.

**Input:** an integer array `nums`
**Output:** a boolean — `true` if any value repeats, `false` if every value is unique

**Examples:**
1. `nums = [1, 2, 3, 1]` → `true` (1 appears twice).
2. `nums = [1, 2, 3, 4]` → `false` (all unique).
3. `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]` → `true` (lots of repeats, only need to find one).

**Constraints:** `1 <= nums.length <= 10^5`, values can be negative, no ordering guaranteed.

## Intuition

### 1. Brute Force
- Compare every pair of elements; if any two match, we have a duplicate. Correct because it literally checks every pair.
- Time complexity: O(n^2)  Space complexity: O(1)
- Way too slow for `n = 10^5` — quadratic blows up instantly.

### 2. Better
- Sort the array first. Duplicates, if any, end up adjacent to each other, so a single linear scan comparing each element to its neighbor finds them.
- Correct because sorting groups equal values together; no duplicate can "hide" once sorted.
- Time complexity: O(n log n)  Space complexity: O(1) extra (ignoring sort's internal usage) or O(n) if we don't want to mutate the input and make a copy first.
- Better than brute force, but we're paying a sorting cost when we don't actually need order — just membership.

### 3. Optimal
- Walk through the array once, adding each number to a hash set. Before adding, check if it's already in the set — if so, we found a duplicate immediately.
- Works because a hash set gives O(1) average membership checks, so we detect the repeat the moment we see it the second time — no need to sort at all.
- Time complexity: O(n)  Space complexity: O(n)
- Edge cases: single-element array (never a duplicate, return false), all elements identical (returns true right after the second element), empty input isn't allowed per constraints but the loop handles it gracefully anyway.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(1) |
| Better | O(n log n) | O(1) |
| Optimal | O(n) | O(n) |
