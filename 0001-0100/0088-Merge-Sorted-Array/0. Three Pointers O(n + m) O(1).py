# 88. Merge Sorted Array

# * The length of `nums1` is equal to (n + m), the total length of both arrays
# * Additionally, we want to keep `nums1` sorted (monotonically non-decreasing)
# * We can use a two pointer approach where we always insert the largest element first
# * Based on that logic, we can use three pointers
# *     index: the index of the next inserted element
# *     left, and right: the indices of `nums1` and `nums2` we are considering
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # * Tracks progress through `nums1` and `nums2` respectively
        left: int = m - 1
        right: int = n - 1

        # * Index of next inserted element
        index: int = m + n - 1

        while left >= 0 and right >= 0:
            # * Insert the larger of the two elements
            if nums1[left] > nums2[right]:
                nums1[index] = nums1[left]
                left -= 1
            else:
                nums1[index] = nums2[right]
                right -= 1

            # * Move to the next position
            index -= 1

        # * Handle the remaining elements
        while right >= 0:
            nums1[index] = nums2[right]
            right -= 1
            index -= 1


# * Time: O(n + m) - The time taken scales with both inputs, there are `n + m` iterations

# * Space: O(1) - The memory usage remains constant regardless of input size
