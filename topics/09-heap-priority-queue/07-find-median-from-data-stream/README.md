# 295. Find Median from Data Stream

**Difficulty:** Hard | **Pattern:** Two Heaps | **Tags:** Heap, Design
**LeetCode:** https://leetcode.com/problems/find-median-from-data-stream/

## Problem
Design a data structure that supports adding integers one at a time
(`addNum(num)`) and, at any point, returning the median of all numbers added so far
(`findMedian()`). The median is the middle value for an odd count, or the average of
the two middle values for an even count.

**Input:** a sequence of `addNum(val)` and `findMedian()` calls
**Output:** for each `findMedian()`, the current median of all numbers seen so far

**Examples**
1. `addNum(1)`; `addNum(2)`; `findMedian()` → `1.5` (average of 1 and 2);
   `addNum(3)`; `findMedian()` → `2` (middle of 1, 2, 3).
2. `addNum(-1)`; `findMedian()` → `-1`. Single element, median is itself.
3. `addNum(5)`; `addNum(2)`; `addNum(8)`; `addNum(1)`; `findMedian()` → `3.5`.
   Sorted so far: 1, 2, 5, 8 → average of the two middle values (2 and 5) is 3.5.

**Constraints:** `-10^5 <= num <= 10^5`, at most `5 * 10^4` calls to `addNum`,
`findMedian` is only called when at least one number has been added.

## Intuition (explained simply)
Finding a median needs to know "what's in the middle," which normally requires
knowing the full sorted order. The clever trick is to split the numbers into two
halves — a "low half" (at most the median) and a "high half" (at least the
median) — and keep each half in a heap so we always have instant access to their
boundary values (the largest of the low half, and the smallest of the high half),
which are exactly what's needed to compute the median.

### 1. Brute Force
- Keep a plain Python list of all numbers seen so far. On `addNum`, just append.
  On `findMedian`, sort the entire list and pick the middle element(s).
- Correct because sorting always gives the true order, and picking the middle
  index(es) is the direct definition of the median.
- Time complexity: `addNum` O(1), `findMedian` O(n log n) (sorts the whole list
  every time it's called) Space complexity: O(n)
- Why it's not good enough: if `findMedian` is called frequently (interleaved with
  many `addNum` calls), repeatedly sorting the entire growing list from scratch is
  extremely wasteful.

### 2. Better
- Keep the list always sorted using `bisect.insort` on `addNum` (binary search for
  the correct position, then insert) instead of appending and re-sorting.
  `findMedian` becomes an O(1) lookup of the middle index(es) since the list is
  already sorted.
- Time complexity: `addNum` O(n) (binary search is O(log n), but insertion into a
  Python list requires shifting elements, which is O(n)), `findMedian` O(1)
  Space complexity: O(n)
- Still suboptimal: `addNum` is O(n) per call due to the list-shifting cost of
  insertion, which becomes expensive with many additions (up to 5*10^4 calls); the
  optimal two-heap approach gets `addNum` down to O(log n).

### 3. Optimal — Two Heaps (Max-Heap + Min-Heap)
- Maintain two heaps: a max-heap `low` holding the smaller half of the numbers
  (via negation, since `heapq` is min-heap only), and a min-heap `high` holding the
  larger half. Keep them balanced so their sizes differ by at most 1. On `addNum`:
  push the new number into `low`, then move `low`'s max into `high` to maintain the
  ordering invariant (everything in `low` <= everything in `high`); if `high` then
  has more elements than `low`, move `high`'s min back into `low` to rebalance. On
  `findMedian`: if the heaps are equal size, the median is the average of `low`'s
  max and `high`'s min; if `low` has one more element (we always let the odd one
  out land in `low`), the median is simply `low`'s max.
- Why it works: the two heaps act as a "hinge" around the median — `low`'s root is
  always the largest of the smaller half, and `high`'s root is always the smallest
  of the larger half, and by construction those two values straddle the true
  median exactly. Balancing sizes after every insertion keeps this invariant valid
  at all times, in O(log n) per insertion instead of O(n).
- Time complexity: `addNum` O(log n), `findMedian` O(1)  Space complexity: O(n)
- Edge cases: a single number added (median is that number), an odd vs. even total
  count (different formula), duplicate numbers, negative numbers.

## Complexity Summary
| Approach | Time (addNum / findMedian) | Space |
|---|---|---|
| Brute Force | O(1) / O(n log n) | O(n) |
| Better | O(n) / O(1) | O(n) |
| Optimal | O(log n) / O(1) | O(n) |
