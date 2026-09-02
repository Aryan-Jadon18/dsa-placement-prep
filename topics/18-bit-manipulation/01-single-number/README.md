# 136. Single Number

**Difficulty:** Easy | **Pattern:** Bit Manipulation — XOR | **Tags:** Bit Manipulation
**LeetCode:** https://leetcode.com/problems/single-number/

## Problem
Given a non-empty array `nums` where every element appears exactly twice except for one element which appears exactly once, find that single element. Ideally solve it in linear time with constant extra space.

**Input:** an integer array `nums`
**Output:** an integer — the element that appears only once

**Examples:**
1. `nums = [2, 2, 1]` → `1`.
2. `nums = [4, 1, 2, 1, 2]` → `4`.
3. `nums = [1]` → `1`. Only one element total, so it's trivially the answer.

**Constraints:** `1 <= nums.length <= 3*10^4`, `-3*10^4 <= nums[i] <= 3*10^4`, exactly one element appears once and every other element appears exactly twice.

## Intuition (explained simply)
XOR (`^`) has two useful properties: `x ^ x = 0` (a number cancels itself out) and `x ^ 0 = x` (XOR-ing with zero changes nothing), and XOR is commutative/associative so order doesn't matter. If we XOR every element together, every pair cancels itself to 0, leaving only the number that had no partner.

### 1. Brute Force
- For each element, count how many times it appears in the whole array (nested loop or `.count()`); return the one whose count is 1.
- Correct because it directly checks the defining property of the answer (appears exactly once).
- Time complexity: O(n^2)  Space complexity: O(1) extra
- Quadratic — checking every element against the whole array again is wasteful, especially since we already know exactly one element is unique.

### 2. Better
- Use a hash map (or hash set) to count occurrences of each number in one pass, then scan the map for the number with count 1 (or: add to a set on first sight, remove on second sight — whatever remains in the set at the end is the answer).
- Correct because a hash map gives O(1) average lookups/updates, and every number is counted exactly once via one linear pass.
- Time complexity: O(n)  Space complexity: O(n) for the hash map
- Uses extra space proportional to the input, when the problem explicitly wants constant space — there's a pure-math/bitwise trick that avoids the map entirely.
- (Bit-manipulation framing: same technique applies to problems like "counting bits" — but here the O(1)-space bitwise trick is even simpler, shown next.)

### 3. Optimal
- **Core insight:** XOR every element in the array together into a running accumulator. Every number that appears twice contributes `x ^ x = 0` to the accumulator (in some order, since XOR is commutative and associative, pairs always cancel regardless of position), leaving only the singleton's value.
- Initialize `result = 0`, then `result ^= num` for every `num` in `nums`. At the end, `result` is the answer.
- Time complexity: O(n)  Space complexity: O(1)
- Edge cases: single-element array (the accumulator starts at 0, XOR with the one element gives that element directly — correct); negative numbers (XOR works the same on Python's two's-complement-like bit representation for this purpose since we never inspect sign bits directly, only accumulate and return the final integer).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(1) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
