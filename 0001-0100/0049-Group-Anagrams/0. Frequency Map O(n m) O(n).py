# 49. Group Anagrams

# * An anagram is a string that is frequency-wise equal to another
# * For example, the strings "bat" and "tar" are anagrams
# *     - They each share the same characters
# *     - And they each share the same frequency for those characters
# * So, for each string, we can count the frequency of characters
# * We can then convert the frequency of characters into a string
# * Finally, using the string, we can group anagrams within a list
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # * There are no anagrams
        if len(strs) == 0:
            return []

        groups: dict[str, list[str]] = {}

        for string in strs:
            # * Convert the frequency of characters into a string
            freq = str(self._getFreq(string))

            # * If we don't have a group for this frequency (anagram), create one
            if freq not in groups:
                groups[freq] = []

            # * Add this string to the corresponding anagram group
            groups[freq].append(string)

        return [groups[group] for group in groups]

    def _getFreq(self, str: str) -> list[int]:
        # * 0 = `a`, 1 = 'b', 2 = 'c', 25 = 'z'
        freq: list[int] = [0] * 26

        # * Get the frequency of every character in `str`
        for char in str:
            freq[ord(char) - 97] += 1

        return freq


sol: Solution = Solution()
print(sol.groupAnagrams(["hey", "yeh", "no"]))
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))

# * Time: O(n * m) - There are `n` strings within `strs`, and `m` is the max length string

# * Space: O(n) - The memory usage scales with the input size
# * Regardless of our choice, we always return the same number of strings
