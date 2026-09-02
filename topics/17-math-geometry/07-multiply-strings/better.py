# Accumulate all digit products into an array, one final carry-cleanup pass — Time: O(n*m), Space: O(n+m)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                result[i + j + 1] += int(num1[i]) * int(num2[j])

        carry = 0
        for k in range(n + m - 1, -1, -1):
            total = result[k] + carry
            result[k] = total % 10
            carry = total // 10

        digits = "".join(map(str, result)).lstrip("0")
        return digits if digits else "0"


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 6, Got:", sol.multiply("2", "3"))
    print("Expected: 56088, Got:", sol.multiply("123", "456"))
    print("Expected: 0, Got:", sol.multiply("0", "12345"))
