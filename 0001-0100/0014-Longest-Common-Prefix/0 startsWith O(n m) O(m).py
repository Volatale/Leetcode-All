# 14. Longest Common Prefix

# * The goal is to write a function to find the longest common prefix in a string array
# *     - If one doesn't exist, we return ""
# * Ultimately, the output length is bottlenecked by the maximum length of all strings in the input
# * In the worst case, for each string, the "final" possible match is an empty string
# * For each string, we check if the current string matches the prefix
# *     - If it doesn't then we knock off characters from the end of the prefix and repeat


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix: str = strs[0]  # * We know the input isn't empty

        for i in range(1, len(strs)):
            # * Keep removing the last character until the strings match
            while not strs[i].startswith(prefix):
                prefix = prefix[0:-1]

        return prefix


# * Time: O(n * m) - Where `n` is the number of strings in strs, and `m` is the length of the longest strs[i]

# * Space: O(m) - The worst case memory usage scales with the length of the longest string in `strs`
# * Why? In the worst case, we create an identical string
