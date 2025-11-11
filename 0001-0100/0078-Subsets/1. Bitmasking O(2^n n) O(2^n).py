# 78. Subsets

# * Since there are always 2^n subsets, we can actually use bit manipulation to encode our choices
# *     - A 0 indicates that an element was NOT chosen in this mask
# *     - A 1 indicates that an element WAS chosen in this mask
# * We can iterate over a range of masks from [0 to (1 << n)]
# ! Each mask tells us whether to include the ith element or not
# * For example:
# *     - 0000 tells us not to include ANY elements
# *     - 0001 tells us to include the 0th
# *     - 0010 tells us to include the 1th
# *     - 0011 tells us to include the 0th and 1st
# *     - 1111 tells us to include ALL of the elements
# ! For each mask, iterate through the input array and check if the ith bit is set
# *     mask & (1 << i)
# * If it is, then we should append the current element to the current subset
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n: int = len(nums)
        results: list[list[int]] = []

        # * `mask` represents each of the subset configurations (0 = exclude, 1 = include)
        for mask in range(1 << n):
            s: list[int] = []

            # * Iterate over all of the elements
            for i in range(n):
                # * If the ith bit of the mask is set, we include the current element in the subset
                if mask & (1 << i):
                    s.append(nums[i])

            results.append(s)

        return results


# * Time: O(2^n * n) - There are 2^n subsets, and therefore 2^n masks
# * For each mask, we iterate over the entire input array

# * Space: O(2^n) - There are 2^n subsets in the output
