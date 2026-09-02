# 494. Target Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Pattern](https://img.shields.io/badge/Pattern-0%2F1%20Knapsack-blue) ![Tags](https://img.shields.io/badge/Tags-DP%2C%20Backtracking-lightgrey)
**LeetCode:** https://leetcode.com/problems/target-sum/

## Problem
Given an array of non-negative integers and a target value, assign either a `+` or a `-` sign in front of every number, then sum them all up. Count how many different sign assignments make the total sum equal the target.

Input: `nums` (list of non-negative integers), `target` (integer).
Output: an integer, the count of sign assignments that reach `target`.

**Example 1:** `nums = [1,1,1,1,1], target = 3` → `5`. There are 5 ways to place +/- signs so the sum is 3 (e.g. `+1+1+1+1-1=3`, and four more variants).

**Example 2:** `nums = [1], target = 1` → `1`. Only `+1 = 1` works (`-1 = -1` does not).

**Example 3:** `nums = [1,0], target = 1` → `2`. `+1+0=1` and `+1-0=1` are both valid (the 0 can take either sign and still equal 1).

Constraints: `0 <= nums.length <= 20`, `0 <= nums[i] <= 1000`, `0 <= sum(nums) <= 1000`, `-1000 <= target <= 1000`.

> 🔑 **Pattern Recognition**
> "Count sign assignments hitting a target" algebraically reduces to "count subsets summing to a fixed value `P`" — once you spot that reduction, it's the same counting 0/1 knapsack as Partition Equal Subset Sum, just with a derived target instead of half the total.

## Intuition (explained simply)
Every number ends up in one of two "buckets": the ones we gave a `+` sign (call their sum `P`) and the ones we gave a `-` sign (call their sum `N`). We know `P + N = sum(nums)` (every number is in exactly one bucket) and we want `P - N = target`. Adding those two equations: `2P = sum(nums) + target`, so `P = (sum(nums) + target) / 2`. This turns "count sign assignments" into "count subsets of `nums` that sum to a fixed value `P`" — the classic 0/1 knapSack *counting* problem (each number is either in the subset or not, used at most once).

### 1. Brute Force
- Recurse over `(index, running_sum)`: at each number, try both `+nums[i]` and `-nums[i]`, and recurse to the next index. Base case: `index == len(nums)` → count 1 if `running_sum == target`, else 0.
- Correct because it literally enumerates every possible +/- assignment.
- Time complexity: O(2^n) — two choices per number. Space complexity: O(n) recursion depth.
- With `n` up to 20 this is ~1,000,000 branches — technically survivable but it's the wrong idea; it doesn't scale and interviewers want the knapsack reduction.

### 2. Better
- The recursion only depends on `(index, running_sum)`, so memoize it (top-down DP). Note `running_sum` can range over `[-sum(nums), sum(nums)]`, so shift it by an offset to index into an array/dict.
- Correctness is preserved, same recurrence, now cached.
- Time complexity: O(n * sum(nums)) — number of distinct `(index, sum)` pairs. Space complexity: O(n * sum(nums)) for the memo + O(n) recursion stack.
- Still framed as a sum-tracking recursion rather than the cleaner subset-sum reduction, and carries recursion + hashing overhead.

### 3. Optimal
- Reduce to subset sum: let `P = (sum(nums) + target) / 2` be the target size of the "positive" subset. If `sum(nums) + target` is negative or odd, no assignment can work — return 0 immediately.
- Define `dp[j]` = number of subsets of the numbers processed *so far* that sum exactly to `j`. Initialize `dp[0] = 1` (the empty subset sums to 0). For each number `num`, update `dp[j] -= dp[j - num]`-style — concretely `dp[j] += dp[j - num]` for `j` from `P` down to `num` (descending, so each number is used at most once — this is standard 0/1 knapsack).
- This works because it's exactly "how many ways to pick a subset summing to `P`", and descending the inner loop guarantees each `num` contributes to at most one selection per subset (no reuse), matching the 0/1 constraint (each number gets exactly one sign, not repeats).
- Time complexity: O(n * sum(nums)). Space complexity: O(sum(nums)) — a single 1D array.
- Edge cases: `target` magnitude larger than `sum(nums)` → impossible, answer 0; `sum(nums) + target` odd → impossible (can't split into two equal-parity buckets), answer 0; a `0` in `nums` doubles the count of whatever ways exist without it (it can take either sign), which the DP naturally captures since `dp[j] += dp[j-0]` doubles `dp[j]`.

#### 🎯 Visual Walkthrough
Worked example: `nums = [1, 1, 1, 1, 1]`, `target = 3` → `5`. `P = (sum(nums) + target) / 2 = (5 + 3) / 2 = 4`. Each row shows `dp[j]` (number of subsets summing to `j`) after one more `1` has been processed (0/1 knapsack, `j` iterated descending per item).

| after # of 1's | dp[0] | dp[1] | dp[2] | dp[3] | dp[4] |
|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 |
| 2 | 1 | 2 | 1 | 0 | 0 |
| 3 | 1 | 3 | 3 | 1 | 0 |
| 4 | 1 | 4 | 6 | 4 | 1 |
| 5 | 1 | 5 | 10 | 10 | 5 |

Answer = `dp[P] = dp[4] = 5` — the 5 ways to choose which four of the five `1`s get `+` (and the remaining one gets `-`) so the sum is `3`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n * sum(nums)) | O(n * sum(nums)) |
| Optimal | O(n * sum(nums)) | O(sum(nums)) |
