# * 76. Minimum Window Substring

# * The goal is to find the minimum length substring such that all the characters in `t` are in the substring (in `s`)
# * The easiest way to achieve this is to use a sliding window
# * A substring is contiguous, which works perfectly with the idea of a sliding window
# ! Immediately, we get the frequency of characters in `t`
# * Then, we begin the sliding window
# ! We are using the "need vs have" variation of sliding window since we are dealing with frequencies
# * This prevents the need to validate the frequency of s_freq vs t_freq using loops every time the window shrinks
# *     - We first need to get the frequency of characters in `t`
# *     - For a valid window, we need len(t) characters
# * Specifically, we are looking to meet the quota of characters in `t` within `s`
# *     A valid window has "need == have" (as in we needed 4 characters and we have them)
# * If we find a character that exists in `t`, and the no. of occurrences we have in the window < t's frequency
# *     - have += 1 (because we made progress toward the goal)
# * Since we want the MINIMUM window, we keep expanding the window until it becomes valid
# * Then, if we have a new "best" (minimum length string):
# *      bestStart = start
# *      bestEnd = end
# *      min_length = end - start + 1
# * Since we want the MINIMUM length substring, and we have a valid window, we shrink on the left until the window is invalid
# *     - Why? Because if we remove characters we don't need and the window is still valid, we end up with a "new best" each iteration
# *
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # * There is no way s contains all the characters in t
        if len(t) > len(s):
            return ""

        n: int = len(s)
        m: int = len(t)

        # * Two pointers for the sliding window
        start: int = 0
        end: int = 0

        # * Markers for the substring start/end
        best_start: int = 0
        best_end: int = 0
        min_length: int = (1 << 31) - 1

        # * Used for need vs have variation of sliding window
        need: int = m
        have: int = 0

        # * Tracks the frequency of characters in each
        s_freq: dict[str, int] = {}
        t_freq: dict[str, int] = {}

        # * Get the frequency of characters in t
        for i in range(m):
            t_freq[t[i]] = (t_freq.get(t[i]) or 0) + 1

        while end < n:
            # * Update the frequency of this character
            s_freq[s[end]] = (s_freq.get(s[end]) or 0) + 1

            # * Check if we made progress (if character we need entered window)
            if t_freq.get(s[end]) and s_freq[s[end]] <= t_freq[s[end]]:
                have += 1

            # * While the window is valid, potentially update pointers and then shrink window
            while have == need:
                if end - start + 1 < min_length:
                    best_start = start
                    best_end = end
                    min_length = end - start + 1

                # * Remove the leftmost character from window
                s_freq[s[start]] -= 1

                # * Check if we lost any progress (if character we need left window)
                if t_freq.get(s[start]) and s_freq[s[start]] < t_freq[s[start]]:
                    have -= 1

                if s_freq[s[start]] == 0:
                    del s_freq[s[start]]

                start += 1
            end += 1

        # * Return the minimum window substring (if we can)
        return s[best_start : best_end + 1] if min_length < (1 << 31) - 1 else ""


sol: Solution = Solution()
print(sol.minWindow("aa", "aa"))
print(sol.minWindow("awec", "aec"))
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("a", "a"))
print(sol.minWindow("a", "aa"))
print(sol.minWindow("abc", "abcd"))

# * Time: O(n + m) - We iterate over `t`, which takes O(m) time, then over `s` which takes O(n) time

# * Space: O(k) - Where `k` is the number of unique characters in `t` and `s`
