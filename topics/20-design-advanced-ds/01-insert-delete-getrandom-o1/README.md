# 380. Insert Delete GetRandom O(1)

**Difficulty:** Medium | **Pattern:** Design — Array + Hash Map Combo | **Tags:** Array, Hash Table, Design
**LeetCode:** https://leetcode.com/problems/insert-delete-getrandom-o1/

## Problem
Design a data structure supporting all of the following in **average O(1)** time:
- `insert(val)`: insert `val` if not already present; return whether it was newly inserted.
- `remove(val)`: remove `val` if present; return whether it was actually removed.
- `getRandom()`: return a random element from the currently stored elements, with every element equally likely.

**Example:**
```
insert(1) -> True     # set is now {1}
remove(2) -> False    # 2 wasn't present
insert(2) -> True     # set is now {1, 2}
getRandom() -> 1 or 2, each with probability 1/2
remove(1) -> True     # set is now {2}
insert(2) -> False    # already present
getRandom() -> 2 (always, only element left)
```

**Constraints:** up to `2*10^5` calls total across all three methods; values fit in a 32-bit signed int.

## Intuition (explained simply)
Each individual requirement is easy alone: a **hash set** gives O(1) insert/remove/contains but can't give O(1) uniformly-random access (you can't index into a hash set). An **array/list** gives O(1) random access by index (`random.choice` needs O(1) indexing) but O(n) removal-by-value (shifting elements). The trick is combining both: keep the values in a list (for O(1) random indexing) *and* a hash map from value → its index in that list (for O(1) lookup), and handle removal cleverly so it doesn't require shifting the whole array.

### 1. Brute Force
- Use a plain Python list. `insert`: check membership with `in` (linear scan) before appending. `remove`: find the value's index with `.index()` (linear scan) and delete it with `.pop(index)`, which also requires shifting every subsequent element left by one. `getRandom`: `random.choice(list)` — this part actually is O(1) already.
- Correct — a list can represent a "collection of unique values" directly if we're careful about duplicates on insert.
- Time complexity: `insert` O(n), `remove` O(n) (search + shift), `getRandom` O(1)  Space complexity: O(n)
- Why it's not good enough: `insert` and `remove` are both linear, failing the O(1) average requirement for large inputs (up to 2×10⁵ calls).

### 2. Better
- Add a hash set alongside the list purely for O(1) membership checks (`insert` no longer needs a linear scan to check "already present"). `remove` still uses `.index()` (linear scan) to find where the value lives in the list, then `.pop(index)` (linear shift) — the hash set speeds up *checking* but doesn't speed up *locating and removing* from the list.
- This fixes `insert`'s complexity (now truly O(1) average, since checking the hash set and appending to the list are both O(1)), but `remove` is still O(n) because we still don't know *where* in the list a value lives without searching.
- Time complexity: `insert` O(1), `remove` O(n), `getRandom` O(1)  Space complexity: O(n)
- `remove` is the remaining bottleneck — solved by tracking each value's exact index, shown next.

### 3. Optimal
- Use a list (for storage + O(1) random indexing) **and** a hash map from `value → its current index in the list`. `insert`: append to the list, record its index in the map. `remove`: instead of removing from the middle of the list (which would require an O(n) shift), **swap the target value with the last element** in the list, update the swapped element's index in the map, then `pop()` the now-last element (O(1)) and delete the removed value from the map. `getRandom`: pick a uniformly random index (`0` to `len-1`) and return `list[index]` — genuinely O(1).
- Why it works: removing an arbitrary element from an *unordered* list doesn't require preserving order — swapping it to the end before popping avoids ever shifting more than one element, and the hash map always tells us exactly where any value currently sits so the swap is O(1) too.
- Time complexity: `insert` O(1), `remove` O(1), `getRandom` O(1), all average-case.  Space complexity: O(n) (list + hash map, both proportional to element count)
- Edge cases: `remove` on the last remaining element (swap-with-self, still correct); `insert` of a duplicate (return `False`, no-op); `remove` of a value never inserted (return `False`); `getRandom` called when the structure has exactly one element.

## Complexity Summary
| Approach | insert | remove | getRandom | Space |
|---|---|---|---|---|
| Brute Force | O(n) | O(n) | O(1) | O(n) |
| Better | O(1) | O(n) | O(1) | O(n) |
| Optimal | O(1) | O(1) | O(1) | O(n) |
