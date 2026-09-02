# 1851. Minimum Interval to Include Each Query

**Difficulty:** Hard | **Pattern:** Intervals + Heap — Offline Sweep with Min-Heap | **Tags:** Array, Heap, Sorting, Intervals
**LeetCode:** https://leetcode.com/problems/minimum-interval-to-include-each-query/

## Problem
You're given a list of intervals `[left, right]` and a list of query points. For each query, find the size (`right - left + 1`) of the **smallest** interval that contains that query point. If no interval contains it, the answer for that query is `-1`.

**Input:** `intervals: List[List[int]]`, `queries: List[int]`.
**Output:** a list of answers, one per query, in the same order the queries were given.

**Example 1:**
`intervals = [[1,4],[2,4],[3,6],[4,4]]`, `queries = [2,3,4,5]` → `[3,3,1,4]`
For query `4`: intervals `[1,4]` (size 4), `[2,4]` (size 3), `[3,6]` (size 4), and `[4,4]` (size 1) all contain 4 — the smallest is `[4,4]` with size 1.

**Example 2:**
`intervals = [[2,3],[2,5],[1,8],[20,25]]`, `queries = [2,19,5,22]` → `[2,-1,4,6]`
Query `19` isn't inside any interval (gap between `[1,8]` and `[20,25]`), so the answer is `-1`.

**Example 3:**
`intervals = [[1,10]]`, `queries = [5]` → `[10]`
Only one interval contains 5, so its size (`10-1+1=10`) is the answer.

**Constraints:** `1 <= intervals.length, queries.length <= 10^5`, `1 <= left <= right <= 10^7`, `1 <= query <= 10^7`.

## Intuition (explained simply)
For a single query, we want the smallest interval among all intervals that contain it. Checking every interval for every query is too slow at this scale, so we process queries in sorted order and only ever look at intervals that could possibly matter — using a min-heap keyed by interval size to instantly grab the smallest *currently valid* interval.

### 1. Brute Force
- For each query, loop over every interval, check if `left <= query <= right`, and keep track of the smallest such interval's size.
- Correct — it directly checks the definition for every query independently.
- Time complexity: O(n · q)  Space complexity: O(1) extra (besides the output)
- Why it's not good enough: with n and q both up to 10⁵, that's up to 10¹⁰ operations — nowhere close to fast enough.

### 2. Better
- Sort intervals by `left`, and sort queries too (remembering each query's original index so we can restore output order at the end). Use a pointer that only ever moves forward through the sorted intervals, adding an interval to an "active" list once its `left <= query`. This avoids rechecking intervals whose start is already known to be too large for the current (and all future, larger) queries. For each query, scan the active list, skip any interval whose `right < query` (expired), and track the minimum size among the rest.
- This cuts out a lot of wasted comparisons (any interval that starts after the query is skipped entirely without inspection) and is correct because sorting both lists means once an interval's start qualifies for a query, it qualifies for every later, larger query too.
- Time complexity: O(n log n + q log q + q·n) worst case (the per-query scan of active intervals is still linear)  Space complexity: O(n)
- Still degrades to brute-force-like behavior when many intervals stay active with a wide range of sizes.

### 3. Optimal
- Sort intervals by `left` and queries by value (keeping original indices). Maintain a **min-heap** of `(size, right)` for all intervals whose `left <= current query`. Process queries in increasing order: first, advance a pointer pushing every interval whose `left <= query` onto the heap; then, pop off the heap any interval whose `right < query` — those are expired and can never help this or any later (larger) query. Whatever remains on top of the heap (if anything) is the smallest interval that both starts early enough and hasn't expired — its size is the answer.
- Why it works: sorting queries means once an interval expires (its `right < query`), it will stay expired forever (queries only grow), so it's safe to permanently discard it from the heap. The heap always gives us the smallest valid interval in O(log n).
- Time complexity: O((n + q) log n) (sorting + heap pushes/pops, each O(log n))  Space complexity: O(n) (heap) + O(q) (output/index mapping)
- Edge cases: a query with no covering interval → `-1`; a query exactly equal to an interval's endpoint (`left == query` or `right == query`) still counts as covered; duplicate queries (answer each independently but they can share heap state); intervals of size 1 (`left == right`).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n·q) | O(1) |
| Better | O(q·n) worst case | O(n) |
| Optimal | O((n+q) log n) | O(n+q) |
