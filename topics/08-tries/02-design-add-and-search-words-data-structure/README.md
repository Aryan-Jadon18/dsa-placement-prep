# 211. Design Add and Search Words Data Structure

**Difficulty:** Medium | **Pattern:** Trie + DFS | **Tags:** Trie, Design, DFS
**LeetCode:** https://leetcode.com/problems/design-add-and-search-words-data-structure/

## Problem
Design a data structure supporting `addWord(word)` (adds a word) and
`search(word)` (returns `True` if some added word matches, where `word` may contain
`.` as a wildcard matching any single letter).

**Input:** a sequence of `addWord` and `search` calls
**Output:** `True`/`False` for each `search` call

**Examples**
1. `addWord("bad")`; `addWord("dad")`; `addWord("mad")`; `search("pad")` → `False`
   (no added word is `"pad"`); `search("bad")` → `True`; `search(".ad")` → `True`
   (matches `"bad"`, `"dad"`, or `"mad"` — the `.` matches any one letter);
   `search("b..")` → `True` (matches `"bad"`).
2. `addWord("a")`; `search(".")` → `True`. A single `.` matches the single-letter
   word `"a"`.
3. `addWord("ab")`; `search("a")` → `False` (lengths must match exactly — `"a"` is
   shorter than any word starting with `a` except itself, and `"a"` was never added).

**Constraints:** `1 <= word length <= 25`, lowercase letters and `.` only for
`search`, lowercase letters only for `addWord`, at most `2 * 10^5` calls, at most 2
dots per `search` call in most test data (though the algorithm should handle any
number correctly).

## Intuition (explained simply)
This is "Implement Trie" plus one twist: a `.` in the search word means "try every
possible letter here." A trie still narrows things down fast for the fixed letters;
for the `.` positions, we simply have to explore all branches at that point — that's
naturally handled by backtracking/DFS over the trie.

### 1. Brute Force
- Keep a simple list of all added words. For `search`, compare the query against
  every stored word: same length required, and for each position, either the query
  character matches the word's character, or the query character is `.` (matches
  anything).
- Correct because it's the literal definition of "does any added word match this
  pattern."
- Time complexity: `addWord` O(1) amortized (append), `search` O(n * L) where n =
  number of added words, L = word length (must check every word, character by
  character)  Space complexity: O(n * L)
- Why it's not good enough: with up to 2*10^5 calls, comparing against every single
  stored word on every search is too slow — a trie can prune entire branches of
  words instantly whenever a fixed (non-`.`) character doesn't match.

### 2. Better
- Group added words by length into a dict of `length -> list of words` (a small
  optimization over brute force: immediately skip any group whose length doesn't
  match the query length before doing the character-by-character comparison). Still
  fundamentally the same linear comparison per matching-length word.
- Time complexity: `addWord` O(1) amortized, `search` O(n' * L) where n' = number of
  words of the exact matching length (usually smaller than n, but same worst case)
  Space complexity: O(n * L)
- Still suboptimal: still degrades to checking many words individually in the worst
  case (e.g., many same-length words); doesn't share common prefixes at all, unlike
  a trie.

### 3. Optimal — Trie + DFS Backtracking for Wildcards
- Store words in a standard trie (same structure as "Implement Trie"). For `search`,
  do a recursive DFS starting at the root: for each character in the query, if it's
  a normal letter, follow that single child (or fail if it doesn't exist); if it's a
  `.`, recursively try **every** child of the current node (since any letter could
  match), returning `True` if any branch leads to a full match with `is_end = True`
  at the final position.
- Why it works: the trie still gives instant pruning for concrete letters (no need
  to touch words that don't share the prefix so far), and DFS naturally explores
  "all possible letters" only at the specific positions where `.` appears, without
  re-scanning stored words from scratch.
- Time complexity: O(L) for a query with no dots (same as a normal trie search);
  O(26^d * L) worst case where `d` is the number of dots in the query (each dot can
  branch into up to 26 children) — but in practice heavily pruned since most
  branches die out quickly if children don't exist.
  Space complexity: O(total characters across added words, shared) for the trie,
  plus O(L) recursion stack depth per search.
- Edge cases: query entirely made of dots (must try all matching-length words),
  query longer/shorter than any stored word (fails immediately), empty trie.

## Complexity Summary
| Approach | Time (search) | Space |
|---|---|---|
| Brute Force | O(n * L) | O(n * L) |
| Better | O(n' * L) | O(n * L) |
| Optimal | O(L) no dots, O(26^d * L) worst case | O(total chars, shared) |
