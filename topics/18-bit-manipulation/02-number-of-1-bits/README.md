# 191. Number of 1 Bits

**Difficulty:** Easy | **Pattern:** Bit Manipulation | **Tags:** Bit Manipulation
**LeetCode:** https://leetcode.com/problems/number-of-1-bits/

## Problem
Given an unsigned 32-bit integer `n`, count how many of its bits are set to `1` (its Hamming weight).

**Input:** an unsigned 32-bit integer `n`
**Output:** an integer — the number of `1` bits in `n`'s binary representation

**Examples:**
1. `n = 0b00000000000000000000000000001011` → `3`. Bits set: positions 0, 1, 3.
2. `n = 0b00000000000000000000000010000000` → `1`. A single bit set (bit 7).
3. `n = 0b11111111111111111111111111111101` → `31`. All bits set except one.

**Constraints:** `n` fits in 32 bits, treated as unsigned (LeetCode passes it as a Python `int` already in `[0, 2^32 - 1]`).

## Intuition (explained simply)
The straightforward way is to look at every one of the 32 bit positions and check if it's a `1`. A cleverer way notices that subtracting 1 from a number flips its lowest set bit to 0 (and everything below it to 1s), so `n & (n-1)` always clears exactly the lowest set bit — repeating that operation counts the set bits directly, skipping over all the 0 bits entirely.

### 1. Brute Force
- Loop through all 32 bit positions; for each position `i`, check if bit `i` is set using `(n >> i) & 1`, and count it if so.
- Correct because it directly inspects every bit of the fixed-width representation.
- Time complexity: O(32) = O(1) (bounded by fixed bit-width, but conceptually "check every bit" scales as O(b) for a b-bit integer)  Space complexity: O(1)
- Not really "slow" for 32-bit numbers, but it always does the full 32 iterations even when there are very few set bits — wasteful when the number is sparse (e.g. only 1 or 2 bits set).

### 2. Better
- Convert to a binary string (or repeatedly divide by 2 tracking remainders) and count the `'1'` characters / count of odd remainders.
- Correct because it's an equivalent representation of the same bit-counting process, just via string/division instead of shifting.
- Time complexity: O(32) = O(1), same order as brute force but with string-building overhead  Space complexity: O(32) = O(1) for the string (bounded length)
- Still touches every position (or every bit-length via division) even when most are 0; introduces string allocation overhead unnecessary for pure bit counting.

### 3. Optimal
- **Core insight:** `n & (n - 1)` clears the lowest set bit of `n`. Why: subtracting 1 turns the lowest `1` bit into `0` and all bits below it (which were `0`) into `1`s; ANDing with the original `n` then zeroes exactly that lowest set bit while leaving everything above it unchanged.
- Repeatedly apply `n = n & (n - 1)` and count how many times you can do this before `n` becomes `0` — that count is exactly the number of set bits, since each application removes exactly one `1` bit.
- Time complexity: O(k) where `k` is the number of set bits (at most 32, so effectively O(1), but strictly faster than the brute force's fixed 32 iterations whenever `k < 32`)  Space complexity: O(1)
- Edge cases: `n = 0` → loop never executes, returns 0 immediately; `n` with all 32 bits set (`2^32 - 1`) → takes exactly 32 iterations, same as brute force in the worst case.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(32) | O(1) |
| Better | O(32) | O(1) |
| Optimal | O(k), k = set bits | O(1) |
