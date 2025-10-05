# 41. FIrst Missing Positive

# * Since we are only concerned with finding the first missing positive, we can avoid some work
# ! A cyclic sort approach will work here because we can disregard the other elements
# *     - Using cyclic sort, we can move any elements < 0 to the end of the array
# ! Why does cyclic sort work?
# *     - We are working with a limited range of values (specifically, x > 0)
# *       We don't care about the other values, so we can partition them away from the others
# * Cyclic sort generally follows one of two requirements:
# *     - Numbers in the range [0, n - 1]
# *     - And numbers in the range [1, n]
# *         - In our case, we are after the latter
# * Since we are concerned with numbers in the range [1, n]
# * index i should store the value i + 1
# *     - index 0 -> 1
# *     - index 1 -> 2
# *     - index 2 -> 3
# *     - index 3 -> 4
# ! We ONLY care about values in the range x > 0 and x <= n
# * Swap nums[i] with nums[x - 1] until nums[i] stores the correct value (i + 1)
# * If nums[i] == i + 1, then nums[i] is in the correct index
# *     - Thus we can increment i
# ! Eventually, the elements <= 0 will exist at indices [n:]
# * At which point we can iterate through the array from left to right and find the first missing positive
# *     - That is, the first index where nums[i] != i + 1
# *     - This works because we partitioned any the elements <= 0 to the end of the array (indices n and beyond)


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i: int = 0
        n: int = len(nums)

        while i < n:
            # * Range is [1, n]. x >= 1 should be stored at index (x - 1) (nums[0] = 1)
            correct_idx: int = nums[i] - 1

            # * Only numbers within the range [1, n] should be put into the correct index
            # * All other numbers will be placed toward the end of the array
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1  # * The element is at the correct index

        # * Find the first missing positive (nums[i] != i + 1)
        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


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

# * Space: O(1) - All of the swaps happen in-place, so the memory usage remains constant regardless of input size
