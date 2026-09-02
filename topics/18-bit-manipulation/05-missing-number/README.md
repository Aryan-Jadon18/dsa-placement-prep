# 268. Missing Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Pattern](https://img.shields.io/badge/Pattern-XOR%20%2F%20Math-blue) ![Tags](https://img.shields.io/badge/Tags-Bit%20Manipulation%20%7C%20Array%20%7C%20Math-lightgrey)
**LeetCode:** https://leetcode.com/problems/missing-number/

## Problem
Given an array `nums` containing `n` distinct numbers taken from the range `[0, n]`, find the one number in that range that is missing from the array.

**Input:** an integer array `nums` of length `n`, values distinct, drawn from `[0, n]`
**Output:** an integer — the missing value

**Examples:**
1. `nums = [3, 0, 1]` → `2`. `n = 3`, range is `[0, 3]`, array has `{3, 0, 1}`, missing `2`.
2. `nums = [0, 1]` → `2`. `n = 2`, range is `[0, 2]`, array has `{0, 1}`, missing `2`.
3. `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]` → `8`. `n = 9`, every value 0-9 except 8 is present.

**Constraints:** `1 <= n <= 10^4` (array length), all values distinct and in `[0, n]`.

> 🔑 **Pattern Recognition**
> "n distinct values from a known full range, exactly one missing" → XOR every index against every value; present numbers pair up and cancel, leaving only the unmatched one. Same cancellation idea as Single Number, applied to indices instead of duplicates.

## Intuition (explained simply)
If every number from `0` to `n` were present, they'd sum to a known fixed total (`n*(n+1)/2`). Since exactly one number is missing, the difference between that expected total and the array's actual sum is exactly the missing number. XOR offers an equivalent trick without any risk of numeric overflow: XOR-ing all indices `0..n` with all array values makes every present number cancel with its index-partner, leaving only the missing one.

### 1. Brute Force
- For each number `i` from `0` to `n`, scan the array to check whether `i` is present (`i in nums` implemented as a linear scan); return the first `i` not found.
- Correct because it directly tests set membership against the definition of "missing."
- Time complexity: O(n^2) (n candidates, each checked with an O(n) scan)  Space complexity: O(1) extra
- Quadratic — very wasteful since we're repeatedly rescanning the same array.

### 2. Better
- Put all array values into a hash set first (O(n)), then for each `i` from `0` to `n`, do an O(1) membership check against the set and return the first missing one. (Equivalently: sort the array and scan for the first index where `nums[i] != i`.)
- Correct because the hash set gives O(1) average lookups, turning the repeated scan into repeated O(1) checks.
- Time complexity: O(n)  Space complexity: O(n) for the hash set
- Uses O(n) extra space; there's a purely arithmetic/bitwise approach that needs none.

### 3. Optimal
- **Core insight (XOR version):** XOR every index `0..n` together with every value in `nums`. Every value that's actually present cancels with its matching index (`x ^ x = 0`), because the array is a permutation of `[0, n]` minus one element — so all present numbers appear exactly twice in the combined XOR (once as an index, once as an array value) and cancel, leaving only the missing number (which appears once, as an index only).
- Equivalently (arithmetic version): compute `expected_sum = n*(n+1)//2` and `actual_sum = sum(nums)`; the missing number is `expected_sum - actual_sum`. Both approaches are O(n) time O(1) space; XOR is preferred when overflow safety matters (irrelevant in Python's arbitrary-precision ints, but standard practice in fixed-width languages).
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: `nums = [0]` → `n=1`, missing is `1`; missing number is `0` itself (e.g. `nums=[1,2]`, `n=2`) → both XOR and sum approaches handle this correctly since `0` contributes nothing to XOR/sum either way, but it's still correctly identified as unmatched.

#### 🎯 Visual Walkthrough
Tracing the XOR-all-indices-and-values approach on Example 1's `nums = [3, 0, 1]` (`n = 3`, expected answer `2`):

| XOR with | Source | Running XOR |
|---|---|---|
| — | start | 0 |
| 0 | index 0 | 0 |
| 1 | index 1 | 1 |
| 2 | index 2 | 3 |
| 3 | index 3 | 0 |
| 3 | nums[0] | 3 |
| 0 | nums[1] | 3 |
| 1 | nums[2] | **2** |

Indices `0`, `1`, `3` each cancel with their matching value in `nums`; index `2` has no partner in the array, so it survives as the final result `2`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(1) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
