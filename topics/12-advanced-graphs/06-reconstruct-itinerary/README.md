# 332. Reconstruct Itinerary

**Difficulty:** Hard | **Pattern:** Advanced Graphs — Eulerian Path (Hierholzer's Algorithm) | **Tags:** Graph, DFS, Eulerian Path, Backtracking
**LeetCode:** https://leetcode.com/problems/reconstruct-itinerary/

## Problem
You're given a list of airline tickets `tickets[i] = [from, to]`. Reconstruct the itinerary in order, starting from `"JFK"`, that uses **every ticket exactly once**. If multiple valid itineraries exist, return the one that is **lexicographically smallest** when read as a sequence of airport codes. Assume the input always has at least one valid itinerary using every ticket.

**Input:** a list of ticket pairs `[from, to]`
**Output:** a list of airport codes representing the itinerary (using every ticket exactly once, starting at `"JFK"`)

**Examples:**
1. `tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]` → `["JFK","MUC","LHR","SFO","SJC"]`. This is the only way to use every ticket starting from JFK.
2. `tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]` → `["JFK","ATL","JFK","SFO","ATL","SFO"]`. Multiple valid orderings exist (e.g. going to SFO first would also use every ticket), but this one is lexicographically smallest.
3. `tickets = [["JFK","A"],["A","JFK"]]` → `["JFK","A","JFK"]`. A simple round trip using both tickets.

**Constraints:** `1 <= tickets.length <= 300`, all airport codes are 3 uppercase letters, at least one valid itinerary using every ticket exists.

## Intuition
Every ticket is a directed edge; we need a path that uses **every edge exactly once** — that's the definition of an **Eulerian path**. Among all valid Eulerian paths, we want the lexicographically smallest, which we get by always preferring the alphabetically smallest next destination when we have a choice.

### 1. Brute Force
- Pure DFS backtracking over all permutations of ticket usage: at each airport, try flying to *every* unused ticket destination from there (not necessarily smallest-first), recursing until either all tickets are used (success) or we get stuck with unused tickets remaining and no way to leave the current airport (backtrack, undo, try a different ticket). Among all successful full itineraries found, keep the lexicographically smallest.
- Correct — it explores the entire search space — but without any ordering heuristic, it may explore a huge number of dead-end branches before finding (or fully verifying) the best one.
- Time complexity: O(E!) worst case (E tickets, trying them in every order at each branching point)  Space complexity: O(E) recursion depth
- Combinatorial explosion — even 300 tickets could make this hopelessly slow without serious pruning.

### 2. Better
- DFS backtracking, but **sort each airport's destination list alphabetically first** and always try the smallest available destination first. This greedily biases toward the lexicographically smallest itinerary. If a branch gets stuck before using all tickets, backtrack (put the ticket back) and try the next-smallest option.
- This works because trying destinations in sorted order means the *first* complete itinerary we find using every ticket is guaranteed to be the lexicographically smallest one — but we may still need to backtrack out of dead ends (a greedy first choice can lead to a dead end even though a *different* valid Eulerian path exists).
- Time complexity: O(E^2) worst case (backtracking can still revisit the same partial paths multiple times before succeeding, and removing/reinserting from a list at arbitrary positions costs O(E))  Space complexity: O(E) for the adjacency lists + recursion stack
- Backtracking is unnecessary overhead — a smarter algorithm (Hierholzer's) can construct the Eulerian path directly without ever needing to backtrack.

### 3. Optimal
- **Hierholzer's algorithm**: for each airport, keep its destinations in a **min-heap** (always pop the alphabetically smallest available ticket). Do an iterative DFS: repeatedly follow the smallest available ticket from the current airport, pushing airports onto a stack, until we reach an airport with no unused outgoing tickets — then pop it onto the final route. Continue from the new stack top. This produces the route in **reverse**, so reverse it at the end.
- This works because a graph with a valid Eulerian path is guaranteed (by graph theory) to never get "truly stuck" before all edges are used **if you only stop advancing from a node once it's genuinely out of edges** — any node we pop early (dead-ended) must have used all its edges already, so it can safely be placed in the final route; no backtracking is ever needed, since Hierholzer's algorithm's core guarantee is that this "dead-end-first" ordering, reversed, is always a valid Eulerian path.
- Time complexity: O(E log E) (each of the E tickets is pushed/popped from a heap once)  Space complexity: O(E) for the heaps + stack + result
- Edge cases: an airport that's visited multiple times (handled naturally — each visit just consumes a different outgoing ticket); airports with no outgoing tickets left mid-route are exactly where we start popping onto the final path; the guarantee that "an Eulerian path always exists" (given by the problem) means we never need failure-handling for an unsolvable input.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(E!) | O(E) |
| Better | O(E^2) | O(E) |
| Optimal | O(E log E) | O(E) |
