# Hash set to remember visited values — Time: O(log n) amortized, Space: O(k)
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(x: int) -> int:
            total = 0
            while x:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1


if __name__ == "__main__":
    sol = Solution()
    print("Expected: True, Got:", sol.isHappy(19))
    print("Expected: False, Got:", sol.isHappy(2))
    print("Expected: True, Got:", sol.isHappy(1))
