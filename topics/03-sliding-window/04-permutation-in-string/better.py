# Fixed window, rebuild frequency counter each slide — Time: O(n * 26), Space: O(26)
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        target = Counter(s1)
        for i in range(n - m + 1):
            window = Counter(s2[i:i + m])
            if window == target:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.checkInclusion("ab", "eidbaooo"))
    print("expected False, got", sol.checkInclusion("ab", "eidboaoo"))
    print("expected True, got", sol.checkInclusion("adc", "dcda"))
