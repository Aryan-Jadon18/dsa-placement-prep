# 198. House Robber

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-1D%20DP-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20Array-lightgrey)
**LeetCode:** https://leetcode.com/problems/house-robber/

## Problem
You're a robber planning to rob houses along a street, where `nums[i]` is the money in house `i`. Adjacent houses have connected security systems — if you rob two adjacent houses in the same night, the alarm goes off. Find the maximum money you can rob without robbing two adjacent houses.

**Input:** an integer array `nums` (money per house)
**Output:** an integer — the maximum sum obtainable with no two chosen indices adjacent

**Examples:**
1. `nums = [1, 2, 3, 1]` → `4`. Rob house 0 and house 2: `1 + 3 = 4`.
2. `nums = [2, 7, 9, 3, 1]` → `12`. Rob houses 0, 2, 4: `2 + 9 + 1 = 12`.
3. `nums = [5]` → `5`. Only one house, rob it.

**Constraints:** `1 <= nums.length <= 100`, `0 <= nums[i] <= 400`.

> 🔑 **Pattern Recognition**
> At every house you make an include-or-exclude decision, and the best result so far depends only on the best results at the previous one or two houses — an optimal choice at each step built from overlapping smaller subproblems → classic 1D DP.

## Intuition (explained simply)
At every house you face a binary choice: rob it (and skip the previous one) or skip it (and keep whatever was best up to the previous house). The best total at house `i` is whichever of those two choices is bigger.

### 1. Brute Force
- Plain recursion `rob(i)` = the best money obtainable using houses `i, i+1, ..., n-1`. At house `i` you either rob it and recurse from `i+2`, or skip it and recurse from `i+1`: `rob(i) = max(nums[i] + rob(i+2), rob(i+1))`. Base case: `rob(i) = 0` when `i >= n`.
- Correct because it exhaustively tries both choices at every house.
- Time complexity: O(2^n)  Space complexity: O(n) (recursion stack)
- Overlapping subproblems — `rob(k)` for the same `k` gets recomputed from many different call paths, exponential blowup.

### 2. Better
- Memoize `rob(i)` so each starting index is solved once (top-down DP).
- Same recursive logic, but cached — no recomputation.
- Time complexity: O(n)  Space complexity: O(n) cache + O(n) recursion stack
- Function-call overhead and stack depth are wasted; an iterative version needs only the last two answers.

### 3. Optimal
- **DP state:** let `dp[i]` = the maximum money obtainable considering houses `0..i` (inclusive).
- **Transition:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` — either skip house `i` (carry forward `dp[i-1]`) or rob it (take `dp[i-2]` plus its value).
- **Base cases:** `dp[-1] = 0` (no houses), `dp[0] = nums[0]`.
- Build up left to right; since `dp[i]` only depends on the previous two values, keep two rolling variables instead of a full array.
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: single house (`dp[0] = nums[0]`), two houses (`max(nums[0], nums[1])`), all zeros (answer 0).

#### 🎯 Visual Walkthrough
Worked example: `nums = [1, 2, 3, 1]` → `4`.

| i | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| nums[i] | 1 | 2 | 3 | 1 |
| dp[i] | 1 | 2 | 4 | 4 |

`dp[i] = max(dp[i-1], dp[i-2] + nums[i])` — e.g. `dp[2] = max(dp[1], dp[0]+nums[2]) = max(2, 1+3) = 4` (rob houses 0 and 2), and `dp[3] = max(dp[2], dp[1]+nums[3]) = max(4, 2+1) = 4` (robbing house 3 doesn't help).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
