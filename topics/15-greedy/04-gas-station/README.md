# 134. Gas Station

**Difficulty:** Medium | **Pattern:** Greedy | **Tags:** Array, Greedy
**LeetCode:** https://leetcode.com/problems/gas-station/

## Problem
There are `n` gas stations arranged in a circle. At station `i`, you can pick up `gas[i]` fuel, and it costs `cost[i]` fuel to travel from station `i` to station `i+1` (wrapping around). Starting with an empty tank, find the index of the gas station you should start from so that you can complete the full circular loop, or return `-1` if it's impossible. It's guaranteed the answer is unique if one exists.

Input: `gas`, `cost` — two lists of integers of the same length.
Output: an integer, the starting index (or `-1`).

**Example 1:** `gas = [1,2,3,4,5], cost = [3,4,5,1,2]` → `3`. Starting at station 3: tank has `4-1=3` after leaving, then `3+5-2=6`, then `6+1-3=4`, then `4+2-4=2`, then `2+3-5=0` — completes the loop with the tank never going negative.

**Example 2:** `gas = [2,3,4], cost = [3,4,3]` → `-1`. Total gas (9) is less than total cost (10), so no starting point can ever complete the circuit.

**Example 3:** `gas = [5,1,2,3,4], cost = [4,4,1,5,1]` → `4`. Starting at station 4: tank has `4-1=3` after leaving, then wrapping to station 0 gives `3+5-4=4`, then `4+1-4=1`, then `1+2-1=2`, then `2+3-5=0` — the tank never dips below zero.

Constraints: `1 <= n <= 10^5`, `0 <= gas[i], cost[i] <= 10^4`.

## Intuition (explained simply)
Two separate facts make this solvable in one pass. First: a valid starting point exists **only if** the total gas across the whole circuit is at least the total cost (`sum(gas) >= sum(cost)`) — otherwise the trip is impossible no matter where you start, since fuel is conserved globally. Second, and more subtle: if you track the *running tank balance* starting from station 0 (even though 0 might not be the right start), the correct starting point is always the station **right after** the point where that running balance hits its lowest value — because everything before that lowest point is "dead weight" that any valid start must skip past.

### 1. Brute Force
- For every candidate starting index `s`, simulate the full loop: start with tank 0, walk all `n` stations starting from `s` (wrapping with modulo), and check if the tank ever goes negative. If it completes without going negative, return `s`.
- Correct because it's a literal exhaustive simulation of every possible starting point.
- Time complexity: O(n^2) — `n` candidate starts, each simulated in O(n). Space complexity: O(1).
- Too slow for `n` up to 100,000 (10 billion operations in the worst case).

### 2. Better
- First check feasibility in O(n): if `sum(gas) < sum(cost)`, no start can ever work — return -1. Otherwise, build an explicit **prefix balance array**: `prefix[i] = sum of (gas[k] - cost[k]) for k in 0..i`, the running tank balance if you (hypothetically) started at station 0. The valid starting station is the one **right after** the index where `prefix` hits its global minimum — find that index with a single scan of the array and return `(argmin_index + 1) % n`.
- Correctness rests on the same prefix-sum fact used in Optimal below: the station following the lowest point of the running balance is where "the least fuel has ever been owed," so starting there guarantees the tank never dips below zero anywhere around the loop (proof detailed in the Optimal section).
- Time complexity: O(n) — one pass to build `prefix`, one pass to find its minimum. Space complexity: O(n) for the explicit prefix array.
- Functionally correct and already linear time, but it materializes an entire array it doesn't need to keep around — the minimum (and the feasibility sum) can both be tracked with running scalars in a single combined pass, which is exactly what Optimal does to cut the space to O(1).

### 3. Optimal
- Do one single combined pass: track `total_tank` (the running sum of `gas[i] - cost[i]` over *all* stations, to check global feasibility) and `current_tank` (the running balance for the current candidate start), plus a `start` index initialized to 0. For each station `i`: add `gas[i] - cost[i]` to both `total_tank` and `current_tank`. If `current_tank` drops below 0, it means station `i` cannot be reached from the current candidate `start` — set `start = i + 1` and reset `current_tank = 0` (this is the same "restart" trick as Better, but computed in the same single sweep as the feasibility check, with no separate second pass).
- **Why the greedy choice is safe:** the argument is a short exchange/prefix-sum proof — if the running balance from `start` first goes negative at station `i`, then for *any* candidate start `s` with `start <= s <= i`, the partial sum from `s` to `i` is even more negative than the partial sum from `start` to `i` was (since we're removing a non-negative prefix contribution), so `s` would fail too. Hence every index up through `i` can be safely eliminated as soon as the deficit is discovered, and jumping straight to `i+1` never skips a valid answer.
- After the single pass, if `total_tank < 0`, no valid start exists — return -1. Otherwise `start` holds the (guaranteed unique) answer.
- Time complexity: O(n) — one linear pass, each index processed once. Space complexity: O(1) — three scalars.
- Edge cases: `n == 1` → valid iff `gas[0] >= cost[0]`; total gas exactly equals total cost → still solvable (the algorithm finds the unique zero-slack start); all gas stations give exactly what the next leg costs → any station technically works, but the problem guarantees uniqueness when feasible, so the algorithm's `start` is still correct.

## Complexity Summary
| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(1) |
| Better | O(n) | O(n) |
| Optimal | O(n) | O(1) |
