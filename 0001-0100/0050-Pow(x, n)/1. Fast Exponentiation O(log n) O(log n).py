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
# * Since 2^4 = (2 * 2 * 2 * 2), that also means it is equal to (2^2 * 2^2)
# * 2^2 * 2^2 == 2^4, so we can therefore split the work into two
# * Splitting work into two is an application of divide and conquer
# * Instead of computing 2^2 twice, we can simply store the value of 2^2 and multiply it by 2
# * When we divide n by 2, the result could be odd
# *     - To handle this case, we simply multiply the result by whatever `x` is
# *     - For example, 2^3 = (2 * 2 * 2) = (2^2 * 2)
# ! Intuition
# * For an even `n`
# *      x^n = (x^(n/2))^2
# *      Thus, if we already know x^(n/2), squaring it gives us x^n directly
# * For an odd `n`
# *      x^n = (x^n//2)^2 * x
# *      n = 2k + 1, so:
# *         x^n = x^(2k+1) = (x^k)^2 * x
# * For negative exponents (n < 0)
# *      x^(-n) = 1 / x^n
# *      Hence we invert x at the start and work with a positive exponent
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # * n^0 = 1 for all x != 0
        if n == 0:
            return 1

        # * Positive exponents are easier to work with
        if n < 0:
            x = 1 / x  # * Get the reciprocal of `x`
            n = -n  # * Make the exponent positive

        # * The result of x^(n//2)
        half = self.myPow(x, n // 2)

        if n & 1:
            # * 2^3 = (2^2 * 2)
            return half * half * x
        else:
            # * 2^2 = (2^1 * 2^1)
            return half * half


sol: Solution = Solution()
print(sol.myPow(2, 5))
print(sol.myPow(2, 31))
print(sol.myPow(2, 10))
print(sol.myPow(2.1, 3))
print(sol.myPow(2, -2))
print(sol.myPow(3, 4))

# * Time: O(log n) - Fast exponentiation is a logarithmic algorithm with respect to base 2
# * At eaach level of recursion we halve the exponent

# * Space: O(log n) - The depth of the recursion is logarithmic with respect to base 2
