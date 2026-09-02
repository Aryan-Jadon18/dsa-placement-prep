# 213. House Robber II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-1D%20DP%20(circular)-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20Array-lightgrey)
**LeetCode:** https://leetcode.com/problems/house-robber-ii/

## Problem
Same as House Robber, but the houses are arranged in a circle — house `0` and house `n-1` are now adjacent too. You still can't rob two adjacent houses. Find the maximum money obtainable.

**Input:** an integer array `nums` (money per house, arranged in a circle)
**Output:** an integer — the maximum sum obtainable with no two adjacent (circularly) chosen

**Examples:**
1. `nums = [2, 3, 2]` → `3`. Robbing house 0 and house 2 is illegal here since they're circularly adjacent, so best is just house 1 (`3`).
2. `nums = [1, 2, 3, 1]` → `4`. House 0 and house 3 are circularly adjacent, so we can't take both, but house 0 and house 2 are *not* adjacent (they're two apart) — robbing them gives `nums[0] + nums[2] = 1 + 3 = 4`, which beats any other combination.
3. `nums = [1, 2, 3]` → `3`. Best is just house 2 (or house 1), since any two houses in a 3-circle are adjacent.

**Constraints:** `1 <= nums.length <= 100`, `0 <= nums[i] <= 1000`.

> 🔑 **Pattern Recognition**
> A circular adjacency constraint that only ever couples the first and last elements can be broken by running the linear DP twice, once with each end excluded — recognizing "the hard wraparound case reduces to two easy linear DP cases" is the key interview cue here.

## Intuition (explained simply)
The circle only creates one extra constraint: house `0` and house `n-1` can't both be robbed. So either house `0` is excluded, or house `n-1` is excluded (or both) — we never need to consider a plan that robs both. That means: solve plain (linear) House Robber twice — once on the array excluding the last house, once excluding the first house — and take the max of the two results. Both of those sub-runs are safe because within each, the "circular" pair is broken.

### 1. Brute Force
- Plain recursion on the *linear* subarray `nums[0..n-2]` and separately on `nums[1..n-1]`, each solved by the same exhaustive rob/skip recursion as House Robber I, then take the max of the two.
- Correct because any valid circular selection either avoids house `n-1` (covered by the first subarray) or avoids house `0` (covered by the second) — these two cases together cover every valid plan, and neither subarray has a wraparound adjacency.
- Time complexity: O(2^n) (two exponential recursions)  Space complexity: O(n) (recursion stack)
- Same overlapping-subproblem blowup as linear House Robber, just run twice.

### 2. Better
- Memoize each of the two linear recursions (top-down DP), same idea as House Robber I applied twice.
- Correct for the same reason as above; now each linear run is O(n).
- Time complexity: O(n)  Space complexity: O(n) cache (each run) + O(n) recursion stack
- Recursion overhead persists; can be replaced with a simple iterative pass.

### 3. Optimal
- **DP state:** for a linear array segment, `dp[i]` = the maximum money obtainable considering positions `0..i` of that segment (identical definition to House Robber I).
- **Transition:** `dp[i] = max(dp[i-1], dp[i-2] + val[i])`, same as House Robber I, run independently on `nums[0 : n-1]` and `nums[1 : n]`.
- Take `max(linearRob(nums[0:n-1]), linearRob(nums[1:n]))`. Each linear pass uses the O(1)-space rolling-variable trick from House Robber I.
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: `n == 1` → must special-case and return `nums[0]` directly (slicing either side would give an empty array, incorrectly yielding 0); `n == 2` → the two linear runs each contain one house so the answer is `max(nums[0], nums[1])`, which the general formula produces correctly.

#### 🎯 Visual Walkthrough
Worked example: `nums = [1, 2, 3, 1]` → `4`.

Run 1 — exclude last house, linear rob on `[1, 2, 3]`:

| i | 0 | 1 | 2 |
|---|---|---|---|
| nums[i] | 1 | 2 | 3 |
| dp[i] | 1 | 2 | 4 |

Run 2 — exclude first house, linear rob on `[2, 3, 1]`:

| i | 0 | 1 | 2 |
|---|---|---|---|
| nums[i] | 2 | 3 | 1 |
| dp[i] | 2 | 3 | 3 |

Answer = `max(run1, run2) = max(4, 3) = 4` (robbing houses 0 and 2).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
