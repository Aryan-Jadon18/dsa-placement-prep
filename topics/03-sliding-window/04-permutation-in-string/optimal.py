# Fixed window, incremental match-count tracking — Time: O(n), Space: O(26)
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        need = Counter(s1)
        window = Counter(s2[:m])
        matches = sum(1 for c in need if need[c] == window[c])

        def bump(char, delta, matches):
            if char not in need:
                return matches
            before = window[char] == need[char]
            window[char] += delta
            after = window[char] == need[char]
            if before and not after:
                matches -= 1
            elif after and not before:
                matches += 1
            return matches

        if matches == len(need):
            return True

        for i in range(m, n):
            add_ch, remove_ch = s2[i], s2[i - m]
            matches = bump(add_ch, 1, matches)
            matches = bump(remove_ch, -1, matches)
            if matches == len(need):
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.checkInclusion("ab", "eidbaooo"))
    print("expected False, got", sol.checkInclusion("ab", "eidboaoo"))
    print("expected True, got", sol.checkInclusion("adc", "dcda"))
