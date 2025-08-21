# 1. Two Sum

# * We need to return the indices of the two numbers whose sum is equal to `target`
# *     - A solution is guaranteed to exist
# !     - We are unable to use the same index multiple times
# * In a brute force manner, we can simply try every possible pairing of numbers
# * Thus, we can use a nested for loop to find both `i` and `j`
# *     - nums[i] + nums[j] == target ? Then return [i, j]
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n: int = len(nums)

        # * Try every possible pairing of [i, j]
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        #! Impossible path
        return [-1, -1]


sol: Solution = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # * [0, 1]
print(sol.twoSum([1, 2, 3], 4))  # * [0, 2]
print(sol.twoSum([1, 1], 2))  # * [0, 1]


# * Time: O(n^2) - We have a pair of nested loops, both of which scale with `n`

# * Space: O(1) - The memory usage remains constant regardless of input size
