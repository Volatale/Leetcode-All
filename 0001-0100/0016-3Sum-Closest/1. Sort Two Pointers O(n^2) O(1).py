# 16. 3Sum Closest

# * We are given an int[] `nums`` and an int `target`
# * The goal is to find three integers in nums that sum up target (or as close as possible)
# *     - Specifically, we need to return the sum of those integers
# ! Sorting the array enforces monotonicity (non-decreasing)
# * Monotonicity allows us to reduce the problem to using two pointers
# *     - The invariant states that nums[left] <= nums[right]
# * Thus, if nums[i] + nums[left] + nums[right] > target
# *     - By decrementing right, we'll move toward a smaller sum
# * Likewise, if nums[i] + nums[left] + nums[right] < target
# *     - By incrementing left, we'll move toward a larger sum
# * If the sum == target, then we found an exact match
# * Specifically, our goal is to reduce the difference between sum and target as much as possible
# *     - There are no ties either, so we know a solution exists
# ! When we calculate the sum, we take the absolute value
# * That way, we are only working on one axis
# *     - [0, Infinity] alone, vs
# *     - [-Infinity, 0] and [0, Infinity]


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n: int = len(nums)
        closest: int = 2**31 - 1  # * We want to converge toward 0

        # * Sort the values into non-descending order to enforce monotonicity
        nums.sort()

        # * Try every triplet starting with each nums[i]
        for i in range(0, n - 2):
            # * Two pointers to converge on the closest
            left: int = i + 1
            right: int = n - 1

            while left < right:
                curr_sum: int = nums[i] + nums[left] + nums[right]

                # * Check if we found a closer sum to target
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum < target:
                    left += 1  # * Try a larger sum
                elif curr_sum > target:
                    right -= 1  # * Try a smaller sum
                else:
                    return curr_sum  # * Found a perfect match

        return closest


sol: Solution = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # * 2
print(sol.threeSumClosest([0, 0, 0], 0))  # * 2
print(sol.threeSumClosest([-4, 5, 1, 5, 7, 9], 8))  # * 8
print(sol.threeSumClosest([1, 1, 1, 0], 100))  # * 3
print(sol.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))  # * -2

# * Time: O(n^2) - It takes O(n log n) to sort the input array
# * Then, for each element nums[i], we perform an O(n) iteration in the worst case

# * Space: O(1) - The `sort()` method in Python uses Timsort, which is O(1)
