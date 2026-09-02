# 7. Reverse Integer

**Difficulty:** Medium | **Pattern:** Math / 32-bit Overflow Handling | **Tags:** Math
**LeetCode:** https://leetcode.com/problems/reverse-integer/

## Problem
Given a signed 32-bit integer `x`, reverse the digits of `x`. If reversing causes the value to fall outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, return `0` instead.

**Input:** a signed 32-bit integer `x`
**Output:** an integer — `x` with its digits reversed, or `0` if that overflows 32-bit signed range

**Examples:**
1. `x = 123` → `321`.
2. `x = -123` → `-321`. The sign is preserved; only the digits are reversed.
3. `x = 1534236469` → `0`. Reversed digits would be `9646324351`, which exceeds `2^31 - 1 = 2147483647`, so we must return `0` instead of the overflowed value.

**Constraints:** `-2^31 <= x <= 2^31 - 1`.

## Intuition (explained simply)
Reversing digits means peeling off the last digit repeatedly (`x % 10`) and building a new number by appending each peeled digit to the front of a running result (`result * 10 + digit`), while shrinking `x` by removing that digit (`x // 10`), until `x` becomes 0. The only real trap is the 32-bit overflow check, since a reversed number can easily land outside the allowed signed range even though the input was valid.

### 1. Brute Force
- Convert `x` to a string, handle the sign separately (strip a leading `-` if present, remember it), reverse the digit characters, convert back to an integer, then reapply the sign. Check the result against the 32-bit signed bounds at the end and return `0` if it's out of range.
- Correct because string reversal is a direct, literal reversal of the digit sequence, and checking bounds afterward catches any overflow.
- Time complexity: O(d) where `d` is the number of digits (string conversion and reversal are linear in digit count)  Space complexity: O(d) for the string representation
- Works fine and is actually reasonably efficient, but relies on string conversion — many interviewers want to see the pure-arithmetic version (no string/array conversion) since that's the spirit of the problem and generalizes better to constrained environments.

### 2. Better
- Do the digit-by-digit arithmetic reversal (`result = result * 10 + x % 10`, `x //= 10`) but only check for 32-bit overflow **after** fully computing `result`, using Python's arbitrary precision to safely accumulate first.
- Correct because the digit-peeling loop is a faithful arithmetic reversal (handles negative `x` correctly since Python's `%` and `//` need care with negative operands — safer to work with `abs(x)` and reapply sign at the end), and checking the final `result` against `[-2^31, 2^31-1]` catches overflow.
- Time complexity: O(d)  Space complexity: O(1) (Python ints don't have a fixed word size, so no true "overflow" happens during computation — this is what makes this version only "better" and not fully faithful to the spirit of a 32-bit-constrained language)
- In a genuinely 32-bit-limited language this approach would overflow *during* accumulation before you even get to check it (undefined behavior in C, wraparound in Java) — the fully "optimal" version checks for overflow **before each multiply/add step**, not after, so it stays correct even if translated to a fixed-width language.

### 3. Optimal
- **Core insight:** check for overflow *before* each digit is appended, not after. Before doing `result = result * 10 + digit`, verify that this operation would not push `result` past `INT_MAX // 10` (or below `INT_MIN // 10`) — and handle the boundary digit case precisely (if `result` already equals the max quotient, the incoming digit must not exceed the max remainder).
- Process digits one at a time via `x % 10` and `x // 10` (using `abs(x)` and reapplying the sign at the very end keeps the modulo logic simple and correct for negative inputs), building `result` the same way as before, but returning `0` immediately the moment an overflow is detected — this mirrors exactly how you'd have to write it in a fixed-width language like C++ or Java, where checking after the fact is too late.
- Time complexity: O(d) where `d` is the number of digits (at most 10 for a 32-bit int)  Space complexity: O(1)
- Edge cases: `x = 0` → returns `0`; `x` ending in trailing zeros (e.g. `x = 120` → reversed is `21`, the leading zero from `120`'s reversal is naturally dropped since arithmetic accumulation doesn't preserve leading zeros); most negative 32-bit int `x = -2147483648` → its reverse would overflow (`8463847412` exceeds range), correctly caught and returns `0`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(d) | O(d) |
| Better | O(d) | O(1) |
| Optimal | O(d) | O(1) |
