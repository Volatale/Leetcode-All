# 12. Integer to Roman

# * Since the goal is a conversion, we need to map the numbers to numerals
# * We know we can have up to THREE adjacent (consecutive) identical roman numerals
# * And we also know that to create numbers that contain the digit 9, we need to use the subtractive principle
# *       III = 3, V = 4, IV = 5 (5 - 1)
# *       X = 10, IX = 9 (10 - 1)
# *       L = 50, XL = 40 (50 - 10)
# ! If a smaller numeral is followed by a larger, we need to subtract the value on the left from the value on the right
# * Additionally, similarly to the decimal system's place value (base 10), larger digits exist on the LEFT of the place value representation
# *     - Since we know we can only have 3 consecutive identical numerals, and they appear in DESCENDING order...
# ! It makes sense to also sort the mappings into descending order
# * Mathematically, we can repeatedly subtract the maximal value'd numeral that can fit into num
# *     - Eventually this won't work for the current numeral, in which case we try the very next (smaller) numeral
# ! In order to avoid complications with calculating numbers involving 9, we precompute the values within the mapping


class Solution:
    def intToRoman(self, num: int) -> str:
        # * Simulates a string builder
        result: list[str] = []

        # * Integer -> Roman Numeral. Sorted in DESC for easy processing
        mapping: dict[int, str] = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        # * Try every possible numeral in descending order
        for val, numeral in mapping.items():
            while num >= val:
                num -= val  # * Subtract the numeral's integer value
                result.append(numeral)  # * Add the corresponding numeral

        return "".join(result)


sol: Solution = Solution()
print(sol.intToRoman(3749))  # * MMMDCCXLIX
print(sol.intToRoman(84))  # * LXXXIV
print(sol.intToRoman(3))  # * III
print(sol.intToRoman(5))  # * V
print(sol.intToRoman(99))  # * XCIX
print(sol.intToRoman(3888))  # * MMMDCCCLXXXVIII

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
