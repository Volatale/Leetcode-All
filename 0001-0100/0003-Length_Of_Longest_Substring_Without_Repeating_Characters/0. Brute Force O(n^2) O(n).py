# Leetcode 3. Longest Substring Without Repeating Characters

# * We are given a string `s` and the goal is to find the LONGEST substring without repeating characters
# * Naturally, this problem involves counting frequencies
# * In a brute force manner, we can try every possible substring and count the length of the longest that follows the constraint
# * Since the maximum number of occurrences for ANY valid substring is 1, we can use a Set
# *     - If the current character already exists in the set, then we can't extend the substring anymore

from __future__ import annotations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n: int = len(s)
        longest: int = 0
        unique: set[str] = set()  # Provides O(1) lookups on average

        # Try every possible substring
        for i in range(n):
            unique.clear()  # Clearing the set every iteration is faster than creating a new one

            for j in range(n):
                if s[j] in unique:
                    break

                longest = max(
                    longest, j - i + 1
                )  # j - i + 1 gets the length of the substring
                unique.add(s[j])

        return longest


# Time: O(n^2) - We are using a pair of nested loops whose time taken scales with the size of the input `n`
# It takes O(1) to create the set, and likely O(1) to clear it
# set.add() is also likely an O(1) operation

# Space: O(n) - In the worst case, every character in the substring is unique
# Thus, the set can grow to be of equal size to the input
