# 261. Graph Valid Tree

**Difficulty:** Medium | **Pattern:** Graphs — Union Find | **Tags:** Graph, Union Find, BFS, DFS
**LeetCode:** https://leetcode.com/problems/graph-valid-tree/

> **Note:** This is a LeetCode **Premium/locked** problem, but it's a very standard interview question — it's the cleanest test of whether you understand what makes a graph a tree.

## Problem
Given `n` nodes labeled `0` to `n-1` and a list of undirected edges, determine whether they form a **valid tree** — meaning the graph is fully connected (every node reachable from every other) *and* contains no cycle.

**Input:** an integer `n`, a list of edges `[u, v]`
**Output:** a boolean — `True` if the edges form a valid tree

**Examples:**
1. `n = 5`, `edges = [[0,1],[0,2],[0,3],[1,4]]` → `True`. Exactly `n-1 = 4` edges, fully connected, no cycle.
2. `n = 5`, `edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]` → `False`. `1-2-3-1` forms a cycle, so it can't be a tree even though everything is connected.
3. `n = 4`, `edges = [[0,1],[2,3]]` → `False`. Only `2` edges for `4` nodes — the graph is disconnected (two separate components), so it can't be a single tree.

**Constraints:** `1 <= n <= 2000`, no self-loops, no duplicate edges.

## Intuition
A graph on `n` nodes is a tree **iff** it has exactly `n-1` edges *and* is fully connected. (Those two facts together automatically rule out cycles — a connected graph with exactly `n-1` edges can't have a cycle, because a cycle would require at least one "extra" edge beyond what's needed to connect everything.) So the edge-count check gives us an instant disqualifier, and then we just need to verify connectivity.

### 1. Brute Force
- First check: if `len(edges) != n - 1`, return `False` immediately (too few edges means disconnected, too many means a cycle). Otherwise, build a full **adjacency matrix**, then DFS from node `0` and count how many nodes get visited — if all `n` are reached, it's connected (and since we already confirmed the edge count, that's enough to conclude it's a tree).
- Correct, but the adjacency matrix wastes `O(n^2)` space and the matrix-scan-per-node DFS wastes time on sparse graphs.
- Time complexity: O(n^2)  Space complexity: O(n^2)
- Way more memory than necessary for what's usually a sparse graph (at most `n-1` edges by the time we even bother checking connectivity).

### 2. Better
- Same edge-count pre-check, but use an **adjacency list** and DFS/BFS with explicit **parent tracking** to detect cycles directly (if we ever see an edge to an already-visited node that *isn't* our immediate parent, that's a cycle) while simultaneously counting reachable nodes for the connectivity check.
- Correct because parent-aware traversal properly distinguishes "revisiting the node we just came from" (expected, undirected edges are stored both ways) from "revisiting some other already-seen node" (a real cycle).
- Time complexity: O(V + E)  Space complexity: O(V + E) for adjacency list + visited set + recursion stack
- Works well and avoids the matrix waste, but doing cycle detection *and* connectivity-counting together via careful parent-tracking is a bit fiddly to get exactly right — Union-Find sidesteps that fiddliness entirely.

### 3. Optimal
- Union-Find (DSU) with path compression and union by rank. Same `n-1` edge-count pre-check. Then process each edge `[u, v]`: if `u` and `v` are *already* in the same set, that edge creates a cycle — return `False` immediately. Otherwise union them. If we get through every edge without finding a cycle (and we already know there are exactly `n-1` edges), the graph must be both cycle-free and fully connected — a valid tree.
- This works because a cycle is detected the instant we try to union two nodes already in the same component — no separate connectivity pass is even needed, since `n-1` cycle-free edges among `n` nodes are *guaranteed* to connect everything (a classic graph theory fact: a forest with `n` nodes and `n-1` edges and no cycles must be a single tree).
- Time complexity: O(n × α(n)) ≈ O(n)  Space complexity: O(n) for parent/rank arrays
- Edge cases: `n = 1` with no edges → `True` (trivially a single-node tree); any self-loop or duplicate edge (not present per constraints, but Union-Find would correctly flag it as a cycle anyway); disconnected graph with the *right* edge count by coincidence (impossible — disconnection with `n-1` total edges forces a cycle somewhere else, which Union-Find still catches).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(n^2) |
| Better | O(V+E) | O(V+E) |
| Optimal | O(n·α(n)) | O(n) |
