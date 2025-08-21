# 1. Two Sum

# * We need to return the indices of the two numbers whose sum is equal to `target`
# *     - A solution is guaranteed to exist
# !     - We are unable to use the same index multiple times
# * Instead of sorting the array, we can simply use an associative array
# * Ultimately, we know the following:
# *     - target = a + b
# *     - a = target - b
# *     - b = target - a
# * In other words, if we have ONE of either `a` or `b`, we know what the "complement" (the other summand)
# * Armed with this information, we can track the indices of values we have already found
# * Then, check if the complement of (target - nums[i]) exists within the associative array
# *     - If it does, then we simply get the index of that value, and we have our (i, j) indices
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n: int = len(nums)

        # * Value indices[int] is stored at index int
        indices: dict[int, int] = {}

        for i in range(0, n):
            # * We want to check if this value exists in the associative array
            complement: int = target - nums[i]

            if complement in indices:
                return [indices[complement], i]

            # * "nums[i] exists at index i"
            indices[nums[i]] = i

        raise ValueError("This code path should not be possible.")


sol: Solution = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # * [0, 1]
print(sol.twoSum([1, 2, 3], 4))  # * [0, 2]
print(sol.twoSum([1, 1], 2))  # * [0, 1]

# * Time: O(n^2) - We have a pair of nested loops, both of which scale with `n`

# * Space: O(1) - The memory usage remains constant regardless of input size
