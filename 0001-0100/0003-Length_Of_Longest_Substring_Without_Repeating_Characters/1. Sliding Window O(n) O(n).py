# Leetcode 3. Longest Substring Without Repeating Characters

# * We are given a string `s` and the goal is to find the LONGEST substring without repeating characters
# * Naturally, this problem involves counting frequencies
# * We COULD iterate through the string in a brute force manner and try every possible substring
# * However, a better approach would be to use a sliding window approach
# ! The sliding window invariant is that all the characters in the window must have a frequency == 1
# *     - Thus, if this invariant is broken, we need to shrink the window (on the left) until it is fixed
# ! Since there can't be any characters with a frequency > 1, we can use a set
# *     - Any element within the set is considered to be part of the window (and has a frequency of 1)
# *     - To remove elements (characters) from the window, we can simply use set.remove or set.discard (to prevent errors)
# * We can get the length of the window via the formula (end - start + 1)
# *     - This helps because Python's set does not have a length or size property (which would be an O(1) operation)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n: int = len(s)
        longest: int = 0

        # Pointers for the sliding window approach
        start: int = 0
        end: int = 0

        # Tracks the characters in the current window
        chars: set[str] = set()

        while end < n:
            # Shrink the window (on the left) while the invariant is broken
            while s[end] in chars:
                chars.discard(s[start])
                start += 1

            # Add the character to the window (we know its not a duplicate by this point)
            chars.add(s[end])
            longest = max(longest, end - start + 1)
            end += 1

        return longest


# Time: O(n) - It takes O(n) to get the length of the string, and to iterate through s
# Each character in s will be processed at most twice (the inner while loop triggers at most `n` times)
# It takes O(1) on average to add/remove a character from a set

# Space: O(k) - The set's size scales with the number of unique characters in s
# Additionally, the set's size is actually bounded by 26 (the number of lowercase ASCII characters)
