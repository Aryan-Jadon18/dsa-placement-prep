# 312. Burst Balloons

**Difficulty:** Hard | **Pattern:** Interval DP | **Tags:** DP
**LeetCode:** https://leetcode.com/problems/burst-balloons/

## Problem
You have `n` balloons in a row, each with a number on it (`nums[i]`). Bursting balloon `i` earns `nums[left] * nums[i] * nums[right]` coins, where `left` and `right` are the *currently adjacent* balloons at the moment you burst it (bursting removes it from the row, so its old neighbors become newly adjacent to each other). Treat out-of-bounds neighbors (before the first, after the last) as having value `1`. Choose a bursting order that maximizes total coins.

Input: `nums`, a list of integers (balloon values).
Output: an integer, the maximum coins obtainable by bursting all balloons.

**Example 1:** `nums = [3,1,5,8]` → `167`. One optimal order bursts `1`, then `5`, then `3`, then `8`, earning `3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15+120+24+8 = 167`.

**Example 2:** `nums = [1,5]` → `10`. Burst either balloon first, e.g. burst `1` (neighbors `1` and `5`, both boundary/real): `1*1*5=5`, then burst `5` (neighbors both boundary `1`s): `1*5*1=5`; total `10`.

**Example 3:** `nums = [7]` → `7`. One balloon, bounded by two implicit `1`s: `1*7*1 = 7`.

Constraints: `1 <= nums.length <= 300`, `0 <= nums[i] <= 100`.

## Intuition (explained simply)
The trap here is thinking "which balloon do I burst *first*?" — that couples every choice to every other, since bursting one balloon changes who's adjacent to whom. The trick is to instead think about which balloon you burst **last** within any given range. If balloon `k` is the *last* one burst in the range `(left, right)` (exclusive boundary balloons `left` and `right`, already fixed/never removed within this sub-problem), then when we finally burst it, its neighbors are still exactly `nums[left]` and `nums[right]` (everything strictly between them and it has already been cleared out on both sides). This decouples the range into two independent sub-ranges — `(left, k)` and `(k, right)` — that can be solved separately, which is the hallmark of interval DP.

### 1. Brute Force
- Recurse by trying every balloon as the *next one to burst* in the current (mutated) list, recursing on the resulting shorter list. `burst(balloons) = max over each index i of nums[i-1]*nums[i]*nums[i+1] + burst(balloons without i)`.
- Correct because it tries every possible full ordering of bursts (via every possible "next pick").
- Time complexity: O(n!) in the worst framing (or O(n * 2^n) if memoized crudely on the *set* of remaining balloons — still exponential either way as brute force). Space complexity: O(n) recursion depth (plus O(n) per call to build the reduced list).
- Catastrophically slow — even `n=300` is unthinkable, and even `n=15` is pushing it.

### 2. Better
- Reframe with the "burst last" insight: define `solve(left, right)` = max coins from bursting everything strictly between `left` and `right` (exclusive boundaries, which are never removed within this call). Try every `k` strictly between `left` and `right` as the last burst: `solve(left, right) = max over k of solve(left, k) + solve(k, right) + nums[left]*nums[k]*nums[right]`. Memoize on `(left, right)`.
- Correct because "last burst in a range" always leaves the range's two boundary values intact as `k`'s neighbors, and it exhaustively considers every possible last-burst choice.
- Time complexity: O(n^3) — O(n^2) distinct `(left, right)` pairs, each trying O(n) choices of `k`. Space complexity: O(n^2) for the memo + O(n) recursion stack.
- This is already the right algorithmic idea; the difference to "optimal" here is purely recursive-with-memo vs. clean iterative bottom-up (which avoids recursion overhead/depth limits) — a good example of where "better" and "optimal" share the same asymptotic complexity but differ in implementation robustness.

### 3. Optimal
- Pad `nums` with a `1` on each end: `vals = [1] + nums + [1]`, length `n+2`. Define `dp[left][right]` = the max coins obtainable from bursting **all** balloons strictly between indices `left` and `right` in `vals` (both endpoints are boundary values, never burst within this sub-problem). Base case: `dp[left][right] = 0` whenever `right - left <= 1` (no balloons strictly between them).
- Fill `dp` by increasing **interval length** (`right - left`), so that by the time we compute `dp[left][right]`, every smaller sub-interval `dp[left][k]` and `dp[k][right]` it depends on is already finalized. Transition: `dp[left][right] = max over k in (left, right) of dp[left][k] + dp[k][right] + vals[left]*vals[k]*vals[right]`.
- The answer is `dp[0][n+1]` (the full padded range). This is the same recurrence as "Better," just iterated in explicit length order instead of via recursion — standard for interval DP problems (also seen in matrix chain multiplication, palindrome partitioning min-cuts, etc.).
- Time complexity: O(n^3) — O(n^2) intervals, O(n) split points each. Space complexity: O(n^2) for the `dp` table.
- Edge cases: `n == 1` → answer is just `nums[0]` (bounded by two implicit 1's); all-zero balloons → answer 0; note `nums[i]` can be 0, which is exactly why boundaries must be *values* of 1, not sentinel "no balloon" markers.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n!) | O(n) |
| Better | O(n^3) | O(n^2) |
| Optimal | O(n^3) | O(n^2) |
