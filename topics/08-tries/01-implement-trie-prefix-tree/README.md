# 208. Implement Trie (Prefix Tree)

**Difficulty:** Medium | **Pattern:** Trie Design | **Tags:** Trie, Design
**LeetCode:** https://leetcode.com/problems/implement-trie-prefix-tree/

## Problem
Design a trie (prefix tree) supporting three operations: `insert(word)` adds a word
to the trie; `search(word)` returns `True` only if the exact word was previously
inserted; `startsWith(prefix)` returns `True` if any inserted word begins with
`prefix`.

**Input:** a sequence of `insert`, `search`, `startsWith` calls
**Output:** `True`/`False` for each `search`/`startsWith` call

**Examples**
1. `insert("apple")`; `search("apple")` → `True`; `search("app")` → `False`
   (`"app"` was never inserted as a complete word); `startsWith("app")` → `True`
   (`"apple"` does start with `"app"`); `insert("app")`; `search("app")` → `True`
   (now it has been inserted).
2. `insert("cat")`; `search("dog")` → `False`; `startsWith("ca")` → `True`.
3. `insert("")`; `search("")` → `True`. Even an empty string can be a valid inserted
   word (the root itself marks end-of-word).

**Constraints:** `1 <= word/prefix length <= 2000`, lowercase English letters only,
up to `3 * 10^4` total calls across all three methods.

## Intuition (explained simply)
A trie is a tree where each edge is labeled with one character, and following a path
from the root spells out a prefix. Many words can share the same prefix path, which
is exactly what makes tries efficient for prefix-based queries: shared prefixes are
stored only once.

### 1. Brute Force
- Just keep a Python `list` (or `set`) of all inserted words. `search` checks exact
  membership; `startsWith` scans the entire collection and checks if any word starts
  with the given prefix using `str.startswith`.
- Correct because both checks are literal definitions of "is this string in the set"
  and "does any string in the set start with this prefix."
- Time complexity: `insert` O(L) to add, `search` O(1) average (set membership),
  `startsWith` O(n * L) where n = number of words (must scan every word)
  Space complexity: O(total characters stored)
- Why it's not good enough: `startsWith` degrades to scanning every single word on
  every call, which is far too slow when there are many words and many prefix
  queries — the trie structure exists specifically to make this fast.

### 2. Better
- Use a hash set of full words for `search` (O(1) average), plus a **separate** hash
  set of every possible prefix of every inserted word (precomputed at insert time:
  for a word of length L, add all L prefixes to the prefix set). Then `startsWith`
  becomes an O(1) average set lookup too.
- Time complexity: `insert` O(L^2) (or O(L) if slicing costs are ignored, but string
  slicing to build each prefix is O(L) so total is O(L^2)), `search` O(1) average,
  `startsWith` O(1) average (with O(L) hashing cost)
  Space complexity: O(n * L^2) in the worst case (all prefixes of all words, without
  sharing) — much worse than a real trie since prefixes aren't deduplicated across
  words efficiently.
- Still suboptimal: wastes a lot of memory storing every prefix as a separate string
  (no structural sharing), and `insert` becomes quadratic in word length.

### 3. Optimal — Actual Trie Structure
- Each trie node holds a dictionary (or fixed-size array of 26) mapping a character
  to a child node, plus a boolean flag `is_end` marking "a word ends here." `insert`
  walks/creates nodes character by character from the root, then marks `is_end=True`
  at the final node. `search` walks the same way and requires both reaching the end
  AND `is_end` being `True`. `startsWith` walks the same way but only requires
  successfully reaching the end of the prefix (regardless of `is_end`).
- Why it works: because nodes are shared across words with common prefixes, the
  structure directly encodes "which prefixes exist" — walking character by character
  either succeeds (prefix exists) or fails as soon as a character isn't a child,
  giving early termination. No word is ever fully rescanned.
- Time complexity: O(L) for all three operations, where L is the length of the word
  or prefix involved (independent of how many words are stored)
  Space complexity: O(total characters across all inserted words) in the worst case,
  but shared prefixes reduce this significantly in practice.
- Edge cases: inserting the empty string, inserting the same word twice, searching
  for a prefix that's also a complete word (must distinguish via `is_end`), prefix
  longer than any stored word.

## Complexity Summary
| Approach | Time (insert / search / startsWith) | Space |
|---|---|---|
| Brute Force | O(L) / O(1) avg / O(n*L) | O(total chars) |
| Better | O(L^2) / O(1) avg / O(1) avg | O(n*L^2) |
| Optimal | O(L) / O(L) / O(L) | O(total chars, shared) |
