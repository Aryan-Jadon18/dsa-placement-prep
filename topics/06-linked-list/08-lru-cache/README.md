# 146. LRU Cache

**Difficulty:** Medium | **Pattern:** Design (HashMap + Doubly Linked List) | **Tags:** Linked List, Design, Hash Table
**LeetCode:** https://leetcode.com/problems/lru-cache/

## Problem
Design a fixed-capacity cache that supports two operations, both in O(1) average
time: `get(key)` returns the value for `key` if present (or `-1` if not) and marks it
as most recently used; `put(key, value)` inserts or updates the value for `key`,
marking it most recently used, and if this pushes the cache over capacity, evicts the
**least recently used** key first.

**Input:** a sequence of `get(key)` / `put(key, value)` calls on an `LRUCache(capacity)`
**Output:** the return value of each `get` call (`-1` or the cached value)

**Examples**
1. `LRUCache(2)`; `put(1,1)`; `put(2,2)`; `get(1)` → `1` (and `1` is now most
   recently used); `put(3,3)` → evicts key `2` (least recently used); `get(2)` → `-1`.
2. `LRUCache(1)`; `put(1,1)`; `put(2,2)` → evicts key `1` immediately since capacity
   is 1; `get(1)` → `-1`; `get(2)` → `2`.
3. `LRUCache(2)`; `put(1,1)`; `put(1,10)`; `get(1)` → `10`. Updating an existing key's
   value also refreshes its recency, and does not count as a new insertion for
   capacity purposes.

**Constraints:** `1 <= capacity <= 3000`, `0 <= key, value <= 10^4`, at most
`2 * 10^5` calls total.

## Intuition (explained simply)
We need two things simultaneously: fast lookup by key (a hash map's specialty), and a
fast way to know which key was used *longest ago* (an ordering problem). Neither data
structure alone gives both — the combination is what makes this a "design" problem.

### 1. Brute Force
- Use a plain Python dict to store `key -> value`, and a separate list to track usage
  order (most-recently-used at one end). On `get`, look up the value, then find and
  remove the key from the order list and re-append it (an O(n) scan). On `put`,
  similarly update order, and if over capacity, remove the least recently used key
  from both the dict and the front of the order list.
- Correct because both operations do maintain accurate recency ordering, just
  inefficiently.
- Time complexity: O(n) per operation (list search/removal is linear)
  Space complexity: O(capacity)
- Why it's not good enough: the problem explicitly wants O(1) average time per
  operation; a linear scan per `get`/`put` fails that requirement badly at scale
  (up to 2*10^5 calls).

### 2. Better
- Use Python's `collections.OrderedDict`, which maintains insertion order and
  supports `move_to_end` and popping the oldest item, both in O(1) amortized. `get`
  looks up the value and calls `move_to_end(key)`. `put` inserts/updates the key,
  moves it to the end, and if over capacity, calls `popitem(last=False)` to evict the
  oldest entry.
- Time complexity: O(1) amortized per operation  Space complexity: O(capacity)
- This is actually close to optimal in practice (and a perfectly good interview
  answer if you explain the mechanism) — but interviewers often want you to show you
  understand *why* it's O(1) by building the underlying data structure yourself,
  since relying on a built-in can be seen as "using a black box."

### 3. Optimal — HashMap + Custom Doubly Linked List
- Maintain a hash map from `key -> node`, where each node lives in a doubly linked
  list ordered by recency (head = most recently used, tail = least recently used, or
  vice versa — using dummy head/tail sentinels to avoid null checks). `get`: look up
  the node via the hash map (O(1)), unlink it from its current position, and re-insert
  it at the "most recently used" end (O(1), since doubly linked list removal/insertion
  at a known node is O(1)). `put`: if the key exists, update its value and move it to
  the front like `get`; if not, create a new node, insert it at the front, add it to
  the hash map, and if capacity is now exceeded, remove the node at the "least
  recently used" end (also O(1) via sentinel) and delete it from the hash map too.
- Why it works: the hash map gives O(1) node lookup by key; the doubly linked list
  gives O(1) removal/insertion at arbitrary and both-end positions (unlike a singly
  linked list, which needs O(n) to find a node's predecessor). Together, both
  operations are true O(1) worst case, not just amortized.
- Time complexity: O(1) worst case per operation  Space complexity: O(capacity)
- Edge cases: `get`/`put` on a key not present, updating an existing key (must not
  double-count against capacity), capacity of 1, evicting exactly when capacity is
  exceeded (not before).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n) per op | O(capacity) |
| Better | O(1) amortized | O(capacity) |
| Optimal | O(1) worst case | O(capacity) |
