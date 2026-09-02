# Sort every fixed-size window and compare — Time: O(n * m log m), Space: O(m)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        target = sorted(s1)
        for i in range(n - m + 1):
            if sorted(s2[i:i + m]) == target:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.checkInclusion("ab", "eidbaooo"))
    print("expected False, got", sol.checkInclusion("ab", "eidboaoo"))
    print("expected True, got", sol.checkInclusion("adc", "dcda"))
