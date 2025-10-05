# 41. FIrst Missing Positive

# * If we use a set, we can simply perform a membership check on the first missing positive
# * Add all of the elements `x` (where x > 0) to a set
# * Then, iterate from [1..n] and find the element that doesn't exist in the set
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        uniques: set[int] = set()

        # * Add all of the unique values to the set
        for x in nums:
            if x > 0:
                uniques.add(x)

        # * Find the first missing positive in the range [1..n + 1]
        for i in range(1, len(nums) + 2):
            if i not in uniques:
                return i


sol: Solution = Solution()
print(sol.firstMissingPositive([6, 4, 5, 1, 2]))  # * 3
print(sol.firstMissingPositive([4, 3, 2]))  # * 1
print(sol.firstMissingPositive([1, 2, 3, 4]))  # * 5
print(sol.firstMissingPositive([-1]))  # * 1
print(sol.firstMissingPositive([-1, 0]))  # * 1
print(sol.firstMissingPositive([4, 1, 3]))  # * 2

# * Time: O(n) - It takes O(n) to iterate over the `nums` array
# * Then, the time taken to find the first missing positive also scales with the length of the input
# * In the worst case, we perform n + 1 iterations


# * Space: O(n) - In the worst case, the list (and the set) hold `n` elements
