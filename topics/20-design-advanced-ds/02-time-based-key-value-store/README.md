# 981. Time Based Key-Value Store

**Difficulty:** Medium | **Pattern:** Design + Binary Search | **Tags:** Design, Hash Table, Binary Search
**LeetCode:** https://leetcode.com/problems/time-based-key-value-store/

## Problem
Design a key-value store where every value is stored **with a timestamp**, and multiple values can be stored for the same key at different (strictly increasing) timestamps. Support:
- `set(key, value, timestamp)`: store `value` for `key` at the given `timestamp` (timestamps for a given key are guaranteed to be called in strictly increasing order).
- `get(key, timestamp)`: return the value that was set for `key` at the **largest timestamp `<=` the given timestamp**. If no such value exists, return `""`.

**Example:**
```
set("foo", "bar", 1)
get("foo", 1)  -> "bar"            # exact timestamp match
get("foo", 3)  -> "bar"            # no value set at 3, most recent <=3 is timestamp 1
set("foo", "bar2", 4)
get("foo", 4)  -> "bar2"           # exact match at 4
get("foo", 5)  -> "bar2"           # most recent <=5 is timestamp 4
get("foo", 0)  -> ""               # nothing set at or before timestamp 0
```

**Constraints:** up to `2*10^5` calls total, `1 <= timestamp <= 10^7`, timestamps for each key strictly increasing across `set` calls.

## Intuition (explained simply)
Since `set` calls for a given key always arrive with strictly increasing timestamps, the list of `(timestamp, value)` pairs stored for any key is **already sorted by timestamp** just from the order we append them. That means answering "largest timestamp `<=` query" is a textbook binary search problem — we don't need to search linearly through history.

### 1. Brute Force
- Store everything as one big list of `(key, value, timestamp)` tuples. For `get(key, timestamp)`, scan the *entire* list, filter down to entries matching `key` with `stored_timestamp <= timestamp`, and take the one with the maximum such timestamp.
- Correct because it directly checks the definition against every stored entry.
- Time complexity: `set` O(1), `get` O(n) where n = total number of `set` calls ever made (across all keys)  Space complexity: O(n)
- Why it's not good enough: `get` rescans irrelevant entries for *other* keys every single time — wasteful, and with up to 2×10⁵ calls this adds up badly.

### 2. Better
- Group entries by key: a hash map from `key → list of (timestamp, value)` pairs (appended in arrival order, so implicitly sorted since timestamps only increase per key). For `get(key, timestamp)`, **linearly scan** that key's list from the end backward (or front forward) until finding the largest timestamp `<= timestamp`.
- This avoids wasting time on other keys' entries (a real improvement), but still scans linearly within one key's history instead of exploiting that the list is sorted.
- Time complexity: `set` O(1), `get` O(k) where k = number of `set` calls for that specific key (worst case still O(n) if all calls target one key)  Space complexity: O(n)
- Doesn't yet use binary search, even though the per-key list is sorted and binary-search-ready.

### 3. Optimal
- Same per-key grouping (hash map from `key → list of (timestamp, value)`, sorted by construction), but use **binary search** (`bisect_right` on the list of timestamps, or a custom binary search comparing tuples) to find, in O(log k), the rightmost timestamp that is `<=` the query timestamp. If the binary search lands before index 0 (no valid timestamp), return `""`; otherwise return the value at that index.
- Why it works: because timestamps for a key are strictly increasing (guaranteed by the problem), the stored list is always sorted, so binary search correctly and efficiently finds the "largest value `<=` target" (this is exactly what `bisect_right` followed by stepping back one index computes).
- Time complexity: `set` O(1), `get` O(log k) (k = number of entries for that key)  Space complexity: O(n)
- Edge cases: `get` called before any `set` for that key → `""`; `get` with timestamp smaller than the first `set` for that key → `""`; `get` with timestamp larger than the last `set` → returns the most recent value; querying a key that was never set at all.

## Complexity Summary
| Approach | set | get | Space |
|---|---|---|---|
| Brute Force | O(1) | O(n) | O(n) |
| Better | O(1) | O(k) | O(n) |
| Optimal | O(1) | O(log k) | O(n) |
