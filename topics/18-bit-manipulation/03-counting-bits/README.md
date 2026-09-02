# 338. Counting Bits

**Difficulty:** Easy | **Pattern:** Bit Manipulation + DP | **Tags:** Bit Manipulation, DP
**LeetCode:** https://leetcode.com/problems/counting-bits/

## Problem
Given an integer `n`, return an array `ans` of length `n + 1` where `ans[i]` is the number of `1` bits in the binary representation of `i`, for every `i` from `0` to `n`.

**Input:** an integer `n`
**Output:** an integer array of length `n + 1`, the popcount of each number `0..n`

**Examples:**
1. `n = 2` → `[0, 1, 1]`. `0 = 0b00` (0 bits), `1 = 0b01` (1 bit), `2 = 0b10` (1 bit).
2. `n = 5` → `[0, 1, 1, 2, 1, 2]`. `3 = 0b011` (2 bits), `4 = 0b100` (1 bit), `5 = 0b101` (2 bits).
3. `n = 0` → `[0]`. Only `0` itself, which has zero set bits.

**Constraints:** `0 <= n <= 10^5`.

## Intuition (explained simply)
You could count the bits of each number independently using the same trick as "Number of 1 Bits" — that works but recomputes from scratch every time. Instead, notice that every number's bit count is closely related to a smaller number's bit count already computed: removing the lowest set bit, or stripping the last bit off entirely, both connect `i` to a value smaller than itself whose answer you already have.

### 1. Brute Force
- For every `i` from `0` to `n`, independently count `i`'s set bits from scratch (using Brian Kernighan's `i & (i-1)` trick or shifting through all bits), and store the results.
- Correct because each entry is computed directly and independently — no dependency assumptions needed.
- Time complexity: O(n log n) (n numbers, each costing up to O(log i) to count its own bits)  Space complexity: O(n) for the output (which is required anyway)
- Recomputes bit-counting work from scratch for every number even though smaller numbers' answers are already sitting in the output array — pure waste.

### 2. Better
- **DP idea (top-down):** define `bits(i)` = number of set bits in `i`. Recursively, `bits(i) = bits(i & (i-1)) + 1` for `i > 0` (removing the lowest set bit reduces to a strictly smaller subproblem, and adds exactly one bit back), with `bits(0) = 0`.
- Memoize `bits(i)` so each `i` from `0` to `n` is computed once, reusing the answer for `i & (i-1)` which is always some earlier value.
- Time complexity: O(n) (each `i` computed once, O(1) amortized work per call given a smaller value's answer is cached)  Space complexity: O(n) for the memo/cache + recursion stack depth up to O(log n)
- Recursion overhead is unnecessary — the same relation trivially becomes an iterative left-to-right fill.

### 3. Optimal
- **DP state:** let `dp[i]` = the number of set bits in `i`. `dp[0] = 0`.
- **Transition (two equivalent, both O(1) per step):**
  - `dp[i] = dp[i >> 1] + (i & 1)` — the bits of `i` are the bits of `i` with its last bit dropped (`i >> 1`, i.e. `i // 2`), plus 1 if that dropped last bit was a `1`.
  - Or `dp[i] = dp[i & (i - 1)] + 1` — same idea as the "Better" recursion but iterative: `i & (i-1)` is always strictly smaller than `i` and already computed.
- Fill `dp` left to right from `0` to `n`; each entry only looks at an already-computed smaller index, so a single forward pass suffices.
- Time complexity: O(n)  Space complexity: O(n) for the output array (no extra space beyond what's required to return)
- Edge cases: `n = 0` → returns `[0]`; powers of two (e.g. `i=8=0b1000`) always have exactly 1 bit, and the recurrence naturally gives `dp[8] = dp[4] + 0 = dp[2] + 0 = dp[1] + 0 = 1`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n log n) | O(n) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(n) |
