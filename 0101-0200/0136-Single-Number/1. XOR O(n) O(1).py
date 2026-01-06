# 136. Single Number

# * We can take the prefix XOR of the entire array, we'll eventually end up with the lone element
# * Why? Due to the following rules:
# *     - (0 ^ n) == n
# *     - (n ^ n) == 0
# *     - (a ^ b ^ a) == b
# * For example:
# *     - 1 ^ 6 ^ 1
# *      0001
# *      0110 ^
# *     ------
# *      0111
# *      0001 ^
# *     ------
# *      0110
# * Thus, by XOR-ing the entire array, we will eventally be left with the single-occurrence element
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        total: int = 0

        # * (n ^ n == 0), so (1 ^ 6 ^ 1 == 6), (0 ^ 3 = 3). XOR is its own inverse
        for i in range(len(nums)):
            total ^= nums[i]

        return total


sol: Solution = Solution()
print(sol.singleNumber([2, 2, 1]))  # * 1
print(sol.singleNumber([4, 1, 2, 1, 2]))  # * 4
print(sol.singleNumber([1]))  # * 1

# * Time: O(n) - We perform a single pass through the input

# * Space: O(1) - The memory usage remains constant regardless of input size
