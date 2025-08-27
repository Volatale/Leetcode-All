# 5. Longest Palindromic Substring

# * Given a string `s`, the goal is to return the longest palindromic substring
# * In a brute force manner, we could generate all possible substrings (n^2)
# *     - Then, for each substring `s`, check if `s` is a substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        n: int = len(s)
        longest: str = ""

        # Generate every possible substring
        for i in range(0, n - 1):
            for j in range(i):
                substr = longest[i : j + 1]

                if self._isPalindrome(substr):
                    longest = substr

        return longest

    def _isPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = 0

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right += 1

        # `s` is a palindrome
        return True


sol = Solution()

print(sol.longestPalindrome("babad"))  # * bab
print(sol.longestPalindrome("cbbd"))  # * bb
print(sol.longestPalindrome("abccba"))  # * abccba
print(sol.longestPalindrome("aaa"))  # * aaa
print(sol.longestPalindrome("v"))  # * v

# Time: O(n^3) - There are n^2 substrings in total, and it takes O(n) to check for a palindrome

# Space: O(n) - In the worst case (per inner iteration), we create a substring of length `n`
