# 8. String to Integer (atoi)

# * We only care about the signedness up until we find our first digit
# *     - After the first digit is found, signs are essentially termination characters
# *     - They aren't digits, thus the loop exits
# * There are possibly `n` characters of whitespace before any digits are encountered
# *     - Thus, we should skip any whitespace characters that exist
# *     - We can either do this via `lstrip()` (which is O(n)), or do it manually via indexing
# * Regardless of the method of whitespace-skipping, the moment we find a digit, the signedness is assumed to be POSITIVE
# *     - We can use a boolean to track whether or not we care about signedness from this point onward
# ! The moment we find a character that ISN'T a digit (after skipping the whitespace), the loop should exit
# * We can use a variable to track the signedness (assume it is positive until it isn't)
# ! To make things easier, we assume the number is negative and it becomes negative if need be (as a return result)
# * Additionally, it is easy to notice that we never end up LOSING digits
# *     - Therefore, the moment we hit an overflow, we can immediately return
# *     - Why? Since we never lose digits, the value of `result` can never decrease
# *         - We are perpetually adding digits, thus increasing the place value (and thus the numerical value of result)
# ! Lastly note the overflow detection formulas:
# *     - If result > INT32_MAX // 10, then adding a new digit will overflow
# *     - If result == INT32_MAX // 10, then we need to do some additional checks
# *         - If signedness == 1 and digit > 7, then we'll overflow
# *         - If signedness == -1 and digit > 8, then we'll overflow
# !         - Why the distinction? Because remember, INT32_MIN = -(2 ** 31) - 1
# *             - The subtract one means the last digit ends up being 8 and not 7 (like it is with (2 ** 31) - 1)
# *                 2147483647
# *                 -(2147483648)
class Solution:
    def myAtoi(self, s: str) -> int:
        result: int = 0
        signedness: int = 1  # * Assume signedness is positive
        INT32_MAX: int = 2**31 - 1
        INT32_MIN: int = -(2**31)

        i: int = 0
        n: int = len(s)

        # * Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # * Handle sign
        if i < n and (s[i] == "-" or s[i] == "+"):
            signedness = -1 if s[i] == "-" else 1
            i += 1

        # * Process digits
        while i < n and s[i].isdigit():
            digit: int = int(s[i])

            # ! Handle potential overflows
            if result > INT32_MAX // 10 or (
                result == INT32_MAX // 10 and digit > (7 if signedness == 1 else 8)
            ):
                return INT32_MAX if signedness == 1 else INT32_MIN

            result = result * 10 + digit
            i += 1

        # * (n * negative = negative) vs (n * positive) = positive
        return result * signedness


# * Time: O(n) - The time taken scales with the size of the input

# * Space: O(1) - The memory usage remains constant regardless of input size
