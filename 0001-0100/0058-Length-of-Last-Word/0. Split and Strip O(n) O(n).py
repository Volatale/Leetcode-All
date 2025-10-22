# 58. Length of Last Word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


sol = Solution()
print(sol.lengthOfLastWord("Hello World"))  # * 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # * 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # * 6
print(sol.lengthOfLastWord("World  "))  # * 5
print(sol.lengthOfLastWord("a"))  # * 1
# print(sol.lengthOfLastWord(""))  # * 0
print(sol.lengthOfLastWord("      sonic"))  # * 5
print(sol.lengthOfLastWord("      sonic oi      "))  # * 2

# * Time: O(n) - In the worst case, the entire input is one word so we iterate over the entire input

# * Space: O(n) - We create ephemeral copies of the input string, so the memory usage scales with the input size
