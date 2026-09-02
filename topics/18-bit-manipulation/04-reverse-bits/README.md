# 190. Reverse Bits

**Difficulty:** Easy | **Pattern:** Bit Manipulation | **Tags:** Bit Manipulation
**LeetCode:** https://leetcode.com/problems/reverse-bits/

## Problem
Given a 32-bit unsigned integer `n`, reverse the order of its bits (bit 0 becomes bit 31, bit 1 becomes bit 30, and so on) and return the resulting unsigned integer.

**Input:** an unsigned 32-bit integer `n`
**Output:** an unsigned 32-bit integer — `n` with its bits reversed

**Examples:**
1. `n = 0b00000010100101000001111010011100` → `0b00111001011110000010100101000000` (`964176192`). The bit pattern is mirrored end to end.
2. `n = 0b11111111111111111111111111111101` → `0b10111111111111111111111111111111` (`3221225471`). Reversing moves the single `0` bit from position 1 to position 30.
3. `n = 0` → `0`. No bits set, reversal changes nothing.

**Constraints:** `n` fits in 32 bits, treated as unsigned (LeetCode passes it as a Python `int` already in `[0, 2^32 - 1]`).

## Intuition (explained simply)
Reversing bits means the bit currently at position `i` (counting from the least significant bit) needs to end up at position `31 - i`. The most direct way is to literally look at each bit position and place it in its mirrored slot in a new number.

### 1. Brute Force
- Build the result bit-by-bit: for each position `i` from `0` to `31`, extract bit `i` of `n` (`(n >> i) & 1`) and OR it into position `31 - i` of the result.
- Correct because it directly implements the definition of bit reversal — each source bit is placed in its exact mirrored destination.
- Time complexity: O(32) = O(1)  Space complexity: O(1)
- Not actually "slow," but does 32 explicit shift-and-mask operations even though there's a faster convergent trick — mainly included here as the natural first approach, contrasted with a smarter one below.

### 2. Better
- Convert `n` to a 32-character binary string (zero-padded), reverse the string, and parse it back into an integer.
- Correct because reversing the string representation of the bits is equivalent to reversing the bits themselves, as long as the string is exactly 32 characters (zero-padded) so no bit position is dropped.
- Time complexity: O(32) = O(1) (string operations bounded by fixed width)  Space complexity: O(32) = O(1) for the string
- Relies on string allocation and formatting overhead (`format`, `[::-1]`, `int(..., 2)`), which is unnecessary compared to a pure bitwise approach; also easy to get the zero-padding wrong and silently produce incorrect results.

### 3. Optimal
- **Core insight:** build the reversed result by repeatedly shifting the accumulator left, pulling the *lowest* bit off `n`, and appending it — this is the standard "reverse via shifting" pattern also used for reversing digits of a number, but done in binary.
- For `32` iterations: shift `result` left by 1 (making room for a new bit), extract `n`'s lowest bit (`n & 1`) and OR it into `result`, then shift `n` right by 1 to consume that bit. After all 32 iterations, `result` holds the bits of `n` in reverse order.
- Time complexity: O(32) = O(1)  Space complexity: O(1)
- Edge cases: `n = 0` → result stays `0` throughout; `n` with all 32 bits set (`2^32 - 1`) → result is also all 32 bits set (a palindrome under reversal); make sure to run exactly 32 iterations regardless of how many of `n`'s bits are actually set, since trailing zero bits of `n` must become leading (nonzero-position) bits of the result.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(32) | O(1) |
| Better | O(32) | O(1) |
| Optimal | O(32) | O(1) |
