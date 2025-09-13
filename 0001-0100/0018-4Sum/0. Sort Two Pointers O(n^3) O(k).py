# 18. 4Sum

# * We are given an int[] nums, and we need to return unique quadruplets that sum to `target`
# * Specifically, the following rules must be followed:
# *     - 0 <= a, b, c, d < n
# *     - a, b, c, d are all distinct (the indices themselves)
# *     - nums[a] + nums[b] + nums[c] + nums[d] == target
# ! In a brute force manner, we can try every possible quadruplet, but this is slow
# * Ultimately, the goal is to create quadruplets that specifically sum to target
# ! Thus, a better approach involves sorting the array to enforce monotonicity
# * With a monotone array, can apply the following logic:
# * If nums[i] + nums[j] + nums[left] + nums[right] < target
# *     - Incrementing left will increase the sum
# * If nums[i] + nums[j] + nums[left] + nums[right] > target
# *     - Decrementing right will decrease the sum
# * Otherwise, sum == target, which means we found a valid quadruplet
# ! We cannot have identical quadruplets, however, so we need to skip some values
# * For example, if i > 0 and nums[i] == nums[i - 1], and nums[i - 1] lead to a quadruplet:
# *     - Then there [nums[i], nums[j], nums[left], nums[right]]] == [nums[i + 1], nums[j], nums[left], nums[right]]
# *     - So we don't even consider nums[i] since nums[i] == nums[i - 1]
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []

        quadruplets: list[list[int]] = []
        n: int = len(nums)

        # * Sorting the array introduces monotonicity
        nums.sort()

        for i in range(0, n - 3):
            # ! Skip the duplicate nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # ! Skip the duplicate nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # * Use two pointers and converge toward valid quadruplets
                left: int = j + 1
                right: int = n - 1

                while left < right:
                    sum: int = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum < target:
                        left += 1  # * We need a larger sum
                    elif sum > target:
                        right -= 1  # * We need a smaller sum
                    else:
                        # * Add the quadruplet
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                        # * Handle duplicates (move TO the final adjacent duplicate for both nums[left] and nums[right])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # * Move beyond the final duplicates for both pointers
                        left += 1
                        right -= 1

        return quadruplets


sol: Solution = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
print(sol.fourSum([2, 2, 2, 2, 2], 8))
print(sol.fourSum([1, 2, 3, 1, 2, 3, 0], 6))

# * Time: O(n^3) - We have 3 nested loops, each of which scales with the size of the input `n`
# * Additionally, sorting the array takes O(n log n)

# * Space: O(k) - The size of the `quadruples` array scales with the number of valid quadruples
# * Not every quadruple is valid, and each valid quadruple has size 4
# * So technically it'd be O(k * 4), but we drop constants with Big O Notation
