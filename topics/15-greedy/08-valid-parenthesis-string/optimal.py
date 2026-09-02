# Greedy: track the reachable [low, high] range of open counts — Time: O(n), Space: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1
                high += 1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.checkValidString("(*)"))
    print("expected True, got", sol.checkValidString("(*))"))
    print("expected False, got", sol.checkValidString("(()"))
