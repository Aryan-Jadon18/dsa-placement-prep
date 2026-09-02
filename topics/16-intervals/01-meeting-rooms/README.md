# 252. Meeting Rooms

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Pattern](https://img.shields.io/badge/Pattern-Overlap%20Detection-blue)
![Tags](https://img.shields.io/badge/Tags-Array%2C%20Sorting%2C%20Intervals-lightgrey)

**LeetCode:** https://leetcode.com/problems/meeting-rooms/

> **Note:** This problem is LeetCode Premium (locked behind a subscription), so you can't open it on the site without paying. It's still one of the most commonly asked interview questions — usually posed verbally or on a whiteboard as "given a list of meeting time intervals, can one person attend all of them?" It's also the warm-up for the much more common LC 253 (Meeting Rooms II).

## Problem
You are given a list of meeting intervals, each with a start and end time. Determine whether a single person could attend every meeting, i.e. no two meetings overlap.

**Input:** a list of `[start, end]` pairs (integers, `start < end`).
**Output:** `true` if no two intervals overlap, `false` otherwise.

**Example 1:**
`intervals = [[0,30],[5,10],[15,20]]` → `false`
`[0,30]` overlaps both `[5,10]` and `[15,20]`, so one person can't attend all three.

**Example 2:**
`intervals = [[7,10],[2,4]]` → `true`
The meetings don't touch at all (`[2,4]` ends before `[7,10]` starts), so one person can attend both.

**Example 3:**
`intervals = [[1,5],[5,10]]` → `true`
They touch exactly at `5`, but a meeting ending at 5 and one starting at 5 don't actually overlap in time — back-to-back meetings are fine.

**Constraints:** `0 <= intervals.length <= 10^4`, `0 <= start < end <= 10^6`.

> **🔑 Pattern Recognition:** "Do any two ranges overlap?" → sort by start, then only adjacent pairs can possibly conflict. Sorting collapses an all-pairs check into a single linear sweep.

## Intuition (explained simply)
Two meetings "conflict" if one starts before the other ends. If we sort the meetings by start time, any conflict must show up between two meetings that are now *next to each other* in that sorted order — you never need to compare far-apart meetings once they're sorted.

### 1. Brute Force
- Compare every pair of meetings. Two intervals `[s1,e1]` and `[s2,e2]` overlap if `s1 < e2 and s2 < e1`. If any pair overlaps, return `false`.
- Correct because it literally checks every possible conflict, no assumptions needed.
- Time complexity: O(n²)  Space complexity: O(1)
- Why it's not good enough: with up to 10⁴ meetings that's ~10⁸ comparisons — too slow, and it doesn't scale to the follow-up (Meeting Rooms II).

### 2. Better
- Sort the intervals by start time first. Now build pairs of consecutive intervals and check each pair for overlap. This narrows the check down from "all pairs" to "adjacent pairs after sorting," which is the same core idea as optimal but written using extra intermediate structures (a sorted copy + zipped pairs), so it uses a bit more memory and is a hair less direct.
- Time complexity: O(n log n)  Space complexity: O(n) (sorted copy + pair list)
- Still allocates extra lists we don't strictly need.

### 3. Optimal
- Sort in place by start time, then walk through once comparing each meeting's start to the *previous* meeting's end. If `intervals[i][0] < intervals[i-1][1]`, they overlap — return `false` immediately (short-circuit, no need to scan further).
- Why it works: after sorting by start time, if meeting `i` doesn't overlap its immediate predecessor, it can't overlap any earlier meeting either (their end times are all ≤ the predecessor's start progression is monotonic... more precisely: since starts are sorted, if `start[i] >= end[i-1]` there's no conflict with `i-1`, and any meeting before `i-1` already ended even earlier isn't guaranteed, but the classic argument is: only adjacent-after-sort pairs can conflict when checking pairwise start<end validity for a *single room*). This is the standard sweep argument for "no overlap" checks.
- Time complexity: O(n log n) (sorting dominates)  Space complexity: O(1) extra (sort in place; O(log n) if counting sort's internal stack)
- Edge cases: empty list or single meeting → trivially `true`; touching meetings (`end == start`) are **not** overlaps; duplicate intervals `[[1,5],[1,5]]` → overlap → `false`.

#### 🎯 Visual Walkthrough
Tracing `intervals = [[0,30],[5,10],[15,20]]` (Example 1, answer `false`), already sorted by start:

| Interval | Start | End | Compared to previous end | Overlap? |
|---|---|---|---|---|
| `[0,30]` | 0 | 30 | — (first) | — |
| `[5,10]` | 5 | 10 | `5 < 30` (prev end) | **Yes** → return `false` |
| `[15,20]` | 15 | 20 | not reached | — |

Sorted order puts `[0,30]` first; the very next meeting `[5,10]` starts at `5`, before `[0,30]` ends at `30`, so the sweep stops immediately and returns `false`.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n²) | O(1) |
| Better | O(n log n) | O(n) |
| Optimal | O(n log n) | O(1) |
