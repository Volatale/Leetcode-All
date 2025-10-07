# 43. Multiply Strings

# * We need to multiply two integers given as strings, but we can't use a BigInt (or anything similar)
# *     - For example, Python's `int` type is actually a BigInt under the hood, so that is disallowed too
# * All we have to do is simulate how long multiplication works
# * The total number of digits in the result is at most `n` + `m`, hence the result array's size
# * Imagine we have two strings `num1` and `num2`
# *     - Based on place value, the ith digit has the value (d * 10^i)
# * If we perform a calculation like (9 * 2), the result is 18
# *     - i = 0, and j = 0
# *     - The result has 2 indices (0 and 1)
# * The 1 in 18 goes into index 0
# * The 8 in 18 goes into index 1
# * So specifically, we are concerned with indices (i + j) and (i + j + 1)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n: int = len(num1)
        m: int = len(num2)

        # * The number of digits in the result is at most (n + m)
        result: list[int] = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # * The carry goes to index (i + j), and the ones are stored at (i + j + 1)
                mul: int = int(num1[i]) * int(num2[j])
                s: int = mul + result[i + j + 1]

                result[i + j + 1] = s % 10  # * The index of the ones (the 8 in 18)
                result[i + j] += s // 10  # * The index of the carry (the 1 in 18)

        return "".join(map(str, result)).lstrip("0") or "0"


sol: Solution = Solution()
print(sol.multiply("81", "2"))  # * "162"
print(sol.multiply("3", "2"))  # * "6"
print(sol.multiply("100", "100"))  # * "10000"
print(sol.multiply("123", "456"))  # * "56088"
print(sol.multiply("5", "0"))  # * "0"
print(sol.multiply("0", "5"))  # * "0"
print(sol.multiply("10", "2"))  # * "20"

# * Time: O(n * m) - THe time taken scales with the length of both input strings
# * For each character in num1, we iterate over num2

# * Space: O(n + m) - The output's size scales with the size of the input strings
