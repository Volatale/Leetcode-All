# 66. Plus One


# * The size of the input is monotonically non-decreasing
# *     - That is, the size either remains the same, or it is increased by one
# *     - [9] = Size 1, but adding one gives us [1, 0] which has size 2
# *     - Alternatively, we could have [6] -> [7] (size 1 -> size 1)
# ! We "could" simulate what happens with elementary addition, but that is more complicated
# * Instead, iterate from the end to the left
# * If we encounter a digit < 9, then perfect
# *     - Simply add 1 to that digit and return
# * Otherwise, we have a 9
# *     - Thus, set the current digit to 0
# * Keep repeating this process until we run out of digits, or we find a digit != 9
# * If we ran out of characters, the entire array is 0s
# * Thus, we can add a 1 as the very first character
# * For example:
# *     - [9, 9, 9]
# *     - [9, 9, 0]
# *     - [9, 0, 0]
# *     - [0, 0, 0]
# *     - [1, 0, 0, 0]
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # * Iterate backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # * Simply add one to the digit
                return digits
            else:
                digits[i] = 0  # * Set it to 0, since it will be eventually

        # * Append a 1 to the start of the array
        digits.insert(0, 1)
        return digits


sol: Solution = Solution()
print(sol.plusOne([1]))  # * [2]
print(sol.plusOne([9]))  # * [1, 0]
print(sol.plusOne([9, 9, 9]))  # * [1,0,0,0]

# * Time: O(n) - In the worst case, we iterate over every element

# * Space: O(1) - In the worst case, the array's size only increases by 1
