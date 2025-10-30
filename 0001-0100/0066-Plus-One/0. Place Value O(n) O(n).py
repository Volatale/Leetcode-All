# 66. Plus One

# * We can manually calculate the value of the list using place value
# * Then, we can add one to that total
# * After, convert the array into a string and return an array of the characters as integers
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        total: int = 0

        # * Manually calculate the value of the digits
        for digit in digits:
            total = total * 10 + digit

        total += 1

        # * We have a int, so convert it to a string, then distribute the characters as ints
        return [int(digit) for digit in str(total)]


sol: Solution = Solution()
print(sol.plusOne([1]))  # * [2]
print(sol.plusOne([9]))  # * [1, 0]
print(sol.plusOne([9, 9, 9]))  # * [1,0,0,0]

# * Time: O(n) - We have to iterate over the entire input
# * Then, it takes O(n) to create the string out of the total, and O(n) to create the return array

# * Space: O(n) - It takes O(n) memory to create the string, then O(n) to create the return array
