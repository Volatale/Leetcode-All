# 65. Valid Number

# * An integer is defined with an optional sign followed by digits
# * A decimal is defined with an optional sign followed by one of these definitions:
# *     Digits followed by a `.` (123.)
# *     Digits followed by a `.` followed by digits (123.456)
# *     A `.` followed by digits (.123)
# * An exponent is defined with exponent notation `e` or `E` followed by an integer number

# ! From this, we know the following rules:
# *     We need to have seen at least one digit for either classification to be met
# *     If at the end we have not seen a digit, return False

# *     A sign can only appear at the 0th index or the character immediately after an exponent
# *     We CAN have multiple signs, however. "+102.e+3" is valid

# *     An exponent must come after a digit (so we must have seen a digit)

# *     Decimal definition comes before exponent definition (which can ONLY be followed up with an integer)
# *     Thus, we must not have seen a dot or an exponent if we encounter a `.`

# *     There can only be ONE exponent (so we must not have already seen an exponent)
# *     There can only be ONE dot (so we must not have already seen an exponent)
class Solution:
    def isNumber(self, s: str) -> bool:
        # * Handle whitespace and empty inputs
        s = s.strip()

        if not s:
            return False

        seen_digit = seen_dot = seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True

            elif ch in ["+", "-"]:
                # * Sign is valid only at start or immediately following exponent
                if i > 0 and s[i - 1] not in ["e", "E"]:
                    return False

            elif ch == ".":
                # * Dot not allowed after exponent or already in use
                if seen_dot or seen_exp:
                    return False

                seen_dot = True

            elif ch in ["e", "E"]:
                # * Exponent must come after a digit, and only once
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                seen_digit = False  # * Must see digit after exponent now

            else:
                return False

        return seen_digit


sol: Solution = Solution()
print(sol.isNumber("0"))  # * True
print(sol.isNumber("e"))  # * False
print(sol.isNumber("."))  # * False
print(sol.isNumber("1.1"))  # * True
print(sol.isNumber("1.1e1"))  # * True
print(sol.isNumber("4.1.2"))  # * False
print(sol.isNumber("1."))  # * True
print(sol.isNumber("2.."))  # * False
print(sol.isNumber("5.e"))  # * False
print(sol.isNumber("-1"))  # * True
print(sol.isNumber("-1.2"))  # * True
print(sol.isNumber("-1.2e5"))  # * True
print(sol.isNumber("-1.-2"))  # * False
print(sol.isNumber("-1.2e."))  # * False
print(sol.isNumber("--1"))  # * False
print(sol.isNumber("-+2"))  # * False
print(sol.isNumber("abc"))  # * False
print(sol.isNumber("1a"))  # * False
print(sol.isNumber("1a"))  # * False
print(sol.isNumber("e3"))  # * False
print(sol.isNumber("99e2.5"))  # * False
print(sol.isNumber("--6"))  # * False
print(sol.isNumber("-+3"))  # * False
print(sol.isNumber("95a54e53"))  # * False

# * Time: O(n) - The time taken scales with input size

# * Space: O(1) - The memory usage remains constant regardless of input size
