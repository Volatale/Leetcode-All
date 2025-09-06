# 11. Container With Most Water

# * We are given an int[] `height` of length `n`
# * The goal is to find the maximum area of the container given two indices (i, j)
# * Ultimately, we are trying to form rectangles and calculate their area
# *     - A = W * L
# * To get the width of the rectangle, we use the following formula:
# *     - (right - left)
# * Getting the length of the rectangle requires us to make some observations
# *     - The amount of water stored is bottlenecked by the minimum of height[left] and height[right]
# *     - Even if height[left] = 14, if height[right] = 8, then the length will be 8 for this calculation
# ! In a brute force manner, we can simply try every possible combination of (i, j)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water: int = 0
        n: int = len(height)

        for i in range(0, n):
            for j in range(0, n):
                width: int = j - i
                length: int = min(height[i], height[j])

                max_water = max(max_water, width * length)

        return max_water


sol: Solution = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # * 49
print(sol.maxArea([5, 5, 5]))  # * 10
print(sol.maxArea([1, 1]))  # * 1

# * Time: O(n^2) - The time taken scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
