# 371. Sum of Two Integers

**Difficulty:** Medium | **Pattern:** Bit Manipulation (add without +/-) | **Tags:** Bit Manipulation, Math
**LeetCode:** https://leetcode.com/problems/sum-of-two-integers/

## Problem
Given two integers `a` and `b`, compute their sum without using the `+` or `-` operators.

**Input:** two integers `a`, `b` (may be negative), treated as 32-bit signed integers
**Output:** an integer — `a + b`

**Examples:**
1. `a = 1, b = 2` → `3`.
2. `a = 2, b = 3` → `5`.
3. `a = -2, b = 3` → `1`. Must work correctly with negative operands too.

**Constraints:** `-1000 <= a, b <= 1000`, and per LeetCode both `a` and `b` are meant to be treated as 32-bit signed integers (so results must wrap around like real 32-bit arithmetic would, even though Python ints don't naturally overflow).

## Intuition (explained simply)
Addition without `+`/`-` has to be built from bitwise operations: XOR (`^`) combines two bits and gives the sum *ignoring* any carry (`1^1=0`, `1^0=1`, `0^0=0` — matches addition except it drops the carry-out of `1+1`), while AND (`&`) followed by a left shift (`<<1`) produces exactly the carry that XOR dropped. Add the "sum without carry" and the "carry" together the same way, repeating until there's no carry left — this is literally how a hardware adder works, bit by bit.

### 1. Brute Force
- Simulate addition by incrementing/decrementing one number toward zero while adjusting the other, using only `+1`/`-1` steps built from bitwise increment (or, since Python forbids `+`/`-` on the values but the LOOP COUNTER itself isn't restricted by the problem's intent, use repeated bit-increment: to add `b` to `a`, repeat "increment `a`, decrement `b`" `|b|` times using bitwise increment/decrement helpers).
- Correct because it reduces addition to repeated unit steps, which can each be built from bitwise logic (e.g. incrementing via `-(-x-1)` style bit tricks, or via the same XOR/AND/carry logic applied to a fixed operand of 1).
- Time complexity: O(max(|a|, |b|)) — proportional to the magnitude of the operands, since we step one unit at a time  Space complexity: O(1)
- Extremely slow for large magnitudes (e.g. adding `1000 + 1000` takes on the order of 1000 iterations) — doesn't scale, and is really just avoiding `+`/`-` in the most literal, inefficient way.

### 2. Better
- Use Python's arbitrary-precision integers with the **carry-propagation trick applied in bulk via string/array digit addition** — e.g. convert both numbers to their binary digit lists and manually add digit-by-digit with a carry variable, similar to how you'd add two numbers on paper.
- Correct because manual digit-by-digit addition with carry propagation is exactly how addition is mathematically defined, just implemented explicitly instead of relying on `+`.
- Time complexity: O(log(max(|a|,|b|))) — proportional to the number of bits/digits, a big improvement over unit stepping  Space complexity: O(log(max(|a|,|b|))) for the digit lists
- Still builds and manipulates lists/strings of digits, which is more overhead than necessary; the pure bitwise XOR/AND/carry approach achieves the same asymptotic complexity with O(1) space and no data structure overhead — that's the true optimal for this specific "no +/-" challenge.

### 3. Optimal
- **Core insight:** `a ^ b` gives the sum of `a` and `b` at every bit position *without* carrying. `(a & b) << 1` gives exactly the carry bits that need to be added in. So `a + b` equals `(a ^ b) + ((a & b) << 1)` — but the right-hand side is itself an addition, so apply the same transformation repeatedly: `a, b = a ^ b, (a & b) << 1` in a loop, until the carry `b` becomes `0`. At that point `a` holds the final sum.
- **32-bit correctness:** Python integers don't wrap around like a real 32-bit register, so we must simulate that. Mask both operands to 32 bits after every operation (`& 0xFFFFFFFF`), and at the very end, if the result's 32nd bit (the sign bit) is set, convert it from the unsigned 32-bit representation back to a negative Python int by subtracting `2^32`.
- Time complexity: O(1) — bounded by the fixed 32-bit width (at most 32 iterations of carry propagation)  Space complexity: O(1)
- Edge cases: both negative (`a=-2, b=-3` → `-5`, needs correct sign-bit handling after masking); one zero (`a=0, b=x` → `x`, loop exits immediately since carry is `0`); result crosses the signed 32-bit range boundary (must reinterpret using the `2^32` subtraction trick, otherwise you'd get an incorrect large positive number instead of the expected negative wraparound).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(max(\|a\|,\|b\|)) | O(1) |
| Better | O(log(max(\|a\|,\|b\|))) | O(log(max(\|a\|,\|b\|))) |
| Optimal | O(1) (32-bit bounded) | O(1) |
