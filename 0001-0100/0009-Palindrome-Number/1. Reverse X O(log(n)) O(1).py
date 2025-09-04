# 9. Palindrome Number

# * We are given a integer `x` and our goal is to determine whether or not `x` is a palindrome
# * As an example, the following are palindromes:
# *     - 131
# *     - 8888
# *     - 7
# * The range of values is in the range of an int 32, so [-2^31..2^31 - 1]
# *     - Thus, negative values are possible
# ! Negative numbers are automatically NOT palindromes
# *     -121 != 121-
# * In a brute force manner, we can simply convert the number into a string
# * Then, use a a two pointer approach to check for identical characters
# ! However, we can actually solve this in a more efficient manner
# * It is possible to apply place value to the problem:
# *     - digit = x % 10
# *         Gives us the LAST digit in num
# *     - Then, we can add this digit to our "reversed" number
# *         reversed = reversed * 10 + digit
# * At the very end, we can check if x == reversed
# ! There is no need to handle the negative sign as we already know negative numbers cannot be palindromes
#! Note that Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # * Negative numbers are never palindromes
        if x < 0:
            return False

        num: int = x  # * A copy of x so we can safely mutate `x`
        x_reversed: int = 0

        while num != 0:
            digit: int = num % 10  # * Get the last digit in num
            x_reversed = x_reversed * 10 + digit  # * Apply the digit to our reversed x
            num //= 10  # * Remove the last digit in num

        # * No need to handle any `-` signs; we know `x` is not negative
        return x == x_reversed


sol: Solution = Solution()
print(sol.isPalindrome(121))  # * True
print(sol.isPalindrome(-121))  # * False
print(sol.isPalindrome(10))  # * False
print(sol.isPalindrome(5))  # * True
print(sol.isPalindrome(99))  # * True
print(sol.isPalindrome(8778))  # * True

# * Time: O(log(n)) - The time taken scales with the number of digits in `x`

# * Space: O(1) - The memory usage remains constant regardless of input size
