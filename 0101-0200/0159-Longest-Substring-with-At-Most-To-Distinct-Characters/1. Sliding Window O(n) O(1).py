# 159. Longest Substring with At Most Two Distinct Characters

# * Instead of trying every possible substring, we can use a sliding window approach
# * At each step, we need to validate the current window based on the sliding window invariant
# * In our case, the invariant is that the window cannot store more than 2 unique characters
# * If it does, we need to shrink the window on the left
# * Otherwise, we can keep extending on the right
# * We can apply the (right - left + 1) formula to get the length of the window, and thus the length of the "substring"
# * A set COULD be used to track the unique characters that exist within the window, and thus validate the window
# !     - However, note that duplicates are more than possible
# * We cannot simply use a set here because the frequency of the element leaving could be > 1
# * If we remove elements at s[left], it'd lead to incorrect results if the frequency of s[left] > 1 (because there are more in the window)
# ! Additionally, we need to use an inner while loop because it isn't guaranteed that removing a single element from the window makes it validate
# *     - It is possible that we need to remove multiple (and thus, multiple checks/iterations must be performed)
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) == 1:
            return 1

        n: int = len(s)
        longest: int = 0
        freq: dict[str, int] = {}  # * Char -> Frequency

        # * Two pointers for the sliding window
        left: int = 0
        right: int = 0

        while right < n:
            # * Add the current char to the window
            freq[s[right]] = (freq.get(s[right]) or 0) + 1

            # * Validate the window (ensure frequency <= 2)
            while len(freq) > 2:
                freq[s[left]] -= 1

                # * Only delete the key if the frequency is 0
                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        return longest


sol: Solution = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct("eceba"))  # * 2
print(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb"))  # * 5
print(sol.lengthOfLongestSubstringTwoDistinct("sonic"))  # * 2
print(sol.lengthOfLongestSubstringTwoDistinct("shadow"))  # * 2
print(sol.lengthOfLongestSubstringTwoDistinct("abccbdefeggh"))  # * 4
print(sol.lengthOfLongestSubstringTwoDistinct("c"))  # * 1
print(sol.lengthOfLongestSubstringTwoDistinct("aaa"))  # * 3
print(sol.lengthOfLongestSubstringTwoDistinct("xy"))  # * 2

# * Time: O(n) - We need to iterate over every element in the input, so the time taken scales with the input size

# * Space: O(1) - In the worst case, the size of the set is 2
