# 13. Roman to Integer

# * Similarly to Leetcode 12, Integer to Roman, we should immediately create a mapping
# * Some observations need to be made:
# *     - We know that with roman numerals, we can only have three consecutive identical numerals
# *     - We also know that when certain smaller numerals are followed by certain larger numerals, we subtract
# * To make things easy, we should iterate from right to left, but we can also do it the other way around
# * We implicitly assume that we need to add the current value
# !     - Except in cases where the subtraction principle applies
# *     - In that case, we subtract the integer value from the current total
# ! Note that when the subtractive principle applies:
# *     - I can be followed by V and X
# *     - X can be followed by L and C
# *     - C can be followed by D and M
# ! Therefore, "IL" is NOT a valid roman numeral to represent 49, it would be "XLIX"
class Solution:
    def romanToInt(self, s: str) -> int:
        sum: int = 0
        n: int = len(s)

        mapping: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for i in range(0, n):
            if i + 1 < n and mapping[s[i]] < mapping[s[i + 1]]:
                sum -= mapping[s[i]]  # * Subtractive principle applies
            else:
                sum += mapping[s[i]]  # * Add the value as normal

        return sum


# * Time: O(1) - The input size is always in the range [1, 3999], so the time complexity is constant
# * It isn't O(n) because the number of iterations doesn't scale linearly with the input size
# * Its also not O(d) where `d` = no. of digits, because intToRoman(3) results in 3 iterations, and intToRoman(5) is only 1
# * There are 3 possible consecutive "M" for the thousands column (3000)
# * The longest possible number for the hundreds column is "DCCC" (800)
# * For tens, the longest number is "LXXX" (80)
# * For ones, the longest number is "VIII" (8)
# * Altogether, that gives us 3888
# * Sum the maxima (iterations in the worst case) -> 3 (thousands) + 4 (hundreds) + 4 (tens) + 4 (ones) = 15

# * Space: O(1) - The memory usage remains constant regardless of the input size
