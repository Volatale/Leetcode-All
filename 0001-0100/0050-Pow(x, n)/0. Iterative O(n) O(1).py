# 50. Pow(x, n)

# * It is a lot easier to work with positive numbers (and exponents)
# *     - Thus, take the absolute value of `n`
# * If the exponent is negative, we can return the reciprocal of the result
# * Exponents are handled via repeated self-multiplication
# *     - 2^3 = (2 * 2 * 2)
# *     - 5^(-5) = 1 / (5 * 5 * 5 * 5 * 5)
# !         - That is, take the reciprocal of the positive result
# *     - n^0 = 1
# *     - 0^n = 0
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or n == 0:
            return 1

        result: float = 1

        for _ in range(abs(n)):
            result *= x

        # * Return the reciprocal of the result if the exponent was negative
        return result if n > 0 else 1 / result


sol: Solution = Solution()
print(sol.myPow(2, 5))
print(sol.myPow(2, 31))
print(sol.myPow(2, 5))

# * Time: O(n) - The number of iterations we do scales with the size of the input `n`

# * Space: O(1) - The memory usage remains constant regardless of input size
