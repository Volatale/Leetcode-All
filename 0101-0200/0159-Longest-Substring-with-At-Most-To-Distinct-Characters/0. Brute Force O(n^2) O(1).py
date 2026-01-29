# 159. Longest Substring with At Most Two Distinct Characters

# * In a brute force manner, we can try every possible substring
# * Since we're trying to count unique characters, we can use a set
# * Instead of re-declaring a new set for each substring, we can simply clear() the set
# * If len(set) > 2 for the current substrnig, we can immediately break out of the inner loop
# *     - Why? Because we're always extending the substring
# *     - We'll never "lose" characters (the substring does not decrease in size), so continuing won't help
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) == 1:
            return 1

        n: int = len(s)
        longest: int = 0
        chars: set[str] = set()

        for i in range(n):
            chars.clear()  # * Avoids the need to a new set each iteration

            for j in range(i, n):
                if s[j] not in chars:
                    chars.add(s[j])

                    # * We have too many characters
                    if len(chars) > 2:
                        break

                    longest = max(longest, j - i + 1)

        return longest


# * Time: O(n^2) - The time taken scales with `n` quadratically; we try every possible substring

# * Space: O(1) - In the worst case, the size of the set is 2
