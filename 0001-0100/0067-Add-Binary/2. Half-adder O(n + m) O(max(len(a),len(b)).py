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
# * If (bit_a & bit_b) == 1, then both are ones, and 1 + 1 = 2, which overflows the place value of binary (0, 1)
# * If (bit_a & carry) == 1, then both are ones
# * If (bit_b & carry) == 1, then both are ones
# * This problem is essentially elementary addition, but applied to binary
# *     1
# *     1 1
# *     1 1
# *     ---
# *   1 0 0
# * In the rightmost column: (1 ^ 1 ^ 0) == 0, so the digit is 0
# *     - We met the criteria of having at least 2 ones (bit_a & bit_b)
# *       Thus, we have a carry
# * In the next column, (1 ^ 1 ^ 1) == 1, so the digit is 1
# *     - We met the criteria of having at least 2 ones (bit_a & bit_b), or, (bit_a & c), or, (bit_b & c)
# *       Thus, we have a carry
# * In the last column, (1 ^ 0 ^ 0) == 1, so the digit is 1
# *     - We didn't meet the criteria of having at least 2 ones (so no carry)
# * carry = (x & y) | (c & (x ^ y))
# *     (x & 1) covers the case where both string digits are 1
# *     (x ^ y) means "exactly one of x and y is 1"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result: list[str] = []
        i, j = len(a) - 1, len(b) - 1
        carry: int = 0

        while i >= 0 or j >= 0 or carry:
            bit_a: int = int(a[i]) if i >= 0 else 0
            bit_b: int = int(b[j]) if j >= 0 else 0

            # * Sum bit
            digit: int = bit_a ^ bit_b ^ carry
            result.append(str(digit))

            # * Update carry: Only occurs if at least two of `bit_a`, `bit_b`, `carry` are 1
            # carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)
            carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))

            i -= 1
            j -= 1

        # * The binary digits are in reverse order
        return "".join(reversed(result))


sol: Solution = Solution()
print(sol.addBinary("11", "11"))

# * Time: O(n + m) - We have to iterate through both strings in their entirety

# * Space: O(max(len(a), len(b))) - The resulting array's size is the max length of both + 1 in the worst case
