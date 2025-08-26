# 4. Median of Two Sorted Arrays

# * We are given two `nums` and `nums2`, we need to return the MEDIAN of the arrays
# * If (n + m % 2), then the length of the combined array is EVEN
# *     - Take the sum of the two middle elements and and divide by 2 (find the average of the two mids)
# * Else, the length of the combined array is ODD
# *     - Here, we can simply return the middle element
# ! Combining the arrays and sorting the results is a possible solution, albiet a slow one
# * Instead, we can take advantage of the fact that the arrays are already sorted
# *     - It is possible to merge the arrays linearly while retaining the relative ordering of the inputs
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sorted_arr: list[int] = self._merge(nums1, nums2)
        length: int = len(sorted_arr)

        if length & 1:
            # Simply return the middle element in an even array
            return sorted_arr[length // 2]
        else:
            # Median of odd length array is the average of the two middle elements
            return (sorted_arr[length // 2 - 1] + sorted_arr[length // 2]) / 2

    def _merge(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result: list[int] = []
        n: int = len(nums1)
        m: int = len(nums2)

        # Pointers used to indicate the next value to be pushed to `result`
        left: int = 0
        right: int = 0

        while left < n and right < m:
            if nums1[left] <= nums2[right]:
                result.append(nums1[left])
                left += 1
            else:
                result.append(nums2[right])
                right += 1

        # Handle the leftover elements (guaranteed to be in sorted order from here on out)
        while left < n:
            result.append(nums1[left])
            left += 1

        while right < m:
            result.append(nums2[right])
            right += 1

        return result


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))  # 2
print(sol.findMedianSortedArrays([1, 2], [3, 4]))  #  2.5
print(sol.findMedianSortedArrays([], [3, 4]))  # 3.5
print(sol.findMedianSortedArrays([9], []))  # 9

# Time: O(n + m) - Merging both arrays takes O(n + m), followed by the O(1) time it to find the median

# Space: O(n + m) - The combined array has a length of n + m
