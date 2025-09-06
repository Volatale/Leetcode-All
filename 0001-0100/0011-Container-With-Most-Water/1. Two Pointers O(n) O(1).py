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
# * Instead of trying every possible combination of (i, j) using nested loops, we can use two pointers
# ! Another observation we can make is derived from the fact that the length is bottlenecked by the minimum length of the bars
# *     - Logically speaking, we always want to "improve the bottleneck"
# *     - In our case, that means trying to REDUCE the range of values between height[left] and height[right]
# *         - In other words, if we had (3, 9), the range of values is [3, 9]
# *     - But we want to reduce the distance between the two values, thereby maximizing the minimum of the two values (find an height[left] > 3)
# ! However, something to note is that reducing the distance between left and right also means the WIDTH will decrease
# *     - And the LENGTH is not necessarily guaranteed to increase (we are only ATTEMPTING to improve the bottleneck, greedily)
# * Thus, we should start `left` and `right` at index 0 and n - 1 respectively
# *     - This guarantees we start with the largest possible width
# * Within each iteration, we simply reduce the distance between left and right by incrementing or decrementing respectively
# ! Why does this approach work?
# * The bottleneck depends on the SHORTER of the two lines because water can't go above it
# * If we move the TALLER side inward:
# *     - The width shrinks
# *     - The height stays the same or might even decrease because the shorter line hasn't improved
# !     - Thus, the height cannot possibly increase (not only does the width decrease, so might the max(h[left], h[right]))
# * If we move the SHORTER side inward:
# *     - The width shrinks (unavoidable)
# *     - There is a CHANCE that the bottleneck improves, thereby increasing the overall area
# *     - In other words, the only way we can improve anything at all is by improving the bottleneck
# ! How does this check all "good" possibilities?
# *     - Each time we move a pointer, we discard one line forever
# *     - We ONLY discard a line if it cannot possibly lead to a larger area in the future
# *     - if height[left] < height[right], then the max area with left has already been found
# *         - We know that because moving right will never increase the area, it only stays as is or decreases
# *         - The same applies in the reverse, so we never miss the best combination
# ! How does the height[left] == height[right] case work?
# *     - If both are equal, moving either side is valid; BOTH are bottlenecks
# *       It doesn't matter which we compute because we already computed the area using that width
# *     - Remember, the width is still decreasing either way
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water: int = 0
        n: int = len(height)

        # * Two pointers
        left: int = 0
        right: int = n - 1

        while left < right:
            width: int = right - left
            length: int = min(height[left], height[right])

            max_water = max(max_water, width * length)

            # * Try to optimize the bottleneck (if equal, move either, doesn't matter)
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1

        return max_water


sol: Solution = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # * 49
print(sol.maxArea([5, 5, 5]))  # * 10
print(sol.maxArea([1, 1]))  # * 1

# * Time: O(n) - The time taken scales with the size of the input

# * Space: O(1) - The memory usage remains constant regardless of input size
