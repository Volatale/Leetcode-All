# 15. 3Sum

# * We are given an int[] and we need to find triplets such that nums[i] + nums[j] + nums[k] == 0
# *     - Specifically, i != j and j != k
# * The goal is to return an array of all of the triplets
# *     - We can't have duplicate triplets, so skip any that occur
# ! In a brute force manner, we can try every possible triplet
# *     - However, this makes it difficult to handle the duplicate triplets
# ! Instead we can sort the array, which introduces monotonicity
# * Then, we can reduce the problem to "Two Sum II" via two pointers
# * We know the array is sorted, therefore we can make the following observations:
# *     - If nums[i] + nums[j] + nums[k] > 0, then we decrement right (thereby decreasing the sum)
# *     - If nums[i] + nums[j] + nums[k] < 0, then we increment left (thereby increasing the sum)
# *     - Otherwise, the sum is equal to 0, so we can add this duplicate
# ! To handle the duplicate triplets, we can immediately move beyond the elements that would result in a duplicate
# * Specifically, the process we'll follow is to try forming a triplet STARTING with every `i`
# *     - Hence, after finding a triplet we skip all of the duplicates of nums[left] and nums[right]


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        n: int = len(nums)
        triplets: list[list[int]] = []

        # * Sort the array to enforce monotonicity (non-decreasing)
        nums.sort()

        # * `i` represents our leftmost value (the anchor)
        for i in range(0, n - 2):
            # ! If i - 1 was used in a (valid) triplet [i - 1, j, k], `i` will lead to a duplicate of that triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # * Use a two pointer approach; the array is monotonically non-decreasing
            left: int = i + 1
            right: int = n - 1

            while left < right:
                sum: int = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1  # * Need a larger sum
                elif sum > 0:
                    right -= 1  # * Need a smaller sum
                else:
                    # * Add the triplet to the pool
                    triplets.append([nums[i], nums[left], nums[right]])

                    # * Handle duplicate case (move to the FINAL (adjacent) duplicate for nums[left] and nums[right])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # * Skip to the last duplicate in left
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # * Skip to the last duplicate in right

                    # * Move away from the last duplicate
                    left += 1
                    right -= 1

        return triplets


sol: Solution = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # * [[-1, -1, 2], [-1, 0, 1]]
print(sol.threeSum([1, 0, 1]))  # * []
print(sol.threeSum([0, 0, 0]))  # * [[0, 0, 0]]
print(sol.threeSum([0, 0, -1, 1, 0]))  # * [[-1, 0, 1], [0, 0, 0]]

# * Time: O(n^2) - It takes O(n log n) to sort the array, however the overall time complexity is O(n^2)
# * For each outer iteration (n), we iterate over the entire array in the range [i + 1, n - 1] (left to right)
# * In the worst case, this is the entire array, so the true time complexity is O(n^2)

# * Space: O(k) - Where `k` is the number of triplets
