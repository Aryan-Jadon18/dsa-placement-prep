# 416. Partition Equal Subset Sum

**Difficulty:** Medium | **Pattern:** 0/1 Knapsack DP | **Tags:** DP
**LeetCode:** https://leetcode.com/problems/partition-equal-subset-sum/

## Problem
Given an array of positive integers `nums`, determine whether it can be split into two subsets such that the sum of elements in both subsets is equal.

**Input:** an integer array `nums`
**Output:** a boolean — `true` if such an equal-sum partition exists

**Examples:**
1. `nums = [1, 5, 11, 5]` → `true`. Split into `[1, 5, 5]` (sum 11) and `[11]` (sum 11).
2. `nums = [1, 2, 3, 5]` → `false`. Total sum is 11 (odd), so an equal split is impossible.
3. `nums = [1, 2, 5]` → `false`. Total sum is 8, target half is 4, but no subset sums to exactly 4.

**Constraints:** `1 <= nums.length <= 200`, `1 <= nums[i] <= 100`.

## Intuition (explained simply)
If the total sum is odd, an equal split is mathematically impossible — stop immediately. Otherwise the question becomes: "can some subset of `nums` sum to exactly `total / 2`?" (the other subset automatically sums to the other half). This is the classic 0/1 knapsack question — each number is either included in our target-sum subset or not, and each number can be used at most once.

### 1. Brute Force
- Plain recursion `canReach(i, remaining)`: at index `i`, either include `nums[i]` (recurse with `remaining - nums[i]` and `i+1`) or exclude it (recurse with `remaining` and `i+1`). Success if `remaining == 0` is reached. Try both choices at every index.
- Correct because it's an exhaustive search over every possible subset (include/exclude for each element).
- Time complexity: O(2^n) (two choices per element)  Space complexity: O(n) recursion stack
- Full subset enumeration — the same `(i, remaining)` state is reached via many different inclusion/exclusion paths, causing massive recomputation.

### 2. Better
- Memoize `canReach(i, remaining)` on the pair `(i, remaining)` so each distinct state is solved once (top-down DP).
- Same correctness argument, cached.
- Time complexity: O(n * target) where `target = total / 2`  Space complexity: O(n * target) cache + O(n) recursion stack
- The 2D cache and recursion overhead are avoidable; also each item must only be usable once (0/1, not unbounded), which needs care in the iteration order for the tabulated version.

### 3. Optimal
- **DP state:** let `dp[s]` = `True` if some subset of the numbers processed *so far* sums to exactly `s`, else `False`. Initialize `dp[0] = True` (the empty subset always sums to 0), rest `False`.
- **Transition:** for each number `num` in `nums`, for `s` from `target` down to `num`: `dp[s] = dp[s] or dp[s - num]` — "can we make `s` either without using `num` (already known) or by using `num` on top of `s - num`?" The reverse-order iteration (high to low) is essential — it ensures each `num` is only applied once per subset (0/1 knapsack), since iterating forward would let the same `num` be reused within the same pass, which is unbounded knapsack instead.
- After processing all numbers, the answer is `dp[target]` where `target = total // 2` (only computed if `total` is even).
- Time complexity: O(n * target)  Space complexity: O(target)
- Edge cases: odd total sum → return `false` immediately without running the DP; single-element array → can never split into two nonempty... actually the problem doesn't require both subsets nonempty in general but with one element you can't reach `target = element/2` unless the element is 0, so effectively always `false` for a single positive element; all elements equal and count is even → always `true`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n · target) | O(n · target) |
| Optimal | O(n · target) | O(target) |
