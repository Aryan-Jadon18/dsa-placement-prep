# 678. Valid Parenthesis String

**Difficulty:** Medium | **Pattern:** Greedy | **Tags:** String, Greedy, Stack, DP
**LeetCode:** https://leetcode.com/problems/valid-parenthesis-string/

## Problem
Given a string containing only `'('`, `')'`, and `'*'` (a wildcard that can be treated as `'('`, `')'`, or an empty string), determine whether it's possible to interpret every `'*'` in some way so the resulting string is a valid (balanced) parenthesis string.

Input: `s`, a string of `'('`, `')'`, `'*'`.
Output: a boolean.

**Example 1:** `s = "(*)"` → `true`. Treat `*` as empty: `"()"`  is balanced.

**Example 2:** `s = "(*))"` → `true`. Treat the `*` as `'('`: `"(())"` is balanced.

**Example 3:** `s = "(()"` → `false`. There's one unmatched `'('` and no `'*'` available to act as a closing `')'` — no interpretation can balance it.

Constraints: `1 <= s.length <= 100`.

## Intuition (explained simply)
Instead of committing to one specific meaning for each `*` up front, track a **range** of possible "open parenthesis counts" as we scan left to right: `low` = the fewest opens we could have (treating every usable `*` as helpful for closing or as empty), and `high` = the most opens we could have (treating every `*` as an opening paren). At each character, update both bounds; if `high` ever drops below zero, no interpretation can recover (too many closes no matter what), so bail out immediately. At the end, the string is valid if `low` can be brought down to (or started at, and stayed at) exactly zero — meaning some interpretation within the tracked range perfectly balances.

### 1. Brute Force
- Recurse on `(index, open_count)`: at each `*`, branch into three possibilities — treat it as `(` (`open_count+1`), as `)` (`open_count-1`, only if `open_count > 0`), or as empty (`open_count` unchanged) — and recurse. For a literal `(` or `)`, apply the corresponding fixed change (failing immediately if a `)` would take `open_count` negative). Succeed if we reach the end of the string with `open_count == 0`.
- Correct because it tries every possible interpretation of every `*`, which is exactly the problem's definition of validity.
- Time complexity: O(3^k) where `k` is the number of `*` characters (three branches per wildcard). Space complexity: O(n) recursion depth.
- Exponential in the number of wildcards — with up to 100 characters, potentially all `*`, this is infeasible.

### 2. Better
- Memoize the recursion on `(index, open_count)` — note `open_count` is bounded by `n` (can never usefully exceed the number of characters left), so there are at most `O(n^2)` distinct states.
- Correctness is preserved (same recurrence, cached); every state is computed once instead of exponentially many times.
- Time complexity: O(n^2) — `O(n)` positions times `O(n)` possible open-counts, each processed once. Space complexity: O(n^2) for the memo + O(n) recursion stack.
- A full 2D memo table over `(index, open_count)` is more memory and bookkeeping than necessary — the same guarantee can be captured by tracking only the *range* of reachable open-counts at each step, collapsing the whole set of reachable states into two numbers.

### 3. Optimal
- Track two running bounds as we scan left to right: `low` (minimum possible open count) and `high` (maximum possible open count), both starting at 0. For each character: `(` → `low += 1, high += 1`; `)` → `low -= 1, high -= 1`; `*` → `low -= 1` (treat as closer, the most pessimistic option), `high += 1` (treat as opener, the most optimistic option). Clamp `low = max(low, 0)` at every step (a *negative* low just means "some valid interpretation avoids going negative here," not that we're actually stuck — we only ever fail if `high` itself goes negative, since that means *even the most optimistic* interpretation can't avoid an unmatched close).
- **Why the greedy "just track the reachable range" choice is safe:** the crucial fact is that the set of open-counts reachable after processing the first `i` characters, over all valid `*`-interpretations, always forms a *contiguous* range of integers with the same parity pattern — there's no "gap" of unreachable values strictly between `low` and `high`, because a single `*` character can always be locally re-interpreted (open, close, or empty) to shift the count by exactly one step in either direction without affecting anything already fixed. So tracking just the two endpoints faithfully represents the entire reachable set — nothing in between is ever missed or falsely included.
- If `high < 0` at any point, terminate early with `false` (unrecoverable). At the end, the string is valid if `low == 0` is reachable, which holds exactly when `low <= 0 <= high` after the final character (since 0 is always in the interval `[low, high]` whenever that interval is non-empty and low was clamped correctly along the way).
- Time complexity: O(n) — one linear pass. Space complexity: O(1) — two scalars.
- Edge cases: string of all `*` → always valid (each can be empty); more `)` than any interpretation can absorb → `high` goes negative, caught early; leftover unmatched `(` at the end with no `*` to balance → `low > 0` at the end, correctly rejected.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(3^k) | O(n) |
| Better | O(n^2) | O(n^2) |
| Optimal | O(n) | O(1) |
