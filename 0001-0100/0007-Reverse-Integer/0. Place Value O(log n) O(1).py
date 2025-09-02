# 7. Reverse Integer

# * We are given a signed 32-bit integer and we need to return it with its digitsd reversed
# * If the reversed value undeflows or overflows, we return 0
# *     - reversed(x) < -2^31
# *     - reversed(x) > 2^31 - 1
# ! Logically speaking, it is a lot easier to handle OVERFLOWS than underflows
# *     - So it makes sense to ONLY deal with overflows by getting the absolute value of the input
# * Mathematically, we can use the following formula to handle the numeric reversals:
# *     - Digit = x % 10
# *         - Gets the last digit of x
# *     - x //= 10
# *         - REMOVES the last digit of x (this isn't a pure operation: mutates x itself)
# *     - num = num * 10 + digit
# *         - Adds space for another digit to prevent column overflows
# *         - 432 = (4 * 10**2) + (3 * 10**1) + (2 * 10**0)
# *         - 234 = (2 * 10**2) + (3 * 10**1) + (4 * 10**0)
# ! Before we update the result, we need to ensure that overflows can't happen
# *     - We ONLY have to check for overflows since we took the absolute value of x
# *         - Mathematically, we'd end up with an underflow in the same situation arised with a negative number
# ! If num > INT32_MAX // 10, then adding another digit will overflow
# ! If num == INT32_MAX // 10 and digit > 7 (it is 8 or 9), multiplying by 10 and adding 8 or 9 will overflow


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX: int = 2**31 - 1  # *  2,147,483,647
        sign: int = (x > 0) - (x < 0)  # * Preserve sign: (1 - 0), (0 - 1) or (0 - 0)
        num: int = 0

        x = abs(x)  # * Prevents the need to deal with negative values for now

        while x != 0:
            digit: int = x % 10  # * Get the LAST digit
            x //= 10  # * Remove the last digit from x

            # ! Check for overflows and underflows BEFORE
            # * If num > INT_MAX // 10, then adding another digit will overflow
            # * If num == INT_MAX // 10, and digit > 7 (i.e. it is 8 or 9), multiplying by 10 and adding 7 or 8 overflows
            if (num > INT_MAX // 10) or (num == INT_MAX // 10 and digit > 7):
                return 0

            # * Handle the place value calculation
            num = num * 10 + digit
        # (num * 1) or (num * -1)
        return num * sign


sol = Solution()
print(sol.reverse(321))  # * 123
print(sol.reverse(123))  # * 321
print(sol.reverse(48152))  # * 25184

# * Time: O(log n) - The time taken scales with the number of digits in `x`
# * Every iteration, we remove one digit, and there are 32 digits at most

# * Space: O(1) - The memory usage remains constant regardless of input size
