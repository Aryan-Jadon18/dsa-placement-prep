# Floyd's cycle detection (slow/fast pointers) — Time: O(log n), Space: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(x: int) -> int:
            total = 0
            while x:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total

        slow = n
        fast = sum_of_squares(n)
        while fast != 1 and slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))

        return fast == 1


if __name__ == "__main__":
    sol = Solution()
    print("Expected: True, Got:", sol.isHappy(19))
    print("Expected: False, Got:", sol.isHappy(2))
    print("Expected: True, Got:", sol.isHappy(1))
