# 9. Palindrome Number

# * We are given a integer `x` and our goal is to determine whether or not `x` is a palindrome
# * As an example, the following are palindromes:
# *     - 131
# *     - 8888
# *     - 7
# * The range of values is in the range of an int 32, so [-2^31..2^31 - 1
# *     - Thus, negative values are possible
# ! Negative numbers are automatically NOT palindromes
# *     -121 != 121-
# * In a brute force manner, we can simply convert the number into a string
# * Then, use a a two pointer approach to check for identical characters
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # * Negative numbers are never palindromes
        if x < 0:
            return False

        num: str = str(x)

        # * Two pointers to track the indices in nums
        left = 0
        right = len(num) - 1

        # * Iterate through nums to check for the palindrome property
        while left < right:
            # * `x` is not a palindrome
            if num[left] != num[right]:
                return False

            left += 1
            right -= 1

        # * `x` is a palindrome
        return True


sol: Solution = Solution()
print(sol.isPalindrome(121))  # * True
print(sol.isPalindrome(-121))  # * False
print(sol.isPalindrome(10))  # * False
print(sol.isPalindrome(5))  # * True
print(sol.isPalindrome(99))  # * True
print(sol.isPalindrome(8778))  # * True

# * Time: O(n) - The time taken scales with the number of digits in `x`

# * Space: O(n) - The length of `num` scales with the number of digits in `x`
