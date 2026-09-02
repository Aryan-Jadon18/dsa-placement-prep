# 39. Combination Sum

**Difficulty:** Medium | **Pattern:** Backtracking | **Tags:** Array, Backtracking
**LeetCode:** https://leetcode.com/problems/combination-sum/

## Problem
Given an array of distinct positive integers `candidates` and a target integer,
return every unique combination of numbers from `candidates` that sums exactly to
`target`. The same number may be reused an unlimited number of times. Combinations
that use the same numbers in a different order count as one combination (no
duplicates).

**Input:** array of distinct positive integers, integer `target`
**Output:** a list of combinations (each a list of integers) summing to `target`

**Examples**
1. Input: `candidates = [2,3,6,7]`, `target = 7` → Output: `[[2,2,3],[7]]`. `2+2+3=7`
   (reusing `2` twice) and `7` alone both work.
2. Input: `candidates = [2,3,5]`, `target = 8` → Output:
   `[[2,2,2,2],[2,3,3],[3,5]]`.
3. Input: `candidates = [2]`, `target = 1` → Output: `[]`. No combination of `2`s can
   ever sum to `1`.

**Constraints:** `1 <= candidates.length <= 30`, all values distinct,
`2 <= candidates[i] <= 40`, `1 <= target <= 40`.

## Intuition (explained simply)
At each step you decide "do I use this candidate again, or move on to the next
one?" Because reuse is allowed, when you pick a candidate you stay at the *same*
index for the next choice (so it can be picked again); when you decide to skip it,
you move forward and never revisit it. This naturally avoids generating the same
combination in different orders.

### 1. Brute Force
- Generate every possible sequence of picks (allowing repeats, without the "only
  move forward" restriction), tracking a running sum, and whenever the sum equals
  `target`, sort the sequence and add it to a result set (using a set to filter out
  duplicate combinations that arose from different orderings), stopping any branch
  once the sum exceeds `target`.
- Time complexity: exponential, worse than necessary because many branches produce
  the exact same multiset of numbers in different orders, all of which get
  generated and then discarded via the dedup step  Space complexity: also
  exponential, temporarily holding many duplicate sequences before filtering
- Why it's not good enough: doing the ordering restriction *after the fact* (via a
  set) instead of *during generation* wastes enormous amounts of work generating
  and comparing sequences that are ultimately thrown away as duplicates.

### 2. Better
- Backtracking with a "non-decreasing index" rule (the standard fix): at each step,
  only consider candidates at index `>= start`, and when picking `candidates[i]`,
  recurse with `start = i` (not `i + 1`) so the same number can be reused, but never
  look backward — this eliminates duplicate combinations by construction, without
  needing a dedup step. Prune (return early) once the running sum exceeds `target`.
- Time complexity: O(2^target) in the worst case (each unit of target can be reached
  many ways with small candidates) — exponential but with no wasted duplicate work
  Space complexity: O(target / min(candidates)) recursion depth, plus output size
- What's still suboptimal: without sorting `candidates` first, pruning happens later
  than it could — larger candidates get tried before smaller ones, so a branch that
  is already hopeless (sum will only grow) isn't cut off as early as possible.

### 3. Optimal
- Same backtracking shape, but **sort `candidates` first**. This lets you `break`
  out of the loop the instant `candidates[i] > target - current_sum` (since
  everything after it in the sorted order is even bigger and equally hopeless),
  instead of merely `continue`-ing past one bad candidate at a time.
- This works because after sorting, all candidates from index `i` onward are `>=
  candidates[i]`; the moment one candidate can't fit, none of the remaining ones can
  either, so a `break` safely skips checking them at all.
- Time complexity: same worst-case exponential bound as Better, but with
  meaningfully fewer explored nodes in practice due to earlier pruning  Space
  complexity: O(target / min(candidates)) recursion depth, plus output size
- Edge cases: `target` smaller than every candidate → returns `[]` immediately after
  the first pruned branch; a candidate exactly equal to `target` → a valid
  single-element combination.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | exponential + dedup overhead | exponential |
| Better | O(2^target) | O(target/min) + output |
| Optimal | O(2^target), fewer nodes visited | O(target/min) + output |
