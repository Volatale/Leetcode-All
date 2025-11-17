# 84. Largest Rectangle in Histogram

# * Try every possible subarray and calculate the area between the two pointers
# *     Width = right - left + 1
# *     Height = min(height, height[right])
# * The "usable" height is bottlenecked by the minimum height in the subarray
# * Thus, if we have an array like [3, 2, 3]:
# *     1 * 3 = 3, which is fine
# *     Then extending to the next index (1) would give us (2 * 2) and NOT (3 * 2)
# *         - Why? Because min(3, 2) = 2. The height we HAD (3) was bottlenecked by the 2
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n: int = len(heights)
        max_area: int = 0

        # * Try every possible subarray
        for i in range(n):
            bottleneck_height: int = (1 << 31) - 1

            for j in range(i, n):
                # * `width` represents the no. of bars in the current range
                # * The "usable" height is bottlenecked by the minimum in the subarray
                width = j - i + 1
                bottleneck_height = min(bottleneck_height, heights[j])

                max_area = max(max_area, width * bottleneck_height)

        return max_area


sol: Solution = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # * 10
print(sol.largestRectangleArea([1, 1, 1]))  # * 3
print(sol.largestRectangleArea([2, 4]))  # * 4
print(sol.largestRectangleArea([1]))  # * 1

# * Time: O(n^2) - We have two for loops, both of which scale with `n`

# * Space: O(1) - The memory usage remains constant regardless of input size
