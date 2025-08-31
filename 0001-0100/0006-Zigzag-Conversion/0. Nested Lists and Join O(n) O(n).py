# 5. Zigzag Conversion

# * We are given a string `s` that is written in zigzag style
# *      P   A   H   N
# *      A P L S I I G
# *      Y   I   R
# * The goal is to return the string as it is written in left to right (concatenate all character son each row)
# * Since we know the number of rows, we can quite literally create the structure of what the input SHOULD look like
# * Then, as we already know, concatenate all of the rows from top to bottom
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        letters: list[list[str]] = [[] for _ in range(numRows)]
        row = 0
        increasing = True  # Whether or not to increase or decrease the row

        # Iterate over every character and determine where to put it
        for i in range(len(s)):
            letters[row].append(s[i])

            row += 1 if increasing else -1

            # Swap directions if necessary
            if row == 0 or row == numRows - 1:
                increasing = not increasing

        # Combine all of the characters in each line into one string
        return "".join("".join(line) for line in letters)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
print(sol.convert("SONICTHEHEDGEHOG", 4))  # SHEOTEGHNCHDOIEG

# * Time: O(n) - It takes O(numRows) to create the letters list
# * Then, we iterate over the entire input string which takes O(n)
# * Finally, the number of `join` calls we make scales with len(s) / numRows, but numRows is constant

# * Space: O(n) - Ultimately, we create a string of equal length to the input
# * We also create len(s) / numRows nested lists to hold each of these characters
