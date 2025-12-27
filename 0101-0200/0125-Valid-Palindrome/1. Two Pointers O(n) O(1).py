# 125. Valid Palindrome

# * We use a two pointer approach because that allows us to simultaneously compare chars
# * There is no need to modify the string at all
# * Simply skip past any elements that are not alphanumeric
# * And whenever we find characters that ARE alphanumeric, we can call .lower()


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n: int = len(s)

        # * Two pointers for palindrome checking
        left: int = 0
        right: int = n - 1

        while left < right:
            # * Skip the non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # * Check for validity
            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# * Time: O(n) - We have to process every character in the input in the worst case

# * Space: O(1) - The memory usage remains constant regardless of input size
