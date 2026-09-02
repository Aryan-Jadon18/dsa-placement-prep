# 43. Multiply Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Pattern](https://img.shields.io/badge/Pattern-Grade%20School%20Multiplication-blue)
![Tags](https://img.shields.io/badge/Tags-Math%2C%20String%2C%20Simulation-lightgrey)

**LeetCode:** https://leetcode.com/problems/multiply-strings/

## Problem
Given two non-negative integers represented as strings, return their product, also as a string. You may **not** use any built-in big-integer library or convert the inputs directly to `int` to do the multiplication (the point of the problem is to simulate the multiplication by hand).

**Input:** `num1: str`, `num2: str` (digits only, no leading zeros unless the number itself is `"0"`).
**Output:** `str` — the product, with no leading zeros (unless the product is `"0"`).

**Example 1:**
`num1 = "2", num2 = "3"` → `"6"`

**Example 2:**
`num1 = "123", num2 = "456"` → `"56088"`
`123 * 456 = 56088`.

**Example 3:**
`num1 = "0", num2 = "12345"` → `"0"`
Anything times zero is zero.

**Constraints:** `1 <= num1.length, num2.length <= 200`, digits only, no leading zeros (except `"0"` itself).

> **🔑 Pattern Recognition:** Multiplying two arbitrary-precision numbers digit by digit → digit `i` times digit `j` always lands at place value `i+j`, so accumulate directly into a fixed-size result array by place, then propagate carries once at the end. The invariant is "place value `i+j`," not string concatenation.

## Intuition (explained simply)
This is exactly the multiplication you learned by hand in school: multiply the first number by each digit of the second number one at a time, shift each partial product left according to place value, and add them all up. The trick to doing it efficiently is realizing that multiplying digit `i` of `num1` by digit `j` of `num2` always contributes to positions `i+j` and `i+j+1` of the result, so we can accumulate directly into a result array instead of adding full partial-product strings one at a time.

### 1. Brute Force
- For each digit of `num2` (from the rightmost), multiply that single digit through all of `num1` (like single-digit multiplication) to get a partial product string, append the right number of trailing zeros for place value, then add that partial product to a running total using **string addition** (digit by digit, just like Plus One's carrying, but for two arbitrary-length numbers).
- Correct because it's literally simulating long multiplication as taught by hand: partial products, shifted, then summed.
- Time complexity: O(n·m) for generating all partial products (n, m = lengths) plus O(n·m) more for repeatedly adding partial products together (each addition can be up to O(n+m)), so roughly O(n·m) overall but with a larger constant from doing separate addition passes.
- Space complexity: O(n+m) for the accumulating result string, plus O(n+m) per partial product.
- Why it's not ideal: allocates and adds many separate intermediate strings — more bookkeeping and string churn than necessary.

### 2. Better
- Same "digit by digit" idea, but instead of building separate partial-product strings and adding them one at a time, accumulate results into a single **integer array** sized `len(num1) + len(num2)`, adding each digit product directly into the correct position (with carrying handled at the very end in one final cleanup pass, rather than immediately after each digit).
- This avoids the overhead of repeated full-string additions, but the carry propagation is deferred and done as a somewhat separate second phase, which is a bit less unified than doing it in one pass.
- Time complexity: O(n·m) (every pair of digits multiplied once)  Space complexity: O(n+m) (the result array)
- Functionally close to optimal — mentioned here as a stepping stone toward the fully clean version.

### 3. Optimal
- Multiply every digit of `num1` by every digit of `num2`, and add each product **directly** into a result array of size `len(num1)+len(num2)` at the right position — digit `i` (from the right) of `num1` times digit `j` (from the right) of `num2` contributes to `result[i+j+1]` (low digit) and adds carry into `result[i+j]` (high digit), immediately propagating any carry into the neighboring position as you go. At the end, strip leading zeros and join the array into the final string.
- Why it works: this is the standard mathematical fact behind long multiplication — the product of the digit at position `i` (worth `10^i`) and the digit at position `j` (worth `10^j`) contributes to place value `10^(i+j)`, and the running carry from each addition naturally spills into the next-higher place, exactly like manual carrying.
- Time complexity: O(n·m) (every digit pair multiplied exactly once — this is optimal for basic long multiplication; faster algorithms like Karatsuba exist but are overkill here)  Space complexity: O(n+m) (the result array)
- Edge cases: either input is `"0"` → result is `"0"`; result naturally has at most `len(num1)+len(num2)` digits, but may have exactly that many minus one (e.g. `99 * 99 = 9801`, 4 digits not 4... check: `9*9=81` 2 digits, arrays sized 4, leading zero stripped) — always strip leading zeros at the end.

#### 🎯 Visual Walkthrough
Tracing `num1 = "123", num2 = "456"` (Example 2, answer `"56088"`). Digit `i` of `num1` (place value `10^i` from the right) times digit `j` of `num2` (place value `10^j`) contributes to place `i+j`:

| Place | Contributing products (`num1[i] * num2[j]`) | Raw sum | + carry in | Digit out | Carry out |
|---|---|---|---|---|---|
| 0 (ones) | `3*6=18` | 18 | 0 | **8** | 1 |
| 1 (tens) | `3*5=15`, `2*6=12` | 27 | 1 | **8** | 2 |
| 2 (hundreds) | `3*4=12`, `2*5=10`, `1*6=6` | 28 | 2 | **0** | 3 |
| 3 (thousands) | `2*4=8`, `1*5=5` | 13 | 3 | **6** | 1 |
| 4 (ten-thousands) | `1*4=4` | 4 | 1 | **5** | 0 |

Reading the digits from the highest place down: `5,6,0,8,8` → `"56088"`, matching `123 * 456 = 56088`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n·m) | O(n+m) |
| Better | O(n·m) | O(n+m) |
| Optimal | O(n·m) | O(n+m) |
