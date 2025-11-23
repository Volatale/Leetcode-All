# 89. Gray Code

# * An n-bit gray code sequence follows these rules:
# *     Every integer is in the range [0, 2^n - 1]
# *     The first integer is 0
# *     An integer appears no more than once in the sequence
# *     The binary representation of every pair of adjacent integers differs by ONE bit
# *     The binary representation of the first and last differs by exactly ONE bit
# ! We can return ANY valid n-bit sequence, so we simply have to modify one bit per integer
# * Luckily, there is a sequence to the numbers in question
# * Lets say n = 2, we have the following sequence
# *     00
# *     01
# *     10
# *     11
# * Now lets say n = 3
# *     000
# *     001
# *     010
# *     011
# *     100
# *     101
# *     110
# *     111
# * Now lets say n = 4
# *     0000
# *     0001
# *     0010
# *     0011
# *     0100
# *     0101
# *     0110
# *     0111
# *     1000
# *     1001
# *     1010
# *     1011
# *     1100
# *     1101
# *     1110
# *     1111
# ! The LSB column follows a pattern of one zero followed by a one
# ! The next column over (to the left) follows a pattern of two zeroes followed by two ones
# ! The next column over follows a pattern of four zeroes followed by 4 ones
# ! The last column is a series of 8 zeroes followed by 8 ones
# * We can solve this by using the formula: i ^ (i >> 1)
# * For example, 100 ^ 10 gives 110 (ony one bit flips)


class Solution:
    def grayCode(self, n: int) -> list[int]:
        bits: list[int] = []

        for i in range(1 << n):
            bits.append(i ^ (i >> 1))

        return bits


# * Time: O(2^n) - Thare are 2^n iterations per call in each `n`

# * Space: O(2^n) - There are 2^n unique bit numbers in each `n`
