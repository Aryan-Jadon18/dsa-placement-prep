# 743. Network Delay Time

**Difficulty:** Medium | **Pattern:** Advanced Graphs — Dijkstra's Algorithm | **Tags:** Graph, Dijkstra, Heap, Shortest Path
**LeetCode:** https://leetcode.com/problems/network-delay-time/

## Problem
`n` network nodes are labeled `1` to `n`. You're given directed edges `times[i] = [u, v, w]` meaning a signal from `u` to `v` takes `w` time units. A signal is sent from node `k`. Find the minimum time for the signal to reach **all** `n` nodes; return `-1` if some node is unreachable.

**Input:** a list of edges `[u, v, w]`, integers `n` and `k` (the source node)
**Output:** an integer, the time until every node has received the signal (or `-1`)

**Examples:**
1. `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2` → `2`. Node `2` reaches `1` and `3` at time `1`, then `4` (via `3`) at time `2` — the answer is the *maximum* over all shortest distances, since we need everyone to have the signal.
2. `times = [[1,2,1]]`, `n = 2`, `k = 1` → `1`. Node `1` reaches `2` directly at cost `1`.
3. `times = [[1,2,1]]`, `n = 2`, `k = 2` → `-1`. Starting from node `2`, node `1` is unreachable (the edge only goes `1 -> 2`).

**Constraints:** `1 <= k <= n <= 100`, `1 <= times.length <= 6000`, `0 <= w <= 100`, no self-loops, no duplicate edges.

## Intuition
"Minimum time to reach every node from a single source" is exactly single-source shortest paths with non-negative weights — the classic use case for **Dijkstra's algorithm**. The final answer is the *largest* of all the shortest distances (the last node to hear the signal determines when everyone has it).

### 1. Brute Force
- Bellman-Ford: relax every edge (check if `dist[u] + w < dist[v]`, update if so) repeatedly, `n - 1` times over the whole edge list. Since edge weights here are non-negative, Bellman-Ford still gives the correct shortest paths — it just doesn't take advantage of that fact the way Dijkstra does.
- Correct because after `n-1` full rounds of relaxing every edge, all shortest paths (which use at most `n-1` edges each) are guaranteed to have been found — this holds for any graph without negative cycles, non-negative or not.
- Time complexity: O(V × E)  Space complexity: O(V) for the distance array
- Doesn't exploit the non-negative-weight guarantee at all — a lot of wasted relaxation passes compared to a greedy approach.

### 2. Better
- Dijkstra's algorithm without a heap: maintain a `dist[]` array (all infinity except the source at `0`). Repeatedly scan the array to find the closest *unvisited* node (`O(V)` scan), mark it visited, and relax all its outgoing edges. Repeat `V` times.
- Correct — Dijkstra's greedy choice (the closest unvisited node's distance is already final) is valid precisely because weights are non-negative — and it's meaningfully faster than Bellman-Ford by exploiting that.
- Time complexity: O(V^2)  Space complexity: O(V) for the distance array
- The `O(V)` linear scan to find the minimum each round is wasteful when a heap could do it in `O(log V)` — matters a lot for sparse graphs (many nodes, relatively few edges).

### 3. Optimal
- Dijkstra's algorithm with a **min-heap**: push `(distance, node)` pairs, always pop the globally closest unvisited node, relax its edges, and push any improved distances. Skip stale heap entries lazily (a node popped again with a worse recorded distance than already finalized).
- This works for the same greedy correctness reason as above, but the heap makes "find the next closest node" logarithmic instead of linear, which is a big win for sparse graphs (here, up to 6000 edges over up to 100 nodes — solidly sparse relative to the 100^2 possible edges).
- Time complexity: O(E log V)  Space complexity: O(V + E) for the adjacency list + heap
- Edge cases: `n = 1` (the source trivially "reaches" itself at time `0`); a node totally unreachable from `k` → `-1`; multiple edges between the same pair aren't present per constraints, but a self-loop-free graph with a direct zero-weight edge is handled fine (`w >= 0`).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force (Bellman-Ford) | O(V·E) | O(V) |
| Better (array Dijkstra) | O(V^2) | O(V) |
| Optimal (heap Dijkstra) | O(E log V) | O(V+E) |
