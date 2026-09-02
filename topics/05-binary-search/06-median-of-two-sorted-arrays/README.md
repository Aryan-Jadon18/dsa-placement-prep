# 4. Median of Two Sorted Arrays

**Difficulty:** Hard | **Pattern:** Binary Search — Partition Search | **Tags:** Array, Binary Search, Divide and Conquer
**LeetCode:** https://leetcode.com/problems/median-of-two-sorted-arrays/

## Problem
Given two sorted arrays, find the median of the combined set of all their elements, in `O(log(min(m, n)))` time.

- **Input:** two sorted integer arrays `nums1` and `nums2`.
- **Output:** a float — the median of all elements from both arrays combined (average of the two middle elements if the total count is even, otherwise the single middle element).

**Examples**
1. `nums1 = [1,3], nums2 = [2]` → `2.0`. Merged: `[1,2,3]`, odd count, median is the middle value `2`.
2. `nums1 = [1,2], nums2 = [3,4]` → `2.5`. Merged: `[1,2,3,4]`, even count, median is the average of `2` and `3`.
3. `nums1 = [], nums2 = [1]` → `1.0`. One array is empty; the median of the other array alone.

**Constraints:** `0 <= m, n <= 1000`, `1 <= m + n <= 2000`, `-10^6 <= nums1[i], nums2[i] <= 10^6`, at least one array is non-empty.

## Intuition (explained simply)

### 1. Brute Force
- Merge both sorted arrays into one sorted array (e.g. using the classic merge-two-sorted-lists technique or simply concatenating and sorting), then directly index into the middle to compute the median.
- Correct because the median of the combined set is trivially found once you actually have the fully merged, sorted sequence.
- Time complexity: O((m+n) log(m+n)) if you concatenate and sort, or O(m+n) if you do a proper linear merge.  Space complexity: O(m+n) for the merged array.
- The problem explicitly asks for `O(log(min(m,n)))`, and building the entire merged array is unnecessary work — we only need the one or two middle values, not the whole thing.

### 2. Better
- Do the linear merge conceptually but without storing the full array: walk two pointers through `nums1` and `nums2` simultaneously (classic merge-step), only keeping track of the last one or two values needed for the median, stopping once we've advanced past the middle position(s). This avoids the O(m+n) *space* of the full merge while keeping O(m+n) *time*.
- Correct because it performs the exact same comparisons a full merge would, just discarding elements we no longer need instead of storing them all.
- Time complexity: O(m+n)  Space complexity: O(1)
- Better on space, but still linear in time — the problem's logarithmic requirement means we need to avoid touching *most* of the elements entirely, not just avoid storing them.

### 3. Optimal
- Binary search on the **partition point** of the smaller array. For a candidate partition `i` in `nums1` (splitting it into a left part of size `i` and right part of size `len(nums1) - i`), the corresponding partition `j` in `nums2` is determined by the requirement that the combined left side has exactly `(m+n+1)//2` elements: `j = (m+n+1)//2 - i`. A partition is correct when `nums1[i-1] <= nums2[j]` and `nums2[j-1] <= nums1[i-1's counterpart nums1[i]]` (every left element <= every right element across both arrays). Binary search `i` over `[0, len(nums1)]`: if `nums1[i-1] > nums2[j]`, `i` is too big, move left; if `nums2[j-1] > nums1[i]`, `i` is too small, move right. Once balanced, the median comes directly from the boundary values (`max` of the left parts, and if total is even, also the `min` of the right parts).
- This works because a correct partition guarantees the left combined half contains exactly the smallest `(m+n+1)//2` elements across both arrays without ever merging them — we're binary-searching for *where* that split falls in the smaller array, which pins down where it must fall in the other.
- Time complexity: O(log(min(m, n))) — binary search over the smaller array's index range.  Space complexity: O(1)
- Edge cases: one array is empty (skip binary search on the empty one, median is purely from the other); very unequal sizes (always binary search on the *smaller* array to keep partitions in bounds); use `-infinity`/`+infinity` sentinels when a partition boundary falls at index 0 or the array's end, to avoid out-of-bounds access; careful odd vs. even total-length median formulas.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O((m+n) log(m+n)) | O(m+n) |
| Better | O(m+n) | O(1) |
| Optimal | O(log(min(m, n))) | O(1) |
