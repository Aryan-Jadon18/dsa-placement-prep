# 152. Maximum Product Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-Running%20Max%2FMin%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20Array-lightgrey)
**LeetCode:** https://leetcode.com/problems/maximum-product-subarray/

## Problem
Given an integer array `nums`, find the contiguous subarray (containing at least one number) that has the largest product, and return that product.

**Input:** an integer array `nums`
**Output:** an integer — the maximum product of any contiguous subarray

**Examples:**
1. `nums = [2, 3, -2, 4]` → `6`. Best subarray is `[2, 3]` → `6`.
2. `nums = [-2, 0, -1]` → `0`. Any subarray touching both negatives crosses the 0, so the best achievable is the single element `0`.
3. `nums = [-2, 3, -4]` → `24`. The whole array: `-2 * 3 * -4 = 24` — two negatives cancel out to a positive.

**Constraints:** `1 <= nums.length <= 2*10^4`, `-10 <= nums[i] <= 10`.

> 🔑 **Pattern Recognition**
> A sign flip from a negative number can turn the *worst* running product into the *best* one, so the state at each index can't just be "best product ending here" — it must also track "worst product ending here." Needing to carry two interacting running extremes instead of one is the tell for this variant of 1D DP.

## Intuition (explained simply)
This looks like Kadane's algorithm (max subarray *sum*), but multiplication has a twist: a negative number flips the sign of everything multiplied with it. So a subarray that currently has the *most negative* product could become the *best* product if you multiply it by one more negative number. That means at each position we must track both the best (max) and worst (min) running products, because the worst one might become the best on the next step.

### 1. Brute Force
- Try every contiguous subarray `nums[i:j]`, compute its product directly, and track the maximum seen.
- Correct because it's an exhaustive check over all O(n^2) subarrays.
- Time complexity: O(n^2) (or O(n^3) if the product is recomputed from scratch each time instead of extended incrementally) — here we extend the product as `j` grows so it's O(n^2)  Space complexity: O(1) extra
- Quadratic — too slow for `n = 2*10^4`, and it doesn't build any reusable structure.

### 2. Better
- **DP idea (top-down):** define `maxEnd(i)` = the maximum product of a subarray ending exactly at index `i`, and `minEnd(i)` = the minimum (most negative) product ending at `i`. Recursively, `maxEnd(i) = max(nums[i], nums[i] * maxEnd(i-1), nums[i] * minEnd(i-1))` (try starting fresh at `i`, extending the previous max, or extending the previous min in case `nums[i]` is negative and flips it). `minEnd(i)` is defined symmetrically with `min(...)`.
- Memoize both `maxEnd` and `minEnd` so each index's max/min-ending-here values are computed once, then take the running max over all `maxEnd(i)`.
- Time complexity: O(n)  Space complexity: O(n) for the two memo arrays + O(n) recursion stack
- We only ever need the *previous* index's max/min, not the whole history — the memo arrays are unnecessary.

### 3. Optimal
- **DP state:** `curMax` = the maximum product of a subarray ending at the current index; `curMin` = the minimum product of a subarray ending at the current index. (Equivalent to `dp[i]` = best/worst product ending at `i`, kept as rolling variables instead of arrays.)
- **Transition:** at each new number `n`, compute the three candidates `n`, `n * curMax`, `n * curMin` — the new `curMax` is the largest of the three, the new `curMin` is the smallest of the three (both must be recomputed from the *old* curMax/curMin before either is overwritten, since a negative `n` swaps which one becomes useful).
- Track a global `result = max(result, curMax)` after updating at each step.
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: array contains a `0` → both `curMax` and `curMin` should reset to consider starting fresh after the zero (handled naturally since `max(n, n*curMax, n*curMin)` with `n=0` allows resetting); single-element array → answer is that element; all negative numbers with even count → whole array product is best; odd count of negatives → must exclude exactly one (leftmost or rightmost run), which the running max/min approach handles automatically.

#### 🎯 Visual Walkthrough
Worked example: `nums = [2, 3, -2, 4]` → `6`.

| i | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| nums[i] | 2 | 3 | -2 | 4 |
| curMax | 2 | 6 | -2 | 4 |
| curMin | 2 | 3 | -12 | -48 |

At `i=2`, `nums[i]=-2` is negative: the three candidates are `{-2, -2*6, -2*3} = {-2, -12, -6}`, so `curMax = max(...) = -2` and `curMin = min(...) = -12` (the old `curMax=6` becomes the new worst case once multiplied by a negative). The running answer is `max(curMax over all i) = max(2, 6, -2, 4) = 6`, matching subarray `[2, 3]`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(1) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
