# 43. Multiply Strings

# * We can simulate the multiplication through place value
# *     num = num * 10 + digit
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # * n * 0 = 0
        if num1 == "0" or num2 == "0":
            return "0"

        val1: int = 0
        val2: int = 0

        # * Calculate the place value for num1
        for digit in num1:
            val1 = val1 * 10 + int(digit)

        # * Calculate the place value for num2
        for digit in num2:
            val2 = val2 * 10 + int(digit)

        return str(val1 * val2)


# * Time: O(n + m) - The time taken scales with the input sizes (num1 and num2 respectively)

# * Space: O(n + m) - The size of the output string scales with the sizes of the input strings
# * For example, "100" (length 3) * "100" (length 3) = "100000" (length 6)
