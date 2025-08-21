# 1. Two Sum

# * We need to return the indices of the two numbers whose sum is equal to `target`
# *     - A solution is guaranteed to exist
# !     - We are unable to use the same index multiple times
# * Instead of trying every pairing of numbers using nested loops, we can instead enforce monotonicity
# *     - The array is not guaranteed to be sorted, so if WE sort it, another approach becomes possible
# * We can use a two pointers approach where we converge on the correct indices from both sides
# * If nums[left] + nums[right] > target, then we know we need a smaller sum
# *     - Thus, right should be decremented
# * If nums[left] + nums[right] < target, then we know we need a larger sum
# *     - Thus, left should be incremented
# * If nums[left] + nums[right] == target, then we found our indices
# *     - Return [left, right]
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n: int = len(nums)

        # * Sort the array to enforce monotonicity and enable a two pointer approach
        nums.sort(key=lambda x: x)

        # * Variables for the two pointer approach
        left: int = 0
        right: int = n - 1

        while left < right:
            total: int = nums[left] + nums[right]

            if total == target:
                break  # * Found targets
            elif total > target:
                right -= 1  # * Need a smaller sum
            else:
                left += 1  # * Need a larger sum

        return [left, right]


sol: Solution = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # * [0, 1]
print(sol.twoSum([1, 2, 3], 4))  # * [0, 2]
print(sol.twoSum([1, 1], 2))  # * [0, 1]

# * Time: O(n log n) - On average, it takes O(n log n) to sort an array
# * Additionally, it takes O(n) to iterate over the input list `nums`

# * Space: O(sort) - If merge sort is used, the memory usage scales linearly with the input size (n)
# * If quick sort is used, the memory usage scales logarithmically (O(log n))
# * And if heap sort is used, the memory usage remains constant regardless of input size
