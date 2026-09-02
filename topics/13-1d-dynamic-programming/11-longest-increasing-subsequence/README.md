# 300. Longest Increasing Subsequence

**Difficulty:** Medium | **Pattern:** 1D DP / Binary Search (patience sorting) | **Tags:** DP, Binary Search
**LeetCode:** https://leetcode.com/problems/longest-increasing-subsequence/

## Problem
Given an integer array `nums`, find the length of the longest strictly increasing subsequence (elements don't need to be contiguous, but must keep their original relative order and each must be strictly greater than the previous).

**Input:** an integer array `nums`
**Output:** an integer — the length of the longest strictly increasing subsequence

**Examples:**
1. `nums = [10, 9, 2, 5, 3, 7, 101, 18]` → `4`. One such subsequence: `[2, 3, 7, 101]` (or `[2, 3, 7, 18]`).
2. `nums = [0, 1, 0, 3, 2, 3]` → `4`. Example: `[0, 1, 2, 3]`.
3. `nums = [7, 7, 7, 7]` → `1`. Strictly increasing means no repeats allowed, so the best is any single element.

**Constraints:** `1 <= nums.length <= 2500`, `-10^4 <= nums[i] <= 10^4`.

## Intuition (explained simply)
For every element, ask: "what's the longest increasing subsequence that *ends* right here?" That depends on all earlier elements that are smaller than the current one — pick whichever of those had the longest subsequence ending at it, and extend by one.

### 1. Brute Force
- Plain recursion `lengthFrom(i)` = the longest increasing subsequence starting at index `i` (using `nums[i]` as the first element). For each `j > i` with `nums[j] > nums[i]`, recursively try extending: `1 + lengthFrom(j)`. The answer is `1` plus the best extension found, or just `1` if nothing extends it. Try every possible starting index and take the max.
- Correct because it exhaustively considers, for every possible next chosen element, whether including it extends the subsequence, covering all possible increasing subsequences.
- Time complexity: O(2^n) (each element can be included or excluded, but the "must increase" constraint prunes some branches, not enough to avoid exponential worst case)  Space complexity: O(n) recursion stack
- Overlapping subproblems: `lengthFrom(j)` gets recomputed from many different earlier starting indices.

### 2. Better
- Memoize `lengthFrom(i)` so each starting index's best-length-from-here is computed once (top-down DP).
- Same correctness argument, but cached — each of the `n` states resolved once, each doing O(n) work to check all `j > i`.
- Time complexity: O(n^2)  Space complexity: O(n) cache + O(n) recursion stack
- Recursion overhead remains; also doesn't reach the theoretically faster O(n log n) approach.

### 3. Optimal
Two valid "optimal" mindsets — the O(n^2) tabulation is the standard DP answer; the O(n log n) patience-sorting trick is the truly optimal one for large inputs. This file implements the O(n log n) version since it's what's expected at the FAANG bar, but the DP state is explained first since it's what interviewers probe.
- **DP state (O(n^2) version):** let `dp[i]` = length of the longest increasing subsequence that *ends* at index `i` (using `nums[i]` as the last element). `dp[i] = 1` at minimum (the element alone).
- **Transition:** `dp[i] = 1 + max(dp[j] for all j < i where nums[j] < nums[i])`, or `dp[i] = 1` if no such `j` exists. The answer is `max(dp)` over all `i`.
- **O(n log n) trick:** maintain an array `tails` where `tails[k]` = the smallest possible tail value of any increasing subsequence of length `k+1` found so far. For each new number, binary-search `tails` for the first position where `tails[pos] >= num` and overwrite it with `num` (or append if `num` is larger than everything in `tails`). This works because keeping the tail as small as possible always gives future numbers the best chance to extend the subsequence — `tails` doesn't literally track *a* valid subsequence, but its *length* always equals the true LIS length.
- Time complexity: O(n log n)  Space complexity: O(n) for the `tails` array
- Edge cases: strictly decreasing array → answer is 1; all equal elements → answer is 1 (strict inequality required); already sorted increasing → answer is `n`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(2^n) | O(n) |
| Better | O(n^2) | O(n) |
| Optimal | O(n log n) | O(n) |
