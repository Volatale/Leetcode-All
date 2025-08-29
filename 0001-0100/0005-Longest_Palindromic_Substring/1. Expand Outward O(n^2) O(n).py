# 5. Longest Palindromic Substring

# * Given a string `s`, the goal is to return the longest palindromic substring
# * In a brute force manner, we could generate all possible substrings (n^2)
# *     - Then, for each substring `s`, check if `s` is a substring
# ! However, this is a relatively slow approach
# * Ultimately, this problem comes down to:
# *     - Dynamic programming - O(n^2) O(n^2)
# *     - An alternative DP approach - O(n^2) O(1)
# *     - Manacher's Algorithm - O(n) O(n)
# * Here, we'll go with the alternative to DP
# * There are two types of palindromes:
# *     - Odd length palindromes ("aba", "accca")
# *     - Even length palindromes ("abba", "xyzzyx")
# ! Based on this logic, we can expand OUTWARD from each index and still hit every possible palindrome
# * Why does this work?
# *     - Because a valid palindrome must have equal characters at all times as we expand outward
# *     - Thus, using a two pointer approach we can directly check for palindromes
# * However, since we know a palindrome can be of even or odd length, we need to do TWO checks per palindrome


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        n: int = len(s)
        longest: str = s[0]  # Minimum palindrome is always of length 1

        # Try every possible starting point for a palindrome (every index)
        for i in range(0, n - 1):
            odd: str = self._expandFromCenter(s, i, i)  # Odd length palindromes
            even: str = self._expandFromCenter(s, i, i + 1)  # Even length palindromes

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest

    def _expandFromCenter(self, s: str, left: int, right: int) -> str:
        n = len(s)

        # Remain in bounds, and only expand (outward) if the characters match
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        # Since `left` is "out of bounds", +1 to stay WITHIN bounds
        return s[left + 1 : right]


# Time: O(n^2) - For each index `i`, we perform an O(n) iteration in the worst case

# Space: O(n) - In the worst case, we create a substring of length `n`
