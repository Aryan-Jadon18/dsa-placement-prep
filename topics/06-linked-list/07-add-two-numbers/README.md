# 2. Add Two Numbers

**Difficulty:** Medium | **Pattern:** Linked List Simulation | **Tags:** Linked List, Math, Recursion
**LeetCode:** https://leetcode.com/problems/add-two-numbers/

## Problem
Two non-negative integers are stored as linked lists where each node holds a single
digit, and the digits are stored in **reverse order** (the head is the ones digit).
Add the two numbers and return the sum as a linked list in the same reversed-digit
format.

**Input:** two linked lists `l1`, `l2`, each representing a non-negative integer with
digits in reverse order
**Output:** a linked list representing the sum, digits in reverse order

**Examples**
1. `l1 = 2 -> 4 -> 3` (= 342), `l2 = 5 -> 6 -> 4` (= 465) → `7 -> 0 -> 8` (= 807),
   since 342 + 465 = 807.
2. `l1 = 0`, `l2 = 0` → `0`. Zero plus zero is zero.
3. `l1 = 9 -> 9 -> 9 -> 9`, `l2 = 9 -> 9` → `8 -> 9 -> 0 -> 0 -> 1`, i.e.
   9999 + 99 = 10098, demonstrating carries propagating and the result having one
   more digit than either input.

**Constraints:** each list has `[1, 100]` nodes, `0 <= Node.val <= 9`, no leading
zeros in the represented numbers except the number `0` itself.

## Intuition (explained simply)
This is exactly how you add two numbers by hand on paper, digit by digit from the
ones place, carrying a `1` to the next column whenever a column sums to 10 or more —
except here the "columns" are already conveniently ordered from least-significant
digit first, since the lists store digits in reverse order.

### 1. Brute Force
- Convert each linked list into an actual integer (walk the list, multiply-accumulate
  digits by increasing powers of 10), add the two integers using normal Python
  arithmetic, then convert the resulting integer back into a reversed-digit linked
  list.
- Correct because it just leans on Python's built-in arbitrary-precision integers to
  do the addition for us.
- Time complexity: O(m+n) (dominated by walking both lists to build the numbers, and
  building the digits of the result — Python big-int arithmetic itself is not O(1)
  but is roughly linear in digit count too) Space complexity: O(m+n)
- Why it's not good enough for an interview: relying on the language's big-integer
  support sidesteps the actual point of the problem, which is to simulate digit-wise
  addition with carries yourself — most interviewers will ask you not to convert to
  int, or will consider it an incomplete answer.

### 2. Better
- Manually simulate the addition but in two explicit phases: first walk both lists
  to collect digits into two arrays (padding the shorter one conceptually with
  zeros), then do a manual digit-by-digit array addition with carry propagation, and
  finally build the result linked list from the resulting digit array.
- Time complexity: O(m+n)  Space complexity: O(m+n) (digit arrays + result list)
- Still suboptimal: doesn't need the intermediate arrays at all — the carry can be
  tracked with a single variable while walking both lists directly in one pass and
  building the result list as we go.

### 3. Optimal — Single-Pass Digit Simulation
- Walk `l1` and `l2` simultaneously (using `0` for a list that has run out of
  digits), maintaining a running `carry` (starts at 0). At each step compute
  `total = digit1 + digit2 + carry`, the new digit is `total % 10`, and the new
  `carry` is `total // 10`. Append the new digit to the result list (built with a
  dummy head + tail pointer). Continue while either list still has nodes or `carry`
  is nonzero (a leftover carry after both lists end adds one more digit, as in the
  9999 + 99 example).
- Why it works: this is literally elementary-school column addition; because both
  lists are already ordered from least-significant digit, the carry only ever needs
  to flow "forward" (to the next node), matching the direction we're already walking.
- Time complexity: O(max(m, n))  Space complexity: O(max(m, n)) for the output list
  (unavoidable — the output itself must be built), O(1) auxiliary space beyond that.
- Edge cases: lists of different lengths, a final leftover carry producing an extra
  digit, both inputs being `0`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(m+n) | O(m+n) |
| Better | O(m+n) | O(m+n) |
| Optimal | O(max(m,n)) | O(max(m,n)) output, O(1) extra |
