# Partial products + string addition (classic long multiplication) — Time: O(n*m), Space: O(n+m)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def multiply_by_digit(num: str, digit: int) -> str:
            if digit == 0:
                return "0"
            carry = 0
            digits_out = []
            for i in range(len(num) - 1, -1, -1):
                prod = int(num[i]) * digit + carry
                digits_out.append(prod % 10)
                carry = prod // 10
            if carry:
                digits_out.append(carry)
            return "".join(map(str, reversed(digits_out)))

        def add_strings(a: str, b: str) -> str:
            i, j = len(a) - 1, len(b) - 1
            carry = 0
            digits_out = []
            while i >= 0 or j >= 0 or carry:
                d1 = int(a[i]) if i >= 0 else 0
                d2 = int(b[j]) if j >= 0 else 0
                total = d1 + d2 + carry
                digits_out.append(total % 10)
                carry = total // 10
                i -= 1
                j -= 1
            return "".join(map(str, reversed(digits_out)))

        result = "0"
        for idx in range(len(num2) - 1, -1, -1):
            digit = int(num2[idx])
            partial = multiply_by_digit(num1, digit)
            shift = len(num2) - 1 - idx
            partial += "0" * shift
            result = add_strings(result, partial)

        return result


if __name__ == "__main__":
    sol = Solution()
    print("Expected: 6, Got:", sol.multiply("2", "3"))
    print("Expected: 56088, Got:", sol.multiply("123", "456"))
    print("Expected: 0, Got:", sol.multiply("0", "12345"))
