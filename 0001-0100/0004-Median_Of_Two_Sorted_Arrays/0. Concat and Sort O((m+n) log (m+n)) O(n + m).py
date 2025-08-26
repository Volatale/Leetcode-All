# 4. Median of Two Sorted Arrays

# * We are given two `nums` and `nums2`, we need to return the MEDIAN of the arrays
# * In a brute force manner, we can simply combine the arrays, sort it, and handle the median appropriately
# * If (n + m % 2), then the length of the combined array is EVEN
# *     - Take the sum of the two middle elements and and divide by 2 (find the average of the two mids)
# * Else, the length of the combined array is ODD
# *     - Here, we can simply return the middle element
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m: int = len(nums1)
        n: int = len(nums2)
        length: int = m + n

        # Combine the array and sort it to enforce monotonicity
        sorted_arr: list[int] = sorted([*nums1, *nums2], key=lambda x: x)

        if length & 1:
            # Simply return the middle element in an even array
            return sorted_arr[length // 2]
        else:
            # Median of odd length array is the average of the two middle elements
            return (sorted_arr[length - 1 // 2] + sorted_arr[length // 2]) / 2


# Time: O((m + n) log (m + n)) - Assume it takes O(n log n) to sort
# Calculating the median from that point onward is a constant time operation

# Space: O(n + m) - Depending on the sorting algorithm used, the memory usage may scale with the size of BOTH inputs
