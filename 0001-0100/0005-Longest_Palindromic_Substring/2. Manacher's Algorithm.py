# 5. Longest Palindromic Substring

# * Given a string `s`, the goal is to return the longest palindromic substring
# * In a brute force manner, we could generate all possible substrings (n^2)
# *     - Then, for each substring `s`, check if `s` is a substring
# ! However, this is a relatively slow approach
# * Ultimately, this problem comes down to:
# *     - Dynamic programming - O(n^2) O(n^2)
# *     - Expand outward from every index - O(n^2) O(1)
# *     - Manacher's Algorithm - O(n) O(n)
# * Here, we'll go with Manacher's algorithm
# * Part of the intuition behind Manacher's algorith is that some palindromes are of even AND odd lengths
# *     - This is why we can do the "expand outward" approach (because we check for both cases)
# * To handle this using Manacher's algorithm, we insert separators like `#` between characters
# *     - s = "abba"
# *     - T = "^#a#b#b#a#$"
# !         - ^ and $ are sentinel values (prevents the need for bounds checks)
# * The seperators ensure that all palindromes in `s` are of ODD length
# *     - "bb" -> length 2 (even)
# *         - "#b#b#" length 5 (odd)
# *     - "a" -> length 1 (odd)
# *         - "#a#" -> length 3 (STILL odd)
# ! We have an array `p`, where p[i] = radius of palindrome centered at index `i`
# *     - E.g, in "^#a#b#b#a#$", p[3] = 3, because we get the following palindrome:
# * Part of our goal is to track two variables, `C` and `R`
# *     - C = Center of the rightmost palindrome found thus far
# *     - R = Right boundary of that palindrome
# * If we are at position `i`, and i < R
# *     - Then we can MIRROR around the center `C`
# *         - mirror = 2 * C - i
# *         - p[i] = min(R - i, P[mirror])
# !     - This means the palindrome at `i` is AT LEAST as big as its mirror (unless it overflows beyond R)
# * Logically speaking, we should start and end our algorithm at index 1 and index n - 1 respectively
# *     - ^ and $ can never be part of a palindrome, so there's no point in checking these characters
# * After setting P[i] from the mirror, try to keep expanding further outward by comparing characters
# * If the expansion goes beyond `R`
# *     - C = i
# *     - R = i + P[i]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        n: int = len(s)
        T: str = "^#" + "#".join(s) + "#$"  # Preprocessing
        P: list[int] = [0] * n
        center: int = 0  # The center of the palindrome
        right: int = 0  # Right boundary of the palindrome

        for i in range(1, n - 1):
            # Mirror index around center
            mirror: int = 2 * center - i

            # We can mirror around center
            if i < right:
                P[i] = min(right - i, P[mirror])

            # Attempt to expand the palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If we expanded past right, update center and right
            if i + P[i] > right:
                center, right = i, i + P[i]

        # Find max length palindrome
        maxLength, centerIndex = max((i, n) for i, n in enumerate(P))
        start = (centerIndex - maxLength) // 2  # Back to original string index

        return s[start : start + maxLength]
