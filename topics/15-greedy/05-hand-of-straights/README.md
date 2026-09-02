# 846. Hand of Straights

**Difficulty:** Medium | **Pattern:** Greedy + HashMap | **Tags:** Array, Greedy, Hash Table, Sorting
**LeetCode:** https://leetcode.com/problems/hand-of-straights/

## Problem
Given a hand of cards (integers, duplicates allowed) and a group size `groupSize`, determine whether the hand can be split entirely into groups of exactly `groupSize` cards, where each group consists of `groupSize` **consecutive** values (e.g. `[3,4,5]`).

Input: `hand`, a list of integers; `groupSize`, an integer.
Output: a boolean.

**Example 1:** `hand = [1,2,3,6,2,3,4,7,8], groupSize = 3` → `true`. Split into `[1,2,3]`, `[2,3,4]`, `[6,7,8]`.

**Example 2:** `hand = [1,2,3,4,5], groupSize = 4` → `false`. `5` cards can't split evenly into groups of 4.

**Example 3:** `hand = [1,2,2,3,3,4], groupSize = 2` → `true`. Split into `[1,2]`, `[2,3]`, `[3,4]` — each pair of consecutive values, and every card used exactly once.

Constraints: `1 <= hand.length <= 10^4`, `0 <= hand[i] <= 10^9`, `1 <= groupSize <= hand.length`.

## Intuition (explained simply)
Since every group must be a run of `groupSize` consecutive values, the **smallest remaining card** in the hand has no choice about which group it belongs to — it *must* be the starting (lowest) card of whatever group it's in, because there's nothing smaller left to pair it with a group that starts even lower. So the natural strategy is: always look at the smallest remaining value, greedily form a group starting exactly there (`x, x+1, ..., x+groupSize-1`), remove one copy of each, and repeat. A hash map of value → remaining count, plus always processing in ascending order, makes this efficient.

### 1. Brute Force
- Recursively/backtrack: repeatedly pick *any* remaining card as a potential group start, try to consume `groupSize` consecutive values from it, remove them, and recurse on what's left; if a branch gets stuck, backtrack and try a different starting card. Succeed if all cards are eventually consumed.
- Correct because it explores every possible way of forming groups, not just starting from the smallest value.
- Time complexity: exponential, roughly O((n/groupSize)!) in the worst case — many different orders of picking group-starts to try. Space complexity: O(n) recursion depth / working copy of the hand.
- Combinatorially infeasible for `n` up to 10,000; way more exploration than necessary once we realize the smallest card's group is forced.

### 2. Better
- Use a `Counter` for card counts, and repeatedly find the current minimum remaining value (e.g. by scanning the counter's keys, or maintaining a sorted structure), then peel off one group starting there, decrementing counts by 1 for each of `groupSize` consecutive values (fail immediately if any needed value is missing). Repeat until all counts are exhausted or a group can't be formed.
- Correctness follows from the same "smallest card is forced" argument, just without pre-sorting the underlying multiset up front — recomputing the minimum on the fly.
- Time complexity: O(n * log n) if using a min-heap of distinct values to fetch the minimum each time (or O(n * D) with D distinct values if scanning naively) — a heap gives roughly O(n log D). Space complexity: O(n) for the counts (and heap).
- Repeatedly searching for the "current minimum" (whether via heap operations or rescanning) adds overhead that a single upfront sort avoids entirely, since the set of distinct values we'll ever need to start a group from is fixed once we sort.

### 3. Optimal
- Sort the **distinct** values once. Build a `Counter` of card counts. Walk the sorted distinct values in ascending order; whenever a value still has remaining count `> 0`, it must start a new group (nothing smaller is left to explain its presence) — consume `count` copies of a full run starting there: for `offset` in `0..groupSize-1`, decrement `counts[value + offset]` by that same amount, failing immediately if any of those needed values doesn't have enough count.
- **Why the greedy choice is safe:** the smallest remaining card can only ever be the *start* of a group (there is no smaller card to be its predecessor in a consecutive run), so committing to start a group there is forced, not just convenient — no alternative strategy could ever do better, since delaying it or using it as a non-starting member of some other group is simply impossible.
- Time complexity: O(n log n) — dominated by sorting the distinct values (or O(n log D) sorting only the `D` distinct values). Space complexity: O(n) for the counts.
- Edge cases: `groupSize == 1` → always `true` (every card is its own group); `len(hand) % groupSize != 0` → immediately `false`, checked upfront to avoid unnecessary work; duplicate values are exactly what the count-based consumption handles correctly (consuming `count` copies of an entire run at once rather than one card at a time).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O((n/groupSize)!) | O(n) |
| Better | O(n log n) | O(n) |
| Optimal | O(n log n) | O(n) |
