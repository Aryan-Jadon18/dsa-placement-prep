# Polynomial rolling hash for O(1) prefix/suffix comparisons — Time: O(n) average, Space: O(n)
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        BASE = 131
        MOD = 2_147_483_647

        # prefix_hash[i] = hash of s[0:i], power[i] = BASE^i mod MOD
        prefix_hash = [0] * (n + 1)
        power = [1] * (n + 1)
        for i in range(n):
            prefix_hash[i + 1] = (prefix_hash[i] * BASE + ord(s[i])) % MOD
            power[i + 1] = (power[i] * BASE) % MOD

        # suffix_hash[i] = hash of s[i:n], built back-to-front
        suffix_hash = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_hash[i] = (suffix_hash[i + 1] + ord(s[i]) * power[n - 1 - i]) % MOD

        def prefix_of_length(length: int) -> int:
            return prefix_hash[length]

        def suffix_of_length(length: int) -> int:
            return suffix_hash[n - length]

        for length in range(n - 1, 0, -1):
            if prefix_of_length(length) == suffix_of_length(length) and s[:length] == s[n - length:]:
                return s[:length]
        return ""


if __name__ == "__main__":
    sol = Solution()
    print("Expected: l, Got:", sol.longestPrefix("level"))
    print("Expected: abab, Got:", sol.longestPrefix("ababab"))
    print("Expected: leet, Got:", sol.longestPrefix("leetcodeleet"))
