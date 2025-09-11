# 16. 3Sum Closest

# * We are given an int[] `nums`` and an int `target`
# * The goal is to find three integers in nums that sum up target (or as close as possible)
# *     - Specifically, we need to return the sum of those integers
# ! In a brute force manner, we can try getting the sum of every possible triplet
# *     - Add them to a set to eliminate duplicates
# * Once we have the set of sums we can sort the elements, which introduces monotonicity
# ! Then, we can binary search over the range of possible values
# * Why does this work?
# *     - The range of possible values is monotonically increasing (due to the sort)
# *     - We are guaranteed that a solution exists, so we'll converge on the result eventually


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        uniques: set[int] = set()
        n: int = len(nums)

        # * Get every possible triplet sum
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    uniques.add(nums[i] + nums[j] + nums[k])

        # * Get all the elements and sort them (sets are not sorted)
        sums: list[int] = sorted(uniques)

        # * Pointers so we can perform a binary search on `sums`
        left: int = 0
        right: int = len(sums) - 1
        closest: int = sums[0]  # * Start with the first sum

        while left <= right:
            # * `mid` represents the current value we are checking
            mid: int = left + ((right - left) >> 1)
            curr_sum: int = sums[mid]

            # * Update closest if this is nearer (abs value so (a - b) == (b - a))
            if abs(curr_sum - target) < abs(closest - target):
                closest = curr_sum

            if curr_sum == target:
                return curr_sum  # * Found a perfect match
            elif curr_sum < target:
                left = mid + 1  # * Need a larger sum
            else:
                right = mid - 1  # * Need a smaller sum

        # * The closest sum to target
        return closest


sol: Solution = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # * 2
print(sol.threeSumClosest([0, 0, 0], 0))  # * 2
print(sol.threeSumClosest([-4, 5, 1, 5, 7, 9], 8))  # * 8

# * Time: O(n^3) - Finding the sum of every triplet takes O(n^3) since we have 3 nested loops (all bounded by `n`)
# * Then, sorting the range of unique sums takes O(k log k) where `k` is the number of unique sums
# * Finally, the binary search takes O(k)

# * Space: O(k) - Where `k` is the number of unique sums
