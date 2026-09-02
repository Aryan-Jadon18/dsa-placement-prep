# Plain recursion, try all 3 meanings of each '*' — Time: O(3^k), Space: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        def dfs(i: int, open_count: int) -> bool:
            if open_count < 0:
                return False
            if i == n:
                return open_count == 0
            c = s[i]
            if c == "(":
                return dfs(i + 1, open_count + 1)
            if c == ")":
                return dfs(i + 1, open_count - 1)
            # '*': try as '(', ')', or empty
            return dfs(i + 1, open_count + 1) or dfs(i + 1, open_count - 1) or dfs(i + 1, open_count)

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print("expected True, got", sol.checkValidString("(*)"))
    print("expected True, got", sol.checkValidString("(*))"))
    print("expected False, got", sol.checkValidString("(()"))
