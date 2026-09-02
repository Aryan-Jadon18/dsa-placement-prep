# 269. Alien Dictionary

**Difficulty:** Hard | **Pattern:** Advanced Graphs — Topological Sort | **Tags:** Graph, Topological Sort, DFS, BFS
**LeetCode:** https://leetcode.com/problems/alien-dictionary/

> **Note:** This is a LeetCode **Premium/locked** problem, but it's a very standard, frequently-asked interview question (Google and Meta both favor it) — it's the go-to problem for testing topological sort applied to something less obviously graph-shaped than a course schedule.

## Problem
You're given a list of words from an alien language, sorted **lexicographically** according to that language's (unknown) alphabet ordering. Determine a valid ordering of the alphabet's letters consistent with the given word list. If no valid ordering exists (contradictory or invalid input), return an empty string. If multiple valid orderings exist, any one is accepted.

**Input:** a list of strings `words`
**Output:** a string containing each distinct letter exactly once, in a valid alien alphabet order (or `""` if invalid)

**Examples:**
1. `words = ["wrt","wrf","er","ett","rftt"]` → `"wertf"` (or another string consistent with letter order `w < e < r < t < f`). Comparing adjacent words: `"wrt"` vs `"wrf"` first differs at index 2 (`t` vs `f`) → `t` before `f`. `"wrf"` vs `"er"` differs at index 0 (`w` vs `e`) → `w` before `e`. And so on.
2. `words = ["z","x"]` → `"zx"`. Only one letter-order constraint: `z` before `x`.
3. `words = ["abc","ab"]` → `""`. This is **invalid**: a shorter word must come before a longer word that shares its prefix (like normal dictionary order — "ab" should come before "abc", not after), so this ordering is contradictory.

**Constraints:** `1 <= words.length <= 100`, `1 <= words[i].length <= 100`, all lowercase English letters.

## Intuition
Compare each pair of **adjacent** words to extract ordering constraints: the first position where they differ tells us "this letter comes before that letter" in the alien alphabet. Collect all such constraints into a directed graph (letter -> letter it precedes), then a valid overall letter order is just a **topological sort** of that graph. A cycle means contradictory constraints, i.e. no valid order.

### 1. Brute Force
- Build the letter-precedence graph, but do it inefficiently: for **every pair** of words (not just adjacent ones), compare them and extract a "first differing letter" constraint, even though most of those pairs give redundant or unnecessary information (adjacency in a sorted list already implies transitivity through the chain). Also, check the invalid-prefix case (`"abc"` before `"ab"`) for every pair, not just adjacent ones. Then run a DFS-based topological sort with cycle detection.
- Correct — the extra comparisons don't produce *wrong* edges, just redundant ones — but comparing all `O(N^2)` pairs of words, each up to length `L`, is unnecessarily expensive.
- Time complexity: O(N^2 × L + V + E)  Space complexity: O(V + E) for the graph
- All that redundant pairwise comparison work is wasted, since adjacent-word comparisons alone (given the list is already sorted) capture every constraint we need.

### 2. Better
- Build the graph efficiently by comparing only **adjacent** word pairs (`O(N × L)` total), checking the invalid-prefix case only there too. Then run a DFS-based topological sort: 3-color marking, postorder push, detect a cycle by finding a back-edge to a `GRAY` node, and reverse the postorder stack at the end for the final letter order.
- Correct for the same topological-sort reasoning as Course Schedule II, applied to a graph built from just the necessary adjacent-pair constraints.
- Time complexity: O(N × L + V + E)  Space complexity: O(V + E) graph + O(V) recursion stack
- Recursion depth risk for a pathological input with a long dependency chain; also needs the extra postorder-reversal step.

### 3. Optimal
- Same efficient adjacent-pairs graph construction, but topologically sort with **Kahn's algorithm** (BFS, in-degree tracking): seed the queue with all letters that have in-degree `0`, repeatedly pop and append to the result, decrementing dependents' in-degrees and enqueueing any that hit `0`. If the result doesn't include every distinct letter that appeared in the input, there's a cycle — return `""`.
- This works for the same reason Kahn's algorithm works generally, and it directly builds the answer forward with no recursion or reversal — plus, for a problem where the *contradiction* case (cycle) is common in test inputs, Kahn's algorithm makes "did we place every letter" a trivial length check rather than needing a separate explicit cycle flag.
- Time complexity: O(N × L + V + E)  Space complexity: O(V + E) graph + in-degree array + queue
- Edge cases: a single word (no constraints at all — every distinct letter in it, any order among them is valid since there's nothing to compare); the invalid "longer word is a prefix-extension appearing before its own prefix" case (`["abc","ab"]`) must be explicitly checked, since a naive adjacent-comparison loop that finds no differing character at all would silently ignore this contradiction; a cycle in the constraints (return `""`).

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(N^2·L + V+E) | O(V+E) |
| Better | O(N·L + V+E) | O(V+E) |
| Optimal | O(N·L + V+E) | O(V+E) |
