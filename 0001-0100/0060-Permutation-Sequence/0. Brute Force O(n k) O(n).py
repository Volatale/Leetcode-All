# 60. Permutation Sequence

# * Simply generate the kth permutation sequentially
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # * The 1st permutation is a sequence of increasing numbers (12345) etc.
        nums: list[int] = [x for x in range(1, n + 1)]

        # * Generate each successive lexicographical permutation until we hit the kth
        for _ in range(1, k):
            nums = self.generate(nums)

        # * Convert the list of nums into a string
        return "".join(map(str, nums))

    def generate(self, nums: list[int]) -> list[int]:
        n: int = len(nums)

        # * Find the first `i` where nums[i] < nums[i + 1]
        i: int = n - 2  # * We look -> so we can't start at the end

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # * Find the first `j` where nums[j] > nums[i]
        if i >= 0:
            j: int = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            # * Swap the values
            nums[i], nums[j] = nums[j], nums[i]

        # * Now reverse the rest of the list (i + 1 and beyond)
        nums[i + 1 :] = reversed(nums[i + 1 :])
        return nums


sol: Solution = Solution()
print(sol.getPermutation(1, 1))  # * "1"
print(sol.getPermutation(2, 2))  # * "21"
print(sol.getPermutation(2, 3))  # * "12"
print(sol.getPermutation(3, 4))  # * "231"
print(sol.getPermutation(4, 2))  # * "1243"
print(sol.getPermutation(4, 3))  # * "1324"
print(sol.getPermutation(4, 4))  # * "4123"

# * Time: O(n * k) - We have to generate `k` permutations in total
# * Within each permutation, in the worst case, we iterate over all `n` numbers

# * Space: O(n) - The memory usage scales with the size of `n` (there are n digits)
# * Additionally, the resulting string's size scales with `n`
