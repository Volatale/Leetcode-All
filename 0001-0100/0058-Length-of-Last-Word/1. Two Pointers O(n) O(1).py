# 58. Length of Last Word

# * We want to return the length of the last word in the input
# * Thus, we can use a two pointer approach
# * With the right pointer, skip all of the trailing whitespace
# * Then, starting from the right pointer's index, left skips past all of the NON-whitespace characters
# * At the very end, left will either be at index -1, or at the index one before the last word's start
# * We can get the length of the string via (right - left + 1)
# !     - However, remember that left is one index to the left of where it should be
# *     - Hence we add 1 to left to fix the offset
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n: int = len(s)

        # * Used to travel from right to left
        right: int = n - 1

        # * Start at the end and skip past any trailing whitespace
        while right >= 0 and s[right] == " ":
            right -= 1

        # * Keep moving the left pointer until we reach the end of the word (or out of bounds)
        left = right
        while left >= 0 and s[left] != " ":
            left -= 1

        # * Left traveled 1 past the end of the word so add one back
        return right - (left + 1) + 1


sol = Solution()
print(sol.lengthOfLastWord("Hello World"))  # * 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # * 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # * 6
print(sol.lengthOfLastWord("World  "))  # * 5
print(sol.lengthOfLastWord("a"))  # * 1
print(sol.lengthOfLastWord(""))  # * 0
print(sol.lengthOfLastWord("      sonic"))  # * 5
print(sol.lengthOfLastWord("      sonic oi      "))  # * 2

# * Time: O(n) - In the worst case, the entire input is one word so we iterate over the entire input

# * Space: O(1) - The memory usage remains constant regardless of input size
