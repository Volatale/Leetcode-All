# 4. Median of Two Sorted Arrays

# * We are given two `nums` and `nums2`, we need to return the MEDIAN of the arrays
# * If (n + m % 2), then the length of the combined array is EVEN
# *     - Take the sum of the two middle elements and and divide by 2 (find the average of the two mids)
# * Else, the length of the combined array is ODD
# *     - Here, we can simply return the middle element
# ! Merging the sorted arrays is a possibility, but we can actually improve on this using binary search
# *     - Ultimately, our search space is the range of indices in the COMBINED array (which is of length n + m)
# *     - We are searching for either ONE or TWO indices, so we also have "targets" to search for
# *     - We can also treat the fact that we want the MIDDLE indices as a form of "optimization" on the search
# * Since the arrays are sorted, the arrays exhibit monotonicity (non-decreasing order)
# * We aren't looking for a specific value; we are looking across the combined index space
# ! This is a problem involving partitioning since we don't have the combined arrays
# * The goal is to split the array such that there are `k` elements on the left (of the combined array)
# *     - Implicitly, this ensures the correct no. of elements on the right (of the combined array)
# *     - k = floor((n + m) / 2)
# * So to put this simply, we are looking for a `split` index `mid` and we want there to be `k` elements on the left of cut
# * If there are `i` elements on the left, then there should be `j` elements on the right
# *     - Thus, if (i + j == k), we know the choice was valid
# * We need `cut` points such that we can ensure there are K elements on the left of the sorted (combined) array
# *     - This is where `i` and `j` come from; they represent cut indices
# * Specifically, when we cut, we are cutting BETWEEN indices
# *     - We can cut at index 0: [], [1, 2]
# *     - We can cut at index 1: [1], [2]
# *     - Or, we can cut at index 2: [1, 2], []
# * Since our `i` represents `mid` (for binary search), `j` is DERIVED from `i`
# *     - Thus, we don't need to binary search to find the cut index on `nums2`
# ! Essentially, we are tracking [start, end] for nums1, and [start, end] for nums2
# *     - Specifically, it is [0, i - 1] and [i, j - 1]
# *        where `i` is the nums1 cut index and `j` is the nums2 cut index
# * Now, this looks like an "interval" problem, so we can check for overlaps
# *     - aStart <= bEnd && bStart <= aEnd
# * What does the formula check for?
# *     - It lets us check if the MAXIMUM of the lefts is SMALLER than the smallest on the right
# *         - If this is NOT the case, the current partitions are invalid
# * If aStart > bEnd
# *     - Then `i` is too large, so we need to search the left
# * Else, bStart > aEnd
# *     - Search the right; `i` is too small
# ! Technically, it is possible to binary search BOTH sides
# *     - So we should always binary search on the SMALLER of the inputs whenever possible
# *     - This reduces the time complexity
# ! Why do we use infinity to handle out of bounds accesses?
# *     - Because the arrays are SORTED, which implies monotonicity
# *     - Therefore, the minimum possible element is NEGATIVE infinity
# *     - And the largest possible element is POSITIVE infinity
# * Another way to look at this is: (max(A[i-1], B[j-1]) <= min(A[i], B[j]))
# *     - max(A[i-1], B[j-1]) = the largest element in the (combined) left side
# *     - min(A[i], B[j]) = the largest element in the (comnined) right side
# * If not, then:
# *     - If A[i-1] > B[j], we took too many from A (shift left cut)
# *     - If B[j-1] > A[i], we took too few from A (shift cut right)
# ! Variable name explanations:
# *     - aLeftMax = largest value in nums1's LEFT partition
# *     - aRightMin = smallest value in nums1's RIGHT partition
# *     - bLeftMAx = largest value in nums2's LEFT partition
# *     - bRightMin = smallest value in nums2's RIGHT partition
# * If aLeftMax > bRightMin
# *     - The LARGEST in nums1's left partition is GREATER than the SMALLEST in nums2's right partition
# *     - Thus, we need to take LESS elements from nums1 (hence right = i - 1)
# * if bLeftMax > aRightMin
# *     - The LARGEST in nums2's left partition is GREATER than the SMALLEST in nums2's right partition
# *     - Thus, we need to take MORE elements from nums2 (hence left = i + 1)


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure A is the smaller array (so we always binary search the smaller of the two)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Get the lengths of the inputs
        n: int = len(nums1)
        m: int = len(nums2)
        total: int = n + m

        # Size of the (combined) left partition
        # +1 to ensure left always has the extra element (in case of odd total length)
        half: int = (total + 1) // 2

        # We are searching over the full "cut space" in `nums1` (including nth index)
        left: int = 0
        right: int = n

        while left <= right:
            i: int = left + ((right - left) >> 1)  # Cut index in `nums1`
            j: int = half - i  # Cut index in `nums2`

            # Valid partition conditions
            aLeftMax = nums1[i - 1] if i > 0 else float("-inf")
            aRightMin = nums1[i] if i < n else float("inf")
            bLeftMax = nums2[j - 1] if j > 0 else float("-inf")
            bRightMin = nums2[j] if j < m else float("inf")

            # if max(aRightMin, bRightMin) <= min(aLeftMax, bLeftMax):
            if aLeftMax <= bRightMin and bLeftMax <= aRightMin:
                if total & 1:
                    # Extra element is in the LEFT partition
                    return max(aLeftMax, bLeftMax)
                else:
                    # Average of the maximum of the lefts and the minimum of the rights
                    return (max(aLeftMax, bLeftMax) + min(aRightMin, bRightMin)) / 2
            elif aLeftMax > bRightMin:
                right = i - 1  # We took too many elements from `nums1`, move left
            elif bLeftMax > aRightMin:
                left = i + 1  # We took too few elements from `nums1`, move right


# * Time: O(log(min(n,))) - We perform a binary search on the SMALLEST of the two arrays (hence min)
# * We assume the smaller to be `nums1`, but if `nums2` is smaller, we recursively call with the arguments swapped
# * Thus, the true time complexity scales with the minimum of the two input array lengths
# * The search space is halved within each iteration of the while loop

# * Space: O(1) - The memory usage remains constant regardless of input size
