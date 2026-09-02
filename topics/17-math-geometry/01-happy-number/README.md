# 202. Happy Number

**Difficulty:** Easy | **Pattern:** Math / Cycle Detection | **Tags:** Math, Two Pointers, Hash Table
**LeetCode:** https://leetcode.com/problems/happy-number/

## Problem
A number is "happy" if, when you repeatedly replace it with the sum of the squares of its digits, you eventually reach `1`. If instead you enter a repeating loop that never includes `1`, the number is not happy. Given a positive integer, determine if it's happy.

**Input:** `n: int` (positive integer).
**Output:** `True` if `n` is happy, `False` otherwise.

**Example 1:**
`n = 19` → `True`
`1² + 9² = 82`, `8² + 2² = 68`, `6² + 8² = 100`, `1² + 0² + 0² = 1`. We hit 1, so it's happy.

**Example 2:**
`n = 2` → `False`
`2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...` — this loops back to `4` forever without ever reaching 1.

**Example 3:**
`n = 1` → `True`
Already 1 — trivially happy (zero steps needed).

**Constraints:** `1 <= n <= 2^31 - 1`.

## Intuition (explained simply)
This is really a **cycle detection** problem in disguise. Repeatedly applying "sum of squares of digits" defines a sequence of numbers. Either that sequence eventually lands on 1 (happy), or — because the sum of squares of digits is bounded (a number with `d` digits produces a sum of at most `81d`, which is far smaller once `d` gets large), the sequence *must* eventually repeat a value, creating a cycle that never includes 1 (not happy). So the real question becomes: "does this sequence reach 1, or does it cycle?"

### 1. Brute Force
- Simulate the digit-square-sum process, storing every value seen in a hash set. If we ever produce `1`, return `True`. If we ever produce a value we've already seen before, we're in a loop that skips 1, so return `False`.
- Correct because a bounded sequence that doesn't reach 1 is guaranteed to eventually repeat a previously-seen value (pigeonhole principle), and storing everything we've seen lets us detect that reliably.
- Time complexity: O(log n) per squaring step, and the sequence enters a small bounded cycle quickly in practice, so overall it's roughly O(log n) amortized (bounded by how fast values shrink into a small range) Space complexity: O(k) where k is the number of distinct values visited before a repeat.
- Why it's "brute": it uses extra space to remember history — an interviewer will ask if you can do it with O(1) space.
- Time complexity: O(log n) (numbers shrink fast)  Space complexity: O(k), extra memory for the seen-set.

### 2. Better
- Same simulation, but cap it with a hard iteration limit (e.g. a few hundred steps) instead of a hash set, relying on the mathematical fact that any non-happy number cycles within a very small number of steps (the known cycle is short: `4→16→37→58→89→145→42→20→4`). If we haven't hit 1 within that generous limit, declare it not happy.
- This avoids storing history at the cost of relying on an external mathematical fact rather than deriving termination directly from the algorithm itself — less rigorous, so it's a stepping stone rather than the preferred final answer.
- Time complexity: O(1) practically (bounded iteration count) but not truly general-purpose, Space complexity: O(1)
- Not fully rigorous/self-contained as a proof of correctness — the true general technique is cycle detection with O(1) space, shown next.

### 3. Optimal
- Use **Floyd's Cycle Detection** (slow/fast pointers), the same trick used to detect a cycle in a linked list — except here, "the next node" is computed by the digit-square-sum function instead of following a `.next` pointer. Move `slow` one step at a time and `fast` two steps at a time. If `fast` (or `slow`) ever reaches `1`, the number is happy. If `slow == fast` while neither is `1`, we've found a cycle that never reaches 1 — not happy.
- Why it works: exactly the same reasoning as detecting a cycle in a linked list — a fast pointer moving twice as fast as a slow one is guaranteed to eventually "lap" the slow pointer if (and only if) they're both stuck going around a finite loop.
- Time complexity: O(log n) (bounded by how fast the sequence shrinks into its small cycle range)  Space complexity: O(1) — no extra data structure needed.
- Edge cases: `n = 1` (immediately happy); single-digit numbers; very large `n` near `2^31 - 1` (still shrinks fast because of how few digits it has).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(log n) | O(k) |
| Better | O(1) (bounded) | O(1) |
| Optimal | O(log n) | O(1) |
