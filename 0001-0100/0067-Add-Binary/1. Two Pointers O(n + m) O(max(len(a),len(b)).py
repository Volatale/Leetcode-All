# 67. Add Binary

# * Here are the XOR rules;
# *     1 ^ 1 = 0
# *     1 ^ 0 = 1
# *     0 ^ 1 = 1
# *     0 ^ 0 = 0
# * We can determine the digit that should go into each position through bitwise AND
# *     1 & 1 = 1
# *     1 & 0 = 0
# *     0 & 1 = 0
# *     0 & 0 = 0
# ! However, we may need to deal with a carry (which may be dealt with in the next column <---)
# *     1 ^ 1 ^ 1 = 1
# * Thus, the carry should be added into the sum
# * We ONLY have to deal with a carry in the cases where we have at least TWO ones
# *     1 ^ 1 = 0
# *     1 ^ 1 ^ 1 = 1


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result: list[str] = []

        # * Two pointers to track progress through inputs
        i: int = len(a) - 1
        j: int = len(b) - 1

        carry: int = 0

        while i >= 0 or j >= 0 or carry:
            curr: int = carry

            if i >= 0:
                curr += int(a[i])
                i -= 1

            if j >= 0:
                curr += int(b[j])
                j -= 1

            # * Calculate binary digit and carry
            result.append(str(curr & 1))  # * (1 & 1) = 1
            carry = curr >> 1  # * (2 / 2) = 1

        # * The binary digits are in reverse order
        return "".join(reversed(result))


# * Time: O(n + m) - We have to iterate through both strings in their entirety

# * Space: O(max(len(a), len(b))) - The resulting array's size is the max length of both + 1 in the worst case
