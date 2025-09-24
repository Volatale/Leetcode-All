# 29. Divide Two Integers

# * The goal is to return the result of an integer division between two numbers
# ! We are not allowed to use multiplication, division or the modulo operator (%)
# * The easiest way to handle this is by using repeated subtraction, but this doesn't work for negatives
# * Therefore, we should take the absolute values of both inputs and simply handle the signage later
# * The number of subtractions we manage to perform is the return value (no. of subtractions = quotient)
# ! Since we aren't able to use regular arithmetic operations (*, /, %), we can resort to bit manipulation
# *     - n << i = n * (2^i)
# *     - n >> i = n / (2^i)
# * So essentially we repeatedly subtract from n multiples of 2^i
# * Then, the number of multiples we subtract is the "quotient" that we can add to our total
# * Finally, we subtract the value of the n multiples of 2^i from dividend
# *     - Dividend's new value is the amount we have leftover
# * We repeat this process while divident >= divisor

# * As for the result:
# *     - It should be truncated toward 0 (-2.892 becomes -2, and 892.1132 becomes 892)
# *     - If the result < -2^31, return -2^31
# *     - If the result > 2^31 - 1, return 2^31 - 1
# ! Edge cases:
# *     - (-2**31 = -2147483648), and (2**31 - 1 == 2147483647)
# !     - (-a / -b) results in a POSITIVE, thus (INT_MIN / -1) will OVERFLOW
# *         -  The result is 2147483648, which is > INT_MAX
# * Division Rules:
# *     - (a / b) = Positive
# *     - (-a / b) = Negative
# *     - (a / -b) = Negative
# *     - (-a / -b) = Positive
# ! We only get a negative if ONE of the two inputs is negative
# *     - Thus, we an handle this relationship using XOR (0 = Positive, 1 = Negative)
# *     - (0 ^ 0 = 0), (1 ^ 1 = 1), (0 ^ 1 = 1), (1 ^ 0 = 1)

# ! Intuition:
# * Lets say we have 58 / 5
# *     - A = (Q * D) + R
# *     - 58 = (11 * 5) + 3
# * In decimal form, we write 11 (Q) as "11"
# * In binary form, we write it (Q) as "1011"
# *     - 11 = (2^3 + 2^1 + 2^0)
# *     - 55 = (2^3 + 2^1 + 2^0) * 5
# *     - 55 = ((2^3 * 5) + (2^1 * 5) + (2^0 * 5))
# * We know the divisor itself is 5, and we can't divide or multiply (or use modulo)
# * We also know we have to subtract, so we can use bit manipulation to perform the multiplications instead
# ! Every left shift is a multiplication by 2
# *     - 5 << 0 = (5)
# *     - 5 << 1 = 5 * 2 = (10)
# *     - 5 << 2 = 5 * 2 * 2 = (20)
# *     - 5 << 3 = 5 * 2 * 2 * 2 = (40)
# *     - 5 << 4 = 5 * 2 * 2 * 2 * 2 = (80)
# * The dividend is 58, which is SMALLER than 80, so we can't use (5 * 2^4)
# *     - Thus, we try a smaller subtraction
# *     - (5 * 2^3) <= 58, so we CAN subtract 40 from 58
# * Now we are left with 18
# *     - (5 * 2^2) > 18, so we can't subtract 20 from 18
# *         - Try a smaller subtraction
# *     - (5 * 2^1) <= 18, so we can subtract 10 from 18
# * Now we have 8 left
# *       ...(skipping redundant computations)
# *     - (5 * 2^0) <= 8, so we can subtract 5 from 8
# ! The subtractions we were able to perform used the following powers of 2:
# *     - 2^3, 2^1, 2^0.
# *         - The sum of the above powers is 11, which we already knew
# *     - 58 - 55 = 3 (remainder)
# ! In other words, the quotient is equal to the sum of the powers of two that were subtracted from dividend (A)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -(2**31)

        # * (-2**31 / -1) > INT_MAX (so we get an overflow)
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # * (N / P = N), (P / N = N), (P / P = P), (N / N = P)
        negative: bool = (dividend < 0) ^ (divisor < 0)
        quotient: int = 0

        # * It is easier to work with positive values than negative
        dividend, divisor = abs(dividend), abs(divisor)

        # * Subtract as many times as we can
        while dividend >= divisor:
            value, count = divisor, 1

            # * Find the largest multiple we can subtract
            while dividend >= (value << 1):
                value <<= 1
                count <<= 1

            # * Subtract the largest multiple
            dividend -= value
            quotient += count

        if negative:
            quotient = -quotient

        if quotient < INT_MIN:
            return INT_MIN
        elif quotient > INT_MAX:
            return INT_MAX
        else:
            return quotient


sol: Solution = Solution()
print(sol.divide(7, 3))  # * 2
print(sol.divide(7, 2))  # * 3
print(sol.divide(-(2**31), -1))  # * INT_MAX
print(sol.divide(5, 1))  # * 1

# * Time: O(log^2 n) - The outer loop runs in O(log n) in the worst case, as does the inner loop

# * Space: O(1) - The memory usage remains constant regardless of input size
